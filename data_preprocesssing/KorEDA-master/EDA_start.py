#-*- coding: utf-8 -*-
from eda import EDA

a = ['우울증','불안장애','자살']

for filename in a:
  with open('../'+filename+'.txt', 'r', encoding='cp949') as f:
    data = f.readlines()

    for params in [['RD+RS', 1,1], ['RS', 0, 1], ['RD', 1, 0]]:
      result = []
      for i in data:
        tmp = []
        for j in range(3):
          tmp += ([j+'\n' for j in EDA(i[:-1], rd = params[1], rs = params[2])])
        result += list(set(tmp+[i]))
      with open('../EDA/'+filename+'_'+params[0]+'.txt', 'w', encoding='cp949') as f2:
        f2.writelines(result)
