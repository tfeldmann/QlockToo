# -*- coding: utf-8 -*-

from PySide.QtGui import *
from PySide.QtCore import *
from marquee_ui import Ui_marquee as Ui
import font

class MarqueeMatrix(object):
    def __init__(self, font):
        self.matrix = []
        self.font = font

    def setText(self, text):
        # font settings
        font = self.font
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

        self.matrix = matrix

    def regionFromLetter(self, letter):
        return self.regionFromPosition(
            (letter - 1) * (font.default['letter_width'] + 1))

    def regionFromPosition(self, x):
        if -11 < x < 0:
            # area before text
            extract = [line[0:x+11] for line in self.matrix]
            result = [[0]*abs(x) + line for line in extract]
        elif x < -11:
            # screen is completely empty
            result = [[0]*11 for _ in range(10)]
        else:
            # middle or end of marquee
            extract = [line[x:x+11] for line in self.matrix]
            result = [line + [0]*(11 - len(line)) for line in extract]
        return result

    @property
    def width(self):
        return len(self.matrix[0])

    @property
    def height(self):
        return len(self.matrix)


class MarqueeApp(QDialog):
    """ Marquee App

    Shows scrolling texts on the QlockToo. You can modify the animation's
    direction, speed and style.
    """
    def __init__(self, device):
        super(MarqueeApp, self).__init__()
        self.device = device
        self.ui = Ui()
        self.ui.setupUi(self)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.ui.text.cursorPositionChanged.connect(self.cursorPositionChanged)
        self.ui.play.stateChanged.connect(self.playToggled)
        self.ui.speed.valueChanged.connect(self.speedChanged)

        # create the update timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.move)

        # marquee
        self.marquee = MarqueeMatrix(font.default)
        self.startposition = - self.device.width
        self.speed = 50  # this is the initial dial position

        # init device with a black screen
        self.device.setMatrix([[0]*11]*10)
        self.device.setCorners([0]*4)

        self.exec_()

    def cursorPositionChanged(self, old, new):
        " Shows the chars around the current cursor position on the device."
        text = self.ui.text.text()
        self.marquee.setText(text)
        self.device.setMatrix(self.marquee.regionFromLetter(new))

    def _frequency(self, speed):
        """" Calculates the step frequency for the marquee from a given speed

        0 <= speed <= 100
        200 >= frequency >= 30
        """
        return 200 - 170 * abs(speed / 100.0)

    def playToggled(self, state):
        if state == Qt.Checked:
            text = self.ui.text.text()
            self.x = self.startposition
            self.timer.start(self._frequency(self.speed))
        else:
            self.timer.stop()

    def speedChanged(self):
        " Gets called from the speed dial and sets the new speed. "
        self.speed = self.ui.speed.value()
        if self.ui.play.isChecked():
            self.timer.start(self._frequency(self.speed))

    def move(self):
        " Moves the marquee one step and shows in on the device. "
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
        self.device.setMatrix(self.marquee.regionFromPosition(self.x))


if __name__ == "__main__":
    # test environment in simulator
    import sys
    sys.path.append("..")
    from simulator import Simulator
    application = QApplication(sys.argv)
    device = Simulator()
    MarqueeApp(device)
    application.exec_()

