# import tensorflow as tf
import pandas as pd

# import numpy as np
# from matplotlib import pyplot as plt

# from tensorflow import keras
# from tensorflow.keras import layers

from keras.models import Sequential
from keras.layers import Dense

def trainHeart(path_train, path_test, desease):
    CSV_COLUMN_NAMES = ['id', 'place', 'sex', 'onmk', 'ibs', 'd_heart',
                        'nedost heart', 'art hyper','obrazov', 'ecg norm','regular drags','sugar diaber',
                         'hepatit','onco','hron lung','astma','tuberc','spid','lek davl',
                        'lek holest','lek insult','lek diabet','lek astma','kurit','percent fat','medium age']
    train = pd.read_csv(path_train, names=CSV_COLUMN_NAMES, header=0, sep=';')
    test = pd.read_csv(path_test, names=CSV_COLUMN_NAMES, header=0,sep=';')
    train.pop('id')
    test.pop('id')
    trainONMK = train.pop(desease)
    testONMK = test.pop(desease)

    model = Sequential()
    model.add(Dense(120, input_dim=24, activation='relu'))
    model.add(Dense(24, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(train, trainONMK, epochs=700, batch_size=20)
    #print("ddfdfdf")
    _, accuracy = model.evaluate(test, testONMK)
    print('Accuracy: %.2f' % (accuracy*100))
    model.save(desease+'.h5')
    return round(accuracy*100,2)

trainHeart('train.csv','test.csv', 'nedost heart')

