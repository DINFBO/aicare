import os
os.chdir('koremo')

from koremo.koremo import pred_emo, save_data_s_rmse, pred_data_s_rmse

save_data_s_rmse()

from keras.models import load_model

models = ('total_s_rmse_cnn_rnnself-20-0.9645-f0.9644', 'total_s_rmse_cnn_rnnself_re-19-0.9723-0.9701')
for filename in models:
    mse_crs = load_model('model/' + filename + '.hdf5', compile=False)
    print(pred_emo(mse_crs, ['../으악-내눈.wav', 'M_000001.wav', 'F_000001.wav']))
    pred_data_s_rmse(mse_crs, '../' + filename)

import pandas as pd
data = pd.read_csv('../data.csv', index_col=0)

import numpy as np
labels = {0: 'Angry', 1: 'Fear', 2: 'Joy', 3: 'Normal', 4: 'Sad'}
for filename in models:
    pred = np.load('../' + filename + '.npy')
    data['pred'] = pred
    data['label'] = data['pred'].map(labels)
    data.groupby(['감정_대분류', 'label']).count().iloc[:,[0]].to_csv('../matrix_' + filename + '.csv')