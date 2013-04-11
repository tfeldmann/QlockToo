# -*- coding: utf-8 -*-
"""
Marquee App

Shows scrolling texts on the QlockTwo. You can modify the animation's
direction, speed and style.
"""

from PySide.QtGui import *
from PySide.QtCore import *
from ui_marquee import Ui_marquee as Ui

class MarqueeApp(QDialog):
    def __init__(self, device):
        super(MarqueeApp, self).__init__()
        self.device = device
        self.ui = Ui()
        self.ui.setupUi(self)
        self.exec_()
