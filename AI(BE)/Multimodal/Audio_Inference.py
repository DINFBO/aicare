# #필요한 모듈 설치하기
# !pip install mxnet
# !pip install torch
# !pip install 'scikit-learn<0.23'
# !pip install gluonnlp
# !pip install sentencepiece
# !pip install transformers==3.0.2
# !pip install speechrecognition
# !pip install git+https://git@github.com/SKTBrain/KoBERT.git@master
# !pip install librosa

# 기본 라이브러리 불러오기
import numpy as np

import librosa

import torch
from torch import nn
import torch.nn.functional as F
import gluonnlp as nlp

#kobert라이브러리에서 많이 쓰이는 함수 불러오기
from kobert.utils import get_tokenizer
from kobert.pytorch_kobert import get_pytorch_kobert_model
import pickle

import speech_recognition as sr

r = None
scaler = None
bertmodel = None
sentence_transformer = None
device_type = None
device = None
model = None
labels = None

def score(audio_file, device_type='cpu'):
    global device, model, label_encoder, labels

    data, sample_rate = librosa.load(audio_file, duration=2.5, offset=0.6)
    audio = extract_features(data, sample_rate)
    audio = transform_audio(audio)

    audio_file.seek(0)
    text = make_text(audio_file)
    input_token_ids, valid_length, input_token_type_ids = transform_text(text)

    if device_type != 'gpu':
        device_type = 'cpu'
    if device is None or device_type != globals()['device_type']:
        globals()['device_type'] = device_type
        device = torch.device(device_type)
        model = None
    if model is None:
        model = torch.load('multimodal_emotion_classification.pt',map_location=device)
        model.eval()

        audio = audio.to(device)
        input_token_ids = input_token_ids.to(device)
        valid_length = valid_length.to(device)
        input_token_type_ids = input_token_type_ids.to(device)
    
    output = model(audio, input_token_ids, valid_length, input_token_type_ids)
    
    if labels is None:
        with open('label_encoder.pkl','rb') as f:
            label_encoder = pickle.load(f)
        labels = label_encoder.classes_.tolist()

    result = list(zip(labels, output.detach()[0].tolist()))
    result.sort(key=lambda x: x[-1], reverse=True)
    return result

def make_text(audio_file):
    global r
    if r is None:
        r = sr.Recognizer()

    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)

    text = r.recognize_google(audio, language='ko-KR')
    return text

# 음성의 특성추출하는 함수 ( MFCC, MEL, RMSV)
def extract_features(audio_data, sample_rate):
    audio = np.array([])

    # MFCC
    mfcc = np.mean(librosa.feature.mfcc(y=audio_data, sr=sample_rate).T, axis=0)
    audio = np.hstack((audio, mfcc)) # stacking horizontally

    # Root Mean Square Value
#    rms = np.mean(librosa.feature.rms(y=data).T, axis=0)
#    result = np.hstack((result, rms)) # stacking horizontally

    # MelSpectogram
    mel = np.mean(librosa.feature.melspectrogram(y=audio_data, sr=sample_rate).T, axis=0)
    audio = np.hstack((audio, mel)) # stacking horizontally

    return audio

def transform_audio(audio):
    global scaler
    if scaler is None:
        with open('scaler.pkl','rb') as f:
            scaler = pickle.load(f)

    audio = np.array(audio).reshape(1, -1)  # 음성 데이터

    # 음성 데이터 스케일 조정
    audio = scaler.transform(audio)

    # 음성 데이터의 차원 모델에 맞게 통일 
    audio = np.expand_dims(audio, axis=2)

    audio = torch.tensor(audio, dtype=torch.float32)
    return audio

#문장을 토크나이저를 통해서 토큰으로 변환(토큰화)
def transform_text(text):
    global bertmodel, sentence_transformer
    if sentence_transformer is None:
        tokenizer = get_tokenizer()
        with open('kobert_data.pkl', 'rb') as f:
            bertmodel, vocab, _ = pickle.load(f)
        # bertmodel, vocab = get_pytorch_kobert_model()
        tok = nlp.data.BERTSPTokenizer(tokenizer, vocab, lower=False)
        sentence_transformer = nlp.data.BERTSentenceTransform(
            tok, max_seq_length=50, pad=True, pair=False)

    input_token_ids, valid_length, input_token_type_ids = (torch.tensor(z.reshape(1,-1)) for z in sentence_transformer(text))
    return input_token_ids, valid_length, input_token_type_ids

# 음성 모델 만들기
class AudioClassifier(nn.Module):
    def __init__(self):
        super(AudioClassifier, self).__init__()
        self.conv1 = nn.Conv1d(in_channels=148, out_channels=256, kernel_size=1, stride=1,padding='same')
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