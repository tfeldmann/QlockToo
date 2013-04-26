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
        self.width = 11
        self.height = 10
        self.callback = None

        self._matrix = [[1]*self.width]*self.height
        self._corners = [1]*4
        # why must the german umlaute be unicode?!?
        self._letters = [
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
        self._initUI()

    def _initUI(self):
        self.setGeometry(120, 200, 330, 300)
        self.setWindowTitle('Simulator')
        self.show()

    def setMatrix(self, matrix):
        self._matrix = matrix
        self._update()

    def setCorners(self, corners):
        self._corners = corners
        self._update()

    def send(self, message):
        if self.callback:
            self.callback('!Serial communication is not available in simulator')

    def close(self):
        self.callback = None

    def _update(self):
        if not self.isVisible():
            self.show()
        super(Simulator, self).update()

    def paintEvent(self, e):
        " The widget paints itself when self.update is called "
        size = self.size()
        ratio = 0.75
        letter_width = size.width()*ratio / 11
        letter_height = size.height()*ratio / 10

        qp = QPainter()
        qp.begin(self)
        qp.fillRect(0, 0, size.width(), size.height(), Qt.black)

        # letters
        qp.setFont(QFont('Helvetica', letter_width*0.5))
        for y, row in enumerate(self._matrix):
            for x, cell in enumerate(row):
                color = QColor(*[255 * cell] * 3)
                qp.setPen(color)
                qp.drawText(
                    size.width()*(1-ratio)/2 + x*letter_width,
                    size.height()*(1-ratio)/2 + y*letter_height,
                    letter_width, letter_height,
                    Qt.AlignCenter,
                    self._letters[y][x])

        # corners
        colors = [QColor(*[255 * b]*3) for b in self._corners]
        pos_top = (1 - ratio) * size.height() / 4
        pos_left = (1 - ratio) * size.width() / 4
        pos_bottom = size.height() - pos_top
        pos_right = size.width() - pos_left
        qp.fillRect(pos_left, pos_top, 2, 2, colors[0])
        qp.fillRect(pos_right, pos_top, 2, 2, colors[1])
        qp.fillRect(pos_left, pos_bottom, 2, 2, colors[2])
        qp.fillRect(pos_right, pos_bottom, 2, 2, colors[3])
        qp.end()


def main():
    app = QApplication(sys.argv)
    ex = Simulator()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
