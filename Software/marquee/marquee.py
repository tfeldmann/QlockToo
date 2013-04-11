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
        # self.ui.text.textChanged.connect(self.textChanged)
        self.ui.text.returnPressed.connect(self.returnPressed)
        self.ui.text.cursorPositionChanged.connect(self.cursorPositionChanged)

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
        x = (new - 1) * 6
        marquee = self.renderText(text=self.ui.text.text(), font=self.font)
        extract = self.matrixExtract(marquee, x)
        self.device.setMatrix(extract)

    def textChanged(self, text):
        x = (self.ui.text.cursorPosition() - 1) * 6
        marquee = self.renderText(text=text, font=self.font)
        extract = self.matrixExtract(marquee, x)
        self.device.setMatrix(extract)

    def returnPressed(self):
        text = self.ui.text.text()
        self.marquee = self.marqueeMatrix(text)
        self.showMarquee()

    def renderText(self, text, font):
        " Returns a matrix representation of the rendered text "

        # gather data
        letter_height = font['letter_height']
        letter_width = font['letter_width']
        spacing = 1
        offset = 1

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
                matrix[y+offset][x:x+letter_width] = line
        return matrix

    def matrixExtract(self, matrix, x=0):
        if x < 0:
            x = 0
        extract = [line[x:x+11] for line in matrix]
        result = [line + [0]*(11 - len(line)) for line in extract]
        return result
