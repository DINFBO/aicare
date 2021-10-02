import os
os.chdir('koremo')

from koremo.koremo import pred_emo, save_data_s_rmse, pred_data_s_rmse

data_names = sorted(os.listdir('../data'))
save_data_s_rmse(data_names)

from tensorflow.compat.v1.keras.models import load_model
import pandas as pd
model_names = ('model_for_6.h5',)
data_s_rmse_names = sorted(os.listdir('../data_s_rmse'), key=lambda filename: int(filename[:-len('.npy')]))
data = pd.read_csv('../data.csv', index_col=0)
labels = {0: 'Angry', 1: 'Fear', 2: 'Joy', 3: 'Normal', 4: 'Sad'}
for model_name in model_names:
    mse_crs = load_model('model/' + model_name, compile=False)
    pred = pred_data_s_rmse(mse_crs, data_s_rmse_names)
    data['pred'] = pred
    data['label'] = data['pred'].map(labels)
    csv_name = os.path.splitext(model_name)[0] + '.csv'
    data.loc[:,['NO.', '감정_대분류', 'label']].to_csv('../pred_' + csv_name)
    data.groupby(['감정_대분류', 'label']).count().iloc[:,[0]].to_csv('../count_' + csv_name)