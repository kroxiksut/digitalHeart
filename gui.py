from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout, QTableView
import sys
from mainGui import design
class HeartApp(QtWidgets.QMainWindow, design.Ui_heartUI, QTableView):
    def __init__(self):
        #super(HeartApp, self).__init__() # Call the inherited classes __init__ method
        #uic.loadUi('form.ui', self) # Load the .ui file
        #self.show() # Show the GUI
        super().__init__()
        CSV_COLUMN_NAMES = ['id', 'place', 'sex', 'onmk', 'ibs', 'd_heart',
                            'nedost heart', 'art hyper', 'obrazov', 'ecg norm', 'regular drags', 'sugar diaber',
                            'hepatit', 'onco', 'hron lung', 'astma', 'tuberc', 'spid', 'lek davl',
                            'lek holest', 'lek insult', 'lek diabet', 'lek astma', 'kurit', 'percent fat', 'medium age']

        data = [[1,2,3],[3,4,5],[6,7,8]]
        self.setupUi(self)

        #self.myTable.setEnabled(False)

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = HeartApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()