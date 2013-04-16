# -*- coding: utf-8 -*-

from PySide.QtGui import *
from PySide.QtCore import *
from ui_snake import Ui_snake as Ui
from snake_model import SnakeModel


class SnakeApp(QDialog):
    def __init__(self, device):
        super(SnakeApp, self).__init__()
        self.device = device
        self.ui = Ui()
        self.ui.setupUi(self)
        self.setAttribute(Qt.WA_DeleteOnClose)

        # initial welcome screen
        welcomeScreen = [
            [0.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.0],
            [0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.0],
            [0.0, 0.5, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.5, 0.0],
            [0.0, 0.5, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.0],
            [0.0, 0.5, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.5, 0.0],
            [0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.5, 0.0],
            [0.0, 0.5, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.5, 0.0],
            [0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.0],
            [0.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.0],
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        ]
        self.device.setMatrix(welcomeScreen)
        self.device.setCorners([0]*4)
        self.stepFrequency = 5

        # init the game model
        self.snake = SnakeModel(
            width=self.device.width,
            height=self.device.height,
            gameOverCallback=self.gameOver,
            ateFoodCallback=self.ateFood)
        self.highscore = 0
        self.pause = False

        # create the timer
        self.stepTimer = QTimer()
        self.stepTimer.timeout.connect(self.step)
        self.exec_()

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Return or key == Qt.Key_Enter:
            self.snake.reset()
            self.stepTimer.start(1000 / self.stepFrequency)
        elif key == Qt.Key_Left:
            self.snake.setSnakeDirection(-1, 0)
        elif key == Qt.Key_Right:
            self.snake.setSnakeDirection(1, 0)
        elif key == Qt.Key_Down:
            self.snake.setSnakeDirection(0, 1)
        elif key == Qt.Key_Up:
            self.snake.setSnakeDirection(0, -1)
        else:
            QDialog.keyPressEvent(self, event)

    def gameOver(self, score):
        QMessageBox.warning(self, "Game Over",
            "Game Over.\nDeine Punktzahl: " + str(score))
        self.stepTimer.stop()

    def ateFood(self, score):
        self.ui.score.setText("Punkte: " + str(score))
        if score > self.highscore:
            self.highscore = score
            self.ui.highscore.setText("Highscore: " + str(self.highscore))

    def step(self):
        self.snake.step()
        self.draw()

    def draw(self):
        head = self.snake.head
        tail = self.snake.tail
        food = self.snake.food
        matrix = self._empty_matrix()

        # draw food
        self._set_matrix_element(matrix, *food, value=0.8)
        # draw snake
        for pos, element in enumerate(tail):
            self._set_matrix_element(matrix, *element,
                value=0.7 - 0.4 * pos / len(tail))
        self._set_matrix_element(matrix, *head, value=1)
        self.device.setMatrix(matrix)

    def _set_matrix_element(self, matrix, x, y, value):
        if 0 <= y < len(matrix) and 0 <= x < len(matrix[0]):
            matrix[y][x] = value

    def _empty_matrix(self):
        return [[0.1]*self.device.width for _ in range(self.device.height)]


if __name__ == "__main__":
    import sys
    sys.path.append("..")
    from simulator import Simulator
    application = QApplication(sys.argv)
    device = Simulator()
    SnakeApp(device)
    application.exec_()
