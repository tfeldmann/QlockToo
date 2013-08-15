# -*- coding: utf-8 -*-

from PySide.QtGui import QDialog
from PySide.QtCore import Slot, QTimer
from demo_ui import Ui_demoapp as Ui
import math


class DemoApp(QDialog):
    """
    Features various graphical demos to show off the QlockToo
    """
    def __init__(self, device):
        QDialog.__init__(self)
        self.device = device
        self.demo = None
        self.ui = Ui()
        self.ui.setupUi(self)

    @Slot()
    def on_black_clicked(self):
        self.demo = None
        self.device.matrix = [[0]*11]*10
        self.device.corners = [0]*4

    @Slot()
    def on_white_clicked(self):
        self.demo = None
        self.device.matrix = [[1]*11]*10
        self.device.corners = [1]*4

    @Slot()
    def on_pulse_clicked(self):
        self.demo = PulseDemo(self.device)

    @Slot()
    def on_fade_clicked(self):
        self.demo = FadeDemo(self.device)

    @Slot()
    def on_wave_clicked(self):
        self.demo = WaveDemo(self.device)

    @Slot()
    def on_pong_clicked(self):
        self.demo = PongDemo(self.device)

    @Slot()
    def on_helix_clicked(self):
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
        self.device.matrix = [[self.b]*11]*10
        self.device.corners = [1-self.b]*4


class FadeDemo(Demo):
    def __init__(self, device, framerate=50):
        Demo.__init__(self, device, framerate)
        self.device.corners = [0]*4
        self.matrix = [[0]*11]*10
        self.b = 0

    def update(self):
        self.b += 0.1
        self.matrix = [[abs(0.5*math.sin(self.b)-x*0.1 + 0.5) for x in range(11)]]*10
        self.device.matrix = self.matrix


class WaveDemo(Demo):
    def __init__(self, device, framerate=30):
        Demo.__init__(self, device, framerate)
        self.device.corners = [0]*4
        self.t = 0

    def update(self):
        def f(x, y, t):
            px = self.device.columns / 2 + 1.7 * math.sin(0.1 * t)
            py = self.device.rows / 2 + 1.7 * math.cos(0.1 * t)
            buckling = 1.3
            result = math.sin(buckling * ((x-px)**2 + (y-py)**2)**0.5 - t)
            return result * 0.5 + 0.5  # scale result to 0 < values < 1

        self.t += 0.2
        matrix = [[f(x, y, self.t) for x in xrange(11)] for y in xrange(10)]
        self.device.matrix = matrix


class PongDemo(Demo):
    def __init__(self, device, framerate=70):
        Demo.__init__(self, device, framerate)
        self.device.corners = [0]*4

        self.x, self.y = device.columns / 2, device.rows / 2
        self.dx, self.dy = 1, 1
        self.paddles = [device.rows / 2, device.rows / 2]

    def update(self):
        self.moveBall()
        self.movePaddles()
        self.draw()

    def moveBall(self):
        self.x += self.dx
        self.y += self.dy
        if self.x == self.device.columns - 1:
            self.dx = -1
        elif self.x == 0:
            self.dx = 1

        if self.y == self.device.rows - 1:
            self.dy = -1
        elif self.y == 0:
            self.dy = 1

    def movePaddles(self):
        if self.dx > 0:
            self.paddles[1] = self.y
        else:
            self.paddles[0] = self.y

    def draw(self):
        self.matrix = [[0]*11 for _ in range(10)]

        self.drawPaddles()

        # ball
        self.matrix[self.y][self.x] = 1.0
        self.device.matrix = self.matrix

    def drawPaddles(self):
        self.matrix[self.paddles[0]][0] = 1
        self.matrix[self.paddles[1]][self.device.columns-1] = 1


class HelixDemo(Demo):
    def __init__(self, device, framerate=100):
        Demo.__init__(self, device, framerate)
        self.device.corners = [0]*4
        self.matrix = [[0]*11 for _ in range(10)]
        self.matrix[0] = [1]*11
        self.t = 0

    def update(self):
        def helix(x, t):
            k = 0.6
            y = math.sin(k * x - t)
            brightness = math.cos(k * x - t) * 0.3 + 0.7
            return [self.device.columns * (y*0.5+0.5), brightness]

        self.t += 0.2
        self.matrix = [[0]*11 for _ in range(10)]
        # helix 1
        for x, line in enumerate(self.matrix):
            for r in range(-2, 2):
                pos, brightness = helix(x, self.t + r / 10.0)
                line[int(pos)] = brightness

        self.device.matrix = self.matrix