import csv
import pandas as pd
import numpy as np
age = [35,46,56,66] #диапазон возрастов
with open('db1.csv') as csv_file, open ('db2.csv','w', newline='', encoding='utf-8') as outf:
    csv_reader = csv.reader(csv_file, delimiter=';')
    csv_writer = csv.writer(outf, delimiter=';')
    for row in csv_reader:
        row[25]=row[25].replace(',','.') #замена , на . для чтения как float
        d = int(row[2])
        #разбиение на возрастные группы
        if (d>=age[0] and d<age[1]): #35-45
            row.append(age[0]) #35
        elif (d>=age[1] and d<age[2]): #46-56
            row.append(age[1]) #46
        elif (d>=age[2] and d<age[3]):
            row.append(age[2])  # 56
        else:
            row.append(age[3])  # >66
        csv_writer.writerow(row)
#разбиение файла на выборки
df = pd.read_csv('db2.csv', header=None, sep=';')
del df[2]
msk = np.random.rand(len(df)) <= 0.9
df[3] = df[3].astype(bool).astype(int)
train = df[msk]
test = df[~msk]
# for i in range(4,9):
#     del test[i]
test.to_csv('test.csv', sep=';', header=None, index=False,  encoding='utf-8')
train.to_csv('train.csv', sep=';', header=None, index=False,  encoding='utf-8')












