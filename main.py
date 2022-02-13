import Enter_sign as input_sign
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint,
                            QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                           QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from PyQt5.QtCore import QSize, Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter, QColor, QPixmap
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QInputDialog, QLabel
from PyQt5.QtWidgets import QCheckBox, QLineEdit, QVBoxLayout
from PyQt5.QtWidgets import (QGraphicsDropShadowEffect, QGridLayout, QSpacerItem,
                             QSizePolicy)
import datetime
import sqlite3
import PySide2
import sys
import os
import random

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

coords = None



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
        self.setStyleSheet("border-radius: 30px; background-color: qlineargradient(spread:pad, x1:0, y1:0,\
         x2:1, y2:1, stop:0 rgba(41, 37, 54, 255), stop:1 rgba(39, 37, 55, 255));")
        self.layout().addWidget(self.info)


class OpenWindow(QMainWindow):
    def __init__(self):
        super(OpenWindow, self).__init__()
        uic.loadUi('Main1.ui', self)
        self.about_window = AboutWindow()
        self.action_button.clicked.connect(self.about)
        self.close_wnd.clicked.connect(self.terminate)
        self.reg_btn.clicked.connect(self.registr)
        self.min_wnd.clicked.connect(self.set_min)
        self.to_sign.clicked.connect(self.run_add_sign)
        self.confirm_btn.clicked.connect(self.confirm_input)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setStyleSheet("border-radius: 20px; background: rgba(0, 0, 0, 0);")
        self.drop_shadow_frame.setStyleSheet("background-color: qlineargradient(spread:pad, \
            x1:0, y1:0, x2:1, y2:1, stop:0 rgba(41, 37, 54, 255), stop:1 rgba(39, 37, 55, 255));\
                                             border-radius: 30px")
        effect = QGraphicsDropShadowEffect(self)
        effect.setBlurRadius(100)
        effect.setOffset(0, 1)
        effect.setColor(Qt.black)
        self.drop_shadow_frame.setGraphicsEffect(effect)
        self.reg = None
        self.sign_main= None

    def about(self):
        self.about_window.show()

    def terminate(self):
        print('Нажат крестик')
        sys.exit()

    def initUI(self):
        print('Открыто Приложение')  # Для отладки

    def set_min(self):
        self.showMinimized()

    def registr(self):
        if not self.reg:
            self.reg = Registration()
        self.reg.show()
        self.hide()
        print("Открыто окно регистрации")

    def confirm_input(self):
        pass

    def run_add_sign(self):
        if not self.sign_main:
            self.sign_main = input_sign.Canvas()
        self.sign_main.show()

class Registration(QWidget):
    def __init__(self):
        super(Registration, self).__init__()
        uic.loadUi('Reg.ui', self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.back_button.clicked.connect(self.back_btn)
        self.initUI()

    def initUI(self):
        effect = QGraphicsDropShadowEffect(self)
        effect.setBlurRadius(50)
        effect.setOffset(0, 2)
        effect.setColor(Qt.black)
        self.frame.setGraphicsEffect(effect)
        self.setStyleSheet("border-radius: 20px; background: rgba(0, 0, 0, 0);")
        self.close_wnd.clicked.connect(self.terminate)
        self.min_wnd.clicked.connect(self.set_min)

    def back_btn(self):
        self.opn_wnd1 = OpenWindow()
        self.opn_wnd1.show()
        self.hide()

    def terminate(self):
        print('Нажат крестик')
        sys.exit()

    def set_min(self):
        self.showMinimized()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    opn = OpenWindow()
    opn.show()
    sys.exit(app.exec())
