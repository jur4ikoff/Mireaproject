import sys
import main as Main
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt

WIDTH, HEIGHT = 880, 560


class Canvas(QtWidgets.QLabel):
    signal = QtCore.pyqtSignal(list)

    def __init__(self):
        self.coords = []
        for i in range(HEIGHT):
            self.coords.append([0] * WIDTH)

        super().__init__()
        pixmap = QtGui.QPixmap(WIDTH, HEIGHT)
        self.setPixmap(pixmap)

        self.last_x, self.last_y = None, None
        self.pen_color = QtGui.QColor('#FFFFFF')

    def set_pen_color(self, c):
        self.pen_color = QtGui.QColor(c)

    def mouseMoveEvent(self, e):
        if self.last_x is None:  # First event.
            self.last_x = e.x()
            self.last_y = e.y()
            return  # Ignore the first time.

        painter = QtGui.QPainter(self.pixmap())
        p = painter.pen()
        p.setWidth(4)
        p.setColor(self.pen_color)
        painter.setPen(p)
        painter.drawLine(self.last_x, self.last_y, e.x(), e.y())
        painter.end()
        self.update()

        # Update the origin for next time.
        self.last_x = e.x()
        self.last_y = e.y()
        try:
            self.coords[e.y()][e.x()] = 255
        except IndexError:
            pass

    def mouseReleaseEvent(self, e):
        self.last_x = None
        self.last_y = None

    QtCore.pyqtSlot()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        sign = self.coords
        self.signal.emit(sign)
        return super().closeEvent(a0)
