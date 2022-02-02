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
        self.setWindowTitle('О программе')
        self.setLayout(QVBoxLayout(self))
        self.info = QLabel(self)
        self.info.setFont(QtGui.QFont("Roboto", 14))
        self.info.setText('Github profiles: Nikdevelop and jur4ikoff' "\n"
                          'Этот проект был написан в рамках проектной деятельности в 10 классе.' "\n"
                          ' С помощью языков программирования и нейросетей, ' "\n"
                          ' мы написали программу по анализу и авторизации по уникальному' "\n"
                          ' графическому символу, введеного пользователем'
                          )  # о создателях
        self.info.setStyleSheet("color: rgb(255, 255, 255)")
        self.setStyleSheet("border-radius: 40px; background-color: qlineargradient(spread:pad, x1:0, y1:0,\
         x2:1, y2:1, stop:0 rgba(41, 37, 54, 255), stop:1 rgba(39, 37, 55, 255));")
        self.layout().addWidget(self.info)


class OpenWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # uic.loadUi('main.ui', self)
        uic.loadUi('Main1.ui', self)
        # self.setStyleSheet("QMainWindow{background-color: #2A3038;}")
        self.about_window = AboutWindow()
        self.action_button.clicked.connect(self.about)
        self.close_wnd.clicked.connect(self.terminate)
        # self.about_action_2.triggered.connect(self.about_1)
        self.initUI()

    def about(self):
        self.about_window.show()

    def terminate(self):
        print('Нажат крестик')
        sys.exit()

    def initUI(self):
        print('Открыто Приложение')  # Для отладки


if __name__ == '__main__':
    app = QApplication(sys.argv)
    opn = OpenWindow()
    opn.show()
    sys.exit(app.exec())
