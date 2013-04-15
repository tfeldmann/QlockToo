# -*- coding: utf-8 -*-

from PySide.QtGui import *
from PySide.QtCore import *
from ui_snake import Ui_snake as Ui


class Snake(object):
    def __init__(self, x=0, y=0):
        self.head = [x, y]
        self.tail = []

    def move(self, dx, dy):
        x, y = self.head
        self.head = [x+dx, y+dy]

    def addElement(self):
        pass


class SnakeApp(QDialog):
    def __init__(self, device):
        super(SnakeApp, self).__init__()
        self.device = device
        self.ui = Ui()
        self.ui.setupUi(self)

        # create the update timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.move)

        # init device with welcome screen
        welcomeScreen = [
            [0.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.0],
            [0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.0],
            [0.0, 0.5, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.5, 0.0],
            [0.0, 0.5, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.0],
            [0.0, 0.5, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.5, 0.0],
            [0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.5, 0.0],
            [0.0, 0.5, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.5, 0.0],
            [0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.0],
            [0.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        ]
        self.device.setMatrix(welcomeScreen)
        self.device.setCorners([0]*4)

        # snake start position
        self.snake = Snake(4, 4)
        self.dir = [1, 0]

        self.timer.start(1000)
        self.exec_()

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Return:
            print "Pressed Return"
        if key == Qt.Key_Left:
            self.dir = [-1, 0]
        elif key == Qt.Key_Right:
            self.dir = [1, 0]
        elif key == Qt.Key_Down:
            self.dir = [0, 1]
        elif key == Qt.Key_Up:
            self.dir = [0, -1]
        elif key == Qt.Key_Space:
            self.dropDown()
        else:
            QDialog.keyPressEvent(self, event)

    def move(self):
        self.timer.start(100)
        self.snake.move(self.dir[0], self.dir[1])

        m = [[0]*11 for _ in range(10)]
        m[self.snake.head[1]][self.snake.head[0]] = 1
        self.device.setMatrix(m)


if __name__ == "__main__":
    import sys
    sys.path.append("..")
    from simulator import Simulator
    application = QApplication(sys.argv)
    device = Simulator()
    SnakeApp(device)
    application.exec_()
