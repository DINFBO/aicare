#-*- coding: utf-8 -*-

a = {'우울증':0, '자살':1, '불안장애':2}
b = ['', '_RD', '_RS', '_RD+RS']

for tmp in b:
    result = []
    for filename in list(a.keys()):
        with open(filename+tmp+'.txt', 'r', encoding='cp949') as f:
            data = f.readlines()
            for i in data:
                result += i[:-1].replace(',','')+','+str(a[filename])+'\n'
    

    with open('data'+tmp+'.csv', 'w', encoding='cp949') as f:
        f.writelines(result)
