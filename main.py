import sys
import os
import random

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter, QColor, QPixmap
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QInputDialog, QLabel
from PyQt5.QtWidgets import QCheckBox, QLabel, QLineEdit, QVBoxLayout
import sqlite3
import DateTime


class AboutWindow(QWidget):  # Menubar
    def __init__(self):
        super(AboutWindow, self).__init__()
        self.setWindowTitle('О программе')
        self.setLayout(QVBoxLayout(self))
        self.info = QLabel(self)
        self.info.setText('Github profiles: Nikdevelop and jur4ikoff')  # о создателях
        self.layout().addWidget(self.info)

   # def retranslateUi(self, MainWindow):
   #     _translate = QtCore.QCoreApplication.translate
   #     MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
   #     self.label.setText(_translate("MainWindow", "Ссылка"))
   #     self.label_2.setText(_translate("MainWindow", "https://ru.stackoverflow.com/"))


class OpenWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.initUI()
        self.about_window = AboutWindow()
        self.about_action.triggered.connect(self.about)

    def about(self):
        self.about_window.show()

    def initUI(self):
        print('Открыто Приложение')  # Для отладки


if __name__ == '__main__':
    app = QApplication(sys.argv)
    opn = OpenWindow()
    opn.show()
    sys.exit(app.exec())
