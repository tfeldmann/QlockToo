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
        self.loadFont('fonts/default.json')
        self.exec_()

    def loadFont(self, filepath):
        with open(filepath, 'rb') as fontfile:
            try:
                self.font = json.loads(fontfile.read())
            except Exception, e:
                QMessageBox.warning(self, 'Error: ', e.message)

    def marqueeMatrix(self, text):
        pass
