import sys
import os
import random

import PySide2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter, QColor, QPixmap
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QInputDialog, QLabel
from PyQt5.QtWidgets import QCheckBox, QLabel, QLineEdit, QVBoxLayout
import sqlite3
import datetime


class AboutWindow(QWidget):  # Menubar
    def __init__(self):
        super(AboutWindow, self).__init__()
        self.setLayout(QVBoxLayout(self))
        self.info = QLabel(self)
        self.info.setFont(QtGui.QFont("Roboto", 14))
        self.info.setText('Github profiles: Nikdevelop and jur4ikoff')  # о создателях
        self.layout().addWidget(self.info)


class AboutWindow_1(QWidget):  # Menubar
    def __init__(self):
        super(AboutWindow_1, self).__init__()
        self.setLayout(QVBoxLayout(self))
        self.info1 = QLabel(self)
        self.info1.setFont(QtGui.QFont("Roboto", 14))
        self.info1.setText('Этот проект был написан в рамках проектной деятельности в 10 классе.' "\n"
                           ' С помощью языков программирования и нейросетей, ' "\n"
                           ' мы написали программу по анализу и авторизации по уникальному' "\n"
                           ' графическому символу, введеного пользователем')  # о создателях
        self.layout().addWidget(self.info1)


class OpenWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # uic.loadUi('main.ui', self)
        uic.loadUi('Main1.ui', self)
        # self.setStyleSheet("QMainWindow{background-color: #2A3038;}")
        self.about_window = AboutWindow()
        self.about_window_1 = AboutWindow_1()
        # self.about_action.triggered.connect(self.about)
        # self.about_action_2.triggered.connect(self.about_1)
        self.initUI()

    def about(self):
        print('hello nahuy')
        self.about_window.show()

    def about_1(self):
        self.about_window_1.show()

    def initUI(self):
        print('Открыто Приложение')  # Для отладки


if __name__ == '__main__':
    app = QApplication(sys.argv)
    opn = OpenWindow()
    opn.show()
    sys.exit(app.exec())
