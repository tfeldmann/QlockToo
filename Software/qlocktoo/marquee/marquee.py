# -*- coding: utf-8 -*-
from PySide.QtGui import QDialog
from PySide.QtCore import Qt, QTimer, Slot
from .fixed_width import font as Font
from .marquee_ui import Ui_marquee as Ui


class MarqueeMatrix(object):

    def __init__(self, font):
        self.matrix = []
        self.font = Font

    def setText(self, text):
        # font settings
        letter_width = self.font['letter_width']
        # letter_height = self.font['letter_height']  # not needed here
        spacing = 1

        # build a empty 2d-array of desired size
        height = 10  # display height
        length = (spacing + letter_width) * len(text)
        # see http://stackoverflow.com/q/15956969/300783
        # we cannot use [[0]*length]*height here
        matrix = [[0] * length for _ in range(height)]

        # print letters
        for _x, _c in enumerate(text):
            c = self.font[_c]
            x = _x * (letter_width + spacing)
            for y, line in enumerate(c):
                matrix[y][x:x + letter_width] = line

        self.matrix = matrix

    def regionFromLetter(self, letter):
        return self.regionFromPosition(
            (letter - 1) * (self.font['letter_width'] + 1))

    def regionFromPosition(self, x):
        if -11 < x < 0:
            # area before text
            extract = [line[0:x + 11] for line in self.matrix]
            result = [[0] * abs(x) + line for line in extract]
        elif x < -11:
            # screen is completely empty
            result = [[0] * 11 for _ in range(10)]
        else:
            # middle or end of marquee
            extract = [line[x:x + 11] for line in self.matrix]
            result = [line + [0] * (11 - len(line)) for line in extract]
        return result

    @property
    def width(self):
        return len(self.matrix[0])

    @property
    def height(self):
        return len(self.matrix)


class MarqueeApp(QDialog):

    """
    Marquee App

    Shows scrolling texts on the QlockToo. You can modify the animation's
    direction, speed and style.
    """

    def __init__(self, device=None, simulator=None):
        super(MarqueeApp, self).__init__()
        self.ui = Ui()
        self.ui.setupUi(self)

        self.device = device
        self.simulator = simulator

        self.ui.text.cursorPositionChanged.connect(self.cursorPositionChanged)

        # create the update timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.move)

        # marquee
        self.marquee = MarqueeMatrix(self.font)
        self.startposition = - self.simulator.columns
        self.speed = 50  # this is the initial dial position

        # init device with a black screen
        self.simulator.matrix = [[0] * 11] * 10
        self.simulator.corners = [0] * 4

    def cursorPositionChanged(self, old, new):
        """
        Shows the chars around the current cursor position on the device.
        """
        text = self.ui.text.text()
        self.marquee.setText(text)
        if len(text) > 0:
            self.simulator.matrix = self.marquee.regionFromLetter(new)

    def _frequency(self, speed):
        """
        Calculates the step frequency for the marquee from a given speed

        0 <= speed <= 100
        200 >= frequency >= 30
        """
        return 200 - 170 * abs(speed / 100.0)

    @Slot()
    def on_play_stateChanged(self):
        if self.ui.play.isChecked():
            self.x = self.startposition
            self.timer.start(self._frequency(self.speed))
        else:
            self.timer.stop()

    @Slot()
    def on_speed_valueChanged(self):
        """
        Gets called from the speed dial and sets the new speed.
        """
        self.speed = self.ui.speed.value()
        if self.ui.play.isChecked():
            self.timer.start(self._frequency(self.speed))

    def move(self):
        """
        Moves the marquee one step and shows in on the device.
        """
        # move forwards
        if self.speed >= 0:
            self.x += 1
            if self.x > self.marquee.width:
                self.x = self.startposition
        else:
        # move backwards
            self.x -= 1
            if self.x < self.startposition:
                self.x = self.marquee.width
        self.simulator.matrix = self.marquee.regionFromPosition(self.x)
