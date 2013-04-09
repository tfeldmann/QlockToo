# -*- coding: utf-8 -*-
"""
Console App

Send and read serial data from the clock
"""

from PySide.QtGui import *
from PySide.QtCore import *
from ui_demo import Ui_demoapp as Ui
import math

class DemoApp(QDialog):
    def __init__(self, device):
        super(DemoApp, self).__init__()
        self.device = device
        self.demo = None
        self.ui = Ui()
        self.ui.setupUi(self)
        self.ui.black.clicked.connect(self.black)
        self.ui.white.clicked.connect(self.white)
        self.ui.fade.clicked.connect(self.fade)
        self.ui.wave.clicked.connect(self.wave)
        self.exec_()

    def black(self):
        self.demo = None
        self.device.setMatrix([[0]*11]*10)

    def white(self):
        self.demo = None
        self.device.setMatrix([[1]*11]*10)

    def fade(self):
        self.demo = FadeDemo(self.device)

    def wave(self):
        self.demo = WaveDemo(self.device)


class Demo(object):
    def __init__(self, device, framerate):
        self.device = device
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(framerate)

    def update(self):
        pass


class FadeDemo(Demo):
    def __init__(self, device, framerate=50):
        Demo.__init__(self, device, framerate)
        self.b = 0
        self.inc = 0.05

    def update(self):
        self.b += self.inc
        if self.b > 1:
            self.b = 1
            self.inc *= -1
        elif self.b < 0:
            self.b = 0
            self.inc *= -1
        self.device.setMatrix([[self.b]*11]*10)


class WaveDemo(Demo):
    def __init__(self, device, framerate=50):
        Demo.__init__(self, device, framerate)
        self.matrix = [[0]*11]*10
        self.b = 0

    def update(self):
        self.b += 0.1
        self.matrix = [[abs(0.5*math.sin(self.b)-x*0.1 + 0.5) for x in range(11)]]*10
        self.device.setMatrix(self.matrix)


