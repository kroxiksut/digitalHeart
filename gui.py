from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout, QTableView, QMessageBox
import sys
from mainGui import design
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
import tensorflow as tf
import numpy as np

from tensorflow import keras
model = keras.models.load_model("onmk.h5")
class HeartApp(QtWidgets.QMainWindow, design.Ui_heartUI):
    def __init__(self):
        #super(HeartApp, self).__init__() # Call the inherited classes __init__ method
        #uic.loadUi('form.ui', self) # Load the .ui file
        #self.show() # Show the GUI
        super().__init__()
        CSV_COLUMN_NAMES = ['id', 'place', 'sex', 'onmk', 'ibs', 'd_heart',
                            'nedost heart', 'art hyper', 'obrazov', 'ecg norm', 'regular drags', 'sugar diaber',
                            'hepatit', 'onco', 'hron lung', 'astma', 'tuberc', 'spid', 'lek davl',
                            'lek holest', 'lek insult', 'lek diabet', 'lek astma', 'kurit', 'percent fat', 'medium age']

        self.setupUi(self)
        self.rb_manual.toggled.connect(self.selectInputManual)
        self.rb_console.toggled.connect(self.selectInputConsole)
        # self.gb_console.setEnabled(True)
        # self.gb_manual.setEnabled(False)
        self.btnRez.clicked.connect(self.calcResult)
        self.pb_demo1.clicked.connect(self.demoOne)
        self.pb_demo2.clicked.connect(self.demoTwo)
        self.pb_demo3.clicked.connect(self.demoThree)
        # if self.rb_manual.isChecked():
        #     self.gb_console.setEnabled(False)
        #     self.gb_manual.setEnabled(True)
        # else:
        #     self.gb_manual.setEnabled(False)
        #     self.gb_console.setEnabled(True)

        #self.myTable.setEnabled(False)

    def calcRes(self):
        self.gb_manual.isChecked()
    def selectInputManual(self):
        self.gb_console.setEnabled(False)
        self.gb_manual.setEnabled(True)
    def selectInputConsole(self):
        self.gb_manual.setEnabled(False)
        self.gb_console.setEnabled(True)
    def predictResult(self, data):
        rez =0.0
        return rez
    def demoOne(self):
        self.pte_console.setPlainText("2;0;0;0;0;0;3;0;1;0;0;0;0;0;0;0;0;0;0;0;0;1;29.8;56")
    def demoTwo(self):
        self.pte_console.setPlainText("2;0;0;0;0;1;4;0;1;1;0;0;0;0;0;0;1;0;0;0;0;1;25.5;46")
    def demoThree(self):
        self.pte_console.setPlainText("1;1;1;0;1;1;5;1;1;0;1;0;0;0;0;0;1;0;0;0;0;0;48.1;66")

    def calcResult(self):
        if self.rb_console.isChecked():
            text = self.pte_console.toPlainText()
            data = text.split(';')
            dd = []
            for i in data:
                if(len(i)>2):
                    dd.append(float(i))
                else:
                    dd.append(int(i))

            pr = model.predict([dd])
            v = list(np.reshape(np.asarray(pr), (1, np.size(pr )))[0])
            # print(v[0])
            # self.l_rez.setText(str(type(float(data[22]))))
            # self.l_rez.setText(str(pr))
            self.l_rez.setText("Вероятность заболевания - "+ str(round(v[0]*100,2))+"%")
        else:
            QMessageBox.about(self, "Test", "Manual")



def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = HeartApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()