# -*- coding: utf-8 -*-
"""
QlockToo Simulator
"""

import sys, random
from PySide.QtGui import QApplication, QWidget, QPainter, QColor, QFont
from PySide.QtCore import Qt

class Simulator(QWidget):
    def __init__(self):
        super(Simulator, self).__init__()
        self.matrix = [[1]*11]*10
        # why must the umlaute be unicode?!?
        self.letters = [
            ['E', 'S', 'K', 'I', 'S', 'T', 'A', 'F', u'Ü', 'N', 'F'],
            ['Z', 'E', 'H', 'N', 'Z', 'W', 'A', 'N', 'Z', 'I', 'G'],
            ['D', 'R', 'E', 'I', 'V', 'I', 'E', 'R', 'T', 'E', 'L'],
            ['V', 'O', 'R', 'F', 'U', 'N', 'K', 'N', 'A', 'C', 'H'],
            ['H', 'A', 'L', 'B', 'A', 'E', 'L', 'F', u'Ü', 'N', 'F'],
            ['E', 'I', 'N', 'S', 'X', u'Ä', 'M', 'Z', 'W', 'E', 'I'],
            ['D', 'R', 'E', 'I', 'A', 'U', 'J', 'V', 'I', 'E', 'R'],
            ['S', 'E', 'C', 'H', 'S', 'N', 'L', 'A', 'C', 'H', 'T'],
            ['S', 'I', 'E', 'B', 'E', 'N', 'Z', 'W', u'Ö', 'L', 'F'],
            ['Z', 'E', 'H', 'N', 'E', 'U', 'N', 'K', 'U', 'H', 'R']]
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 330, 300)
        self.setWindowTitle('Simulator')
        self.show()

    def setMatrix(self, m):
        self.matrix = m
        self.update()
        if not self.isVisible():
            self.show()

    def paintEvent(self, e):
        size = self.size()
        letter_width = size.width() / 11
        letter_height = size.height() / 10

        qp = QPainter()
        qp.begin(self)
        qp.fillRect(0, 0, size.width(), size.height(), Qt.black)
        qp.setFont(QFont('Helvetica', letter_width*0.5))
        for y, row in enumerate(self.matrix):
            for x, cell in enumerate(row):
                brightness = 255 * cell
                qp.setPen(QColor(*[brightness]*3))
                qp.drawText(x*letter_width, y*letter_height,
                    letter_width, letter_height,
                    Qt.AlignCenter, self.letters[y][x])
        qp.end()


def main():
    app = QApplication(sys.argv)
    ex = Simulator()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
