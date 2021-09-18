import os

os.chdir('koremo')
from koremo.koremo import pred_emo

os.chdir('..')
pred_emo('으악-내눈.wav')
pred_emo('M_000001.wav')
pred_emo('F_000001.wav')