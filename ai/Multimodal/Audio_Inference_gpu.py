# #필요한 모듈 설치하기
# !pip install mxnet
# !pip install gluonnlp pandas tqdm
# !pip install sentencepiece
# !pip install transformers==3.0.2
# !pip install torch
# !pip install sklearn
# !pip install numpy
# !pip install git+https://git@github.com/SKTBrain/KoBERT.git@master
# !pip install speechrecognition

# 기본 라이브러리 불러오기
import pandas as pd
import numpy as np
import os
import sys

from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split

import librosa
import librosa.display

# 경고메세지 숨기기
import warnings
if not sys.warnoptions:
    warnings.simplefilter("ignore")
warnings.filterwarnings("ignore", category=DeprecationWarning) 

import torch
from torch import nn
import torch.nn.functional as F
import gluonnlp as nlp
from tqdm import tqdm, tqdm_notebook

#kobert라이브러리에서 많이 쓰이는 함수 불러오기
from kobert.utils import get_tokenizer
from kobert.pytorch_kobert import get_pytorch_kobert_model
#transformers에서 하이퍼파라미터 세팅
from transformers import AdamW
from transformers.optimization import get_cosine_schedule_with_warmup
import pickle

import speech_recognition as sr

#GPU 사용(권장)
device = torch.device("cuda:0")
#CPU 사용
#device = torch.device("cpu")

if __name__ == '__main__':
    argument = sys.argv[1]

data_path = argument # argmument

r = sr.Recognizer()
harvard = sr.AudioFile(data_path)
with harvard as source:
  audio = r.record(source)
text = r.recognize_google(audio, language='ko-KR')

# 음성의 특성추출하는 함수 ( MFCC, MEL, RMSV)
def extract_features(data):

    result = np.array([])

    # MFCC
    mfcc = np.mean(librosa.feature.mfcc(y=data, sr=sample_rate).T, axis=0)
    result = np.hstack((result, mfcc)) # stacking horizontally

    # Root Mean Square Value
#    rms = np.mean(librosa.feature.rms(y=data).T, axis=0)
#    result = np.hstack((result, rms)) # stacking horizontally

    # MelSpectogram
    mel = np.mean(librosa.feature.melspectrogram(y=data, sr=sample_rate).T, axis=0)
    result = np.hstack((result, mel)) # stacking horizontally
    
    return result

data, sample_rate = librosa.load(data_path, duration=2.5, offset=0.6)
x = np.array(extract_features(data)).reshape(1, -1)  # 음성 데이터
z = text

# # 음성 데이터 스케일 조정
with open('scaler.pkl','rb') as f:
  scaler = pickle.load(f)
x = scaler.transform(x)
# 음성 데이터의 차원 모델에 맞게 통일 
x = np.expand_dims(x, axis=2)

X = torch.tensor(x, dtype=torch.float32)

#문장을 토크나이저를 통해서 토큰으로 변환(토큰화)
with open('kobert_data.pkl', 'rb') as f:
  bertmodel, vocab, _ = pickle.load(f)
tokenizer = get_tokenizer()
tok = nlp.data.BERTSPTokenizer(tokenizer, vocab, lower=False)

transform = nlp.data.BERTSentenceTransform(
            tok, max_seq_length=50, pad=True, pair=False)

Z = list(transform(z))
Z1, Z2, Z3 = torch.tensor(Z[0].reshape(1,-1)),torch.tensor(Z[1].reshape(1,-1)),torch.tensor(Z[2].reshape(1,-1))

# 음성 모델 만들기
class AudioClassifier(nn.Module):
    def __init__(self):
        super(AudioClassifier, self).__init__()
        self.conv1 = nn.Conv1d(in_channels=x_train.shape[1], out_channels=256, kernel_size=1, stride=1,padding='same')
        self.max_pool1 = nn.MaxPool1d(5, stride=2, padding = 2)

        self.conv2 = nn.Conv1d(in_channels=256, out_channels=256, kernel_size=5, stride=1, padding='same')
        self.max_pool2 = nn.MaxPool1d(5, stride=2, padding = 2)

        self.conv3 = nn.Conv1d(in_channels=256, out_channels=128, kernel_size=5, stride=1, padding='same')
        self.max_pool3 = nn.MaxPool1d(5, stride=2, padding = 2)
        self.dropout1 = nn.Dropout(0.2)
        
        self.conv4 = nn.Conv1d(in_channels=128, out_channels=64, kernel_size=5, stride=1, padding='same')
        self.max_pool4 = nn.MaxPool1d(5, stride=2, padding = 2)
        
        self.fc1 = nn.Linear(64, 32)
        self.dropout2 = nn.Dropout(0.6)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = self.max_pool1(x)

        x = F.relu(self.conv2(x))
        x = self.max_pool2(x)

        x = F.relu(self.conv3(x))
        x = self.max_pool3(x)
        x = self.dropout1(x)

        x = F.relu(self.conv4(x))
        x = self.max_pool4(x)

        x = torch.flatten(x,1)

        x = F.relu(self.fc1(x))
        x = self.dropout2(x)
        
        return x

# KoBERT 학습모델 만들기
class BERTClassifier(nn.Module):
    def __init__(self,
                 bert,
                 hidden_size = 768,
                 num_classes=32,   ##클래스 수 조정##
                 dr_rate=None,
                 params=None):
        super(BERTClassifier, self).__init__()
        self.bert = bert
        self.dr_rate = dr_rate
                 
        self.classifier = nn.Linear(hidden_size , num_classes)
        if dr_rate:
            self.dropout = nn.Dropout(p=dr_rate)
    
    def gen_attention_mask(self, token_ids, valid_length):
        attention_mask = torch.zeros_like(token_ids)
        for i, v in enumerate(valid_length):
            attention_mask[i][:v] = 1
        return attention_mask.float()

    def forward(self, token_ids, valid_length, segment_ids):
        attention_mask = self.gen_attention_mask(token_ids, valid_length)
        
        _, pooler = self.bert(input_ids = token_ids, token_type_ids = segment_ids.long(), attention_mask = attention_mask.float().to(token_ids.device))
        if self.dr_rate:
            out = self.dropout(pooler)
        return self.classifier(out)

# 멀티모달 모델 만들기
class MultimodalClassifier(nn.Module):
    def __init__(self, audioModel, textModel):
        super(MultimodalClassifier, self).__init__()
        self.audioModel = audioModel
        self.textModel = textModel

        self.fc1 = nn.Linear(64,32)
        self.dropout1 = nn.Dropout(0.2)

        self.fc2 = nn.Linear(32, 5)

    def forward(self, x1, token_ids, valid_length, segment_ids):
        x1 = self.audioModel(x1)
        x2 = self.textModel(token_ids, valid_length, segment_ids)
        x = torch.cat((x1,x2), 1)
        x = F.relu(self.fc1(x))
        x = self.dropout1(x)
        
        x = F.relu(self.fc2(x))
        return x

model = torch.load('multimodal_emotion_classification.pt')

output = model(X.to(device), Z1.to(device), Z2.to(device),Z3.to(device))
output

with open('label_encoder.pkl','rb') as f:
  le = pickle.load(f)
result = le.inverse_transform([torch.argmax(output.cpu())])

print(result[0])