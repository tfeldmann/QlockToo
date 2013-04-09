# -*- coding: utf-8 -*-
"""
QlockTwo Simulator
"""

import sys, random
from PySide.QtGui import QApplication, QWidget, QPainter, QColor
from PySide.QtCore import Qt

class Simulator(QWidget):
    def __init__(self):
        super(Simulator, self).__init__()
        self.matrix = [[0]*11]*10
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 330, 300)
        self.setWindowTitle('Simulator')
        self.show()

    def setMatrix(self, m):
        self.matrix = m
        self.update()

    def paintEvent(self, e):
        size = self.size()
        letter_width = size.width() / 11
        letter_height = size.height() / 10

        qp = QPainter()
        qp.begin(self)
        qp.setPen(Qt.red)
        for y, row in enumerate(self.matrix):
            for x, cell in enumerate(row):
                brightness = 255 * cell
                qp.fillRect(x*letter_width, y*letter_height,
                    letter_width, letter_height, QColor(*[brightness]*3))
        qp.end()


def main():
    app = QApplication(sys.argv)
    ex = Simulator()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
