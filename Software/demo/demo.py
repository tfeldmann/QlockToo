# -*- coding: utf-8 -*-
"""
Demo App

Various demos to show off the QlockToo
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
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.ui.black.clicked.connect(self.black)
        self.ui.white.clicked.connect(self.white)
        self.ui.pulse.clicked.connect(self.pulse)
        self.ui.fade.clicked.connect(self.fade)
        self.ui.wave.clicked.connect(self.wave)
        self.ui.pong.clicked.connect(self.pong)
        self.ui.helix.clicked.connect(self.helix)
        self.exec_()

    def black(self):
        self.demo = None
        self.device.setMatrix([[0]*11]*10)
        self.device.setCorners([0]*4)

    def white(self):
        self.demo = None
        self.device.setMatrix([[1]*11]*10)
        self.device.setCorners([1]*4)

    def pulse(self):
        self.demo = PulseDemo(self.device)

    def fade(self):
        self.demo = FadeDemo(self.device)

    def wave(self):
        self.demo = WaveDemo(self.device)

    def pong(self):
        self.demo = PongDemo(self.device)

    def helix(self):
        self.demo = HelixDemo(self.device)


class Demo(object):
    def __init__(self, device, framerate):
        self.device = device
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(framerate)

    def update(self):
        pass


class PulseDemo(Demo):
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
        self.device.setCorners([1-self.b]*4)


class FadeDemo(Demo):
    def __init__(self, device, framerate=50):
        Demo.__init__(self, device, framerate)
        self.device.setCorners([0]*4)
        self.matrix = [[0]*11]*10
        self.b = 0

    def update(self):
        self.b += 0.1
        self.matrix = [[abs(0.5*math.sin(self.b)-x*0.1 + 0.5) for x in range(11)]]*10
        self.device.setMatrix(self.matrix)


class WaveDemo(Demo):
    def __init__(self, device, framerate=30):
        Demo.__init__(self, device, framerate)
        self.device.setCorners([0]*4)
        self.t = 0

    def update(self):
        def f(x, y, t):
            px = self.device.width / 2 + 1.7 * math.sin(0.1 * t)
            py = self.device.height / 2 + 1.7 * math.cos(0.1 * t)
            buckling = 1.3
            result = math.sin(buckling * ((x-px)**2 + (y-py)**2)**0.5 - t)
            return result * 0.5 + 0.5  # scale result to 0 < values < 1

        self.t += 0.2
        matrix = [[f(x, y, self.t) for x in xrange(11)] for y in xrange(10)]
        self.device.setMatrix(matrix)


class PongDemo(Demo):
    def __init__(self, device, framerate=70):
        Demo.__init__(self, device, framerate)
        self.device.setCorners([0]*4)

        self.x, self.y = device.width / 2, device.height / 2
        self.dx, self.dy = 1, 1
        self.paddles = [device.height / 2, device.height / 2]

    def update(self):
        self._moveBall()
        self._movePaddles()
        self._draw()

    def _moveBall(self):
        self.x += self.dx
        self.y += self.dy
        if self.x == self.device.width - 1:
            self.dx = -1
        elif self.x == 0:
            self.dx = 1

        if self.y == self.device.height - 1:
            self.dy = -1
        elif self.y == 0:
            self.dy = 1

    def _movePaddles(self):
        if self.dx > 0:
            self.paddles[1] = self.y
        else:
            self.paddles[0] = self.y

    def _draw(self):
        self.matrix = [[0]*11 for _ in range(10)]
        # paddles
        self.matrix[self.paddles[0]][0] = 1
        self.matrix[self.paddles[1]][self.device.width-1] = 1
        # ball
        self.matrix[self.y][self.x] = 1.0
        self.device.setMatrix(self.matrix)


class HelixDemo(Demo):
    def __init__(self, device, framerate=50):
        Demo.__init__(self, device, framerate)
        self.device.setCorners([0]*4)
        self.t = 0

    def update(self):
        def f(x, y, t):
            px = self.device.width / 2
            py = self.device.height / 2
            buckling = 1.3
            result = math.sin(buckling * ((x-px)**2 + (y-py)**2)**0.5 - t)
            return result * 0.5 + 0.5  # scale result to 0 < values < 1

        self.t += 0.25
        matrix = [[f(x, y, self.t) for x in xrange(11)] for y in xrange(10)]
        self.device.setMatrix(matrix)


if __name__ == "__main__":
    # test environment in simulator
    import sys
    sys.path.append("..")
    from simulator import Simulator
    application = QApplication(sys.argv)
    device = Simulator()
    DemoApp(device)
    application.exec_()

