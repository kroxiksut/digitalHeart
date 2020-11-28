import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
import tensorflow as tf
import numpy as np
import P
from tensorflow import keras
model = keras.models.load_model("onmk.h5")
CSV_COLUMN_NAMES = ['id', 'place', 'sex', 'onmk', 'ibs', 'd_heart',
                    'nedost heart', 'art hyper','obrazov', 'ecg norm','regular drags','sugar diaber',
                     'hepatit','onco','hron lung','astma','tuberc','spid','lek davl',
                    'lek holest','lek insult','lek diabet','lek astma','kurit','percent fat','medium age']
test = pd.read_csv('test.csv', names=CSV_COLUMN_NAMES, header=0,sep=';')
test.pop('id')
testONMK = test.pop('onmk')
# np.testing.assert_allclose(
#     model.predict(test), model.predict(test)
# )
# model.fit(test,testONMK)
#data = [2,58,1,0,0,0,0,5,1,0,0,1,0,1,1,0,1,0,1,0,0,1,0,36.8,56]
data = [2,0,0,0,0,0,3,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,29.8,56] #onmk0
#data = [2,53,0,0,0,0,1,4,0,1,1,0,0,0,0,0,0,1,0,0,0,0,1,25.5,46] #onmk1
pr = model.predict([data])
print(pr)