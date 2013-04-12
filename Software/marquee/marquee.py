# -*- coding: utf-8 -*-
"""
Marquee App

Shows scrolling texts on the QlockToo. You can modify the animation's
direction, speed and style.
"""

from PySide.QtGui import *
from PySide.QtCore import *
from ui_marquee import Ui_marquee as Ui
import json


class MarqueeApp(QDialog):
    def __init__(self, device):
        super(MarqueeApp, self).__init__()
        self.device = device
        self.ui = Ui()
        self.ui.setupUi(self)
        self.ui.text.cursorPositionChanged.connect(self.cursorPositionChanged)
        self.ui.play.stateChanged.connect(self.playToggled)

        # update timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)

        # load default font
        self.font = self.loadFont('fonts/default.json')

        # show empty matrix
        self.device.setMatrix([[0]*11]*10)

        self.exec_()

    def loadFont(self, filepath):
        with open(filepath, 'rb') as fontfile:
            try:
                return json.loads(fontfile.read())
            except Exception, e:
                QMessageBox.warning(self, 'Error: ', e.message)

    def cursorPositionChanged(self, old, new):
        font = self.font
        self.x = (new - 1) * (font['letter_width'] + 1)
        self.marquee = self.renderText(text=self.ui.text.text(), font=font)
        extract = self.matrixExtract(self.marquee, self.x)
        self.device.setMatrix(extract)

    def playToggled(self, state):
        if state == Qt.Checked:
            text = self.ui.text.text()
            font = self.font
            self.x = 0
            self.marquee = self.renderText(text=text, font=font)
            self.timer.start(100)
        else:
            self.timer.stop()

    def update(self):
        self.x += 1
        if self.x > len(self.marquee[0]):
            self.x = -2 * (self.font['letter_width'] + 1)
        self.device.setMatrix(self.matrixExtract(self.marquee, self.x))

    def renderText(self, text, font):
        " Returns a matrix representation of the rendered text "

        # font settings
        letter_height = font['letter_height']
        letter_width = font['letter_width']
        spacing = 1

        # build a empty 2d-array of desired size
        height = 10  # display height
        length = (spacing + letter_width) * len(text)
        # see http://stackoverflow.com/q/15956969/300783
        # we cannot use [[0]*length]*height here
        matrix = [[0]*length for _ in range(height)]

        # print letters
        for _x, _c in enumerate(text):
            c = font[_c]
            x = _x * (letter_width + spacing)
            for y, line in enumerate(c):
                matrix[y][x:x+letter_width] = line
        return matrix

    def matrixExtract(self, matrix, x=0):
        if -11 < x < 0:
            # area before text
            extract = [line[0:x+11] for line in matrix]
            result = [[0]*abs(x) + line for line in extract]
        elif x < -11:
            # screen is completely empty
            result = [[0]*11 for _ in range(10)]
        else:
            # middle or end of marquee
            extract = [line[x:x+11] for line in matrix]
            result = [line + [0]*(11 - len(line)) for line in extract]
        return result
