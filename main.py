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
import datetime


class AboutWindow(QWidget):  # Menubar
    def __init__(self):
        super(AboutWindow, self).__init__()
        self.setLayout(QVBoxLayout(self))
        self.info = QLabel(self)
        self.info.setText('Github profiles: Nikdevelop and jur4ikoff')  # о создателях
        self.layout().addWidget(self.info)


class AboutWindow_1(QWidget):  # Menubar
    def __init__(self):
        super(AboutWindow_1, self).__init__()
        self.setLayout(QVBoxLayout(self))
        self.info1 = QLabel(self)
        self.info1.setText('Проект для МИРЭА')  # о создателях
        self.layout().addWidget(self.info1)


class OpenWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.initUI()
        self.about_window = AboutWindow()
        self.about_action.triggered.connect(self.about)
        self.about_action_2.triggered.connect(self.about_1)

    def about(self):
        print('hello nahuy')
        self.about_window.show()

    def about_1(self):
        self.about_window_1.show()
        print('hello1')

    def initUI(self):
        print('Открыто Приложение')  # Для отладки


if __name__ == '__main__':
    app = QApplication(sys.argv)
    opn = OpenWindow()
    opn.show()
    sys.exit(app.exec())
