# -*- coding: utf-8 -*-
from PySide.QtGui import QDialog, QMessageBox
from PySide.QtCore import Qt, QTimer, Slot
from snake_ui import Ui_snake as Ui
from snake_model import SnakeModel


class SnakeApp(QDialog):
    def __init__(self, device):
        super(SnakeApp, self).__init__()
        self.device = device
        self.ui = Ui()
        self.ui.setupUi(self)

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
        self.device.matrix = welcomeScreen
        self.device.corners = [0]*4
        self.stepFrequency = 5

        # init the game model
        self.snake = SnakeModel(
            width=self.device.columns,
            height=self.device.rows,
            gameOverCallback=self.gameOver,
            ateFoodCallback=self.ateFood)
        self.highscore = 0
        self.pause = False

        # create the timer
        self.stepTimer = QTimer()
        self.stepTimer.timeout.connect(self.step)

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
        self.device.matrix = matrix

    def _set_matrix_element(self, matrix, x, y, value):
        if 0 <= y < len(matrix) and 0 <= x < len(matrix[0]):
            matrix[y][x] = value

    def _empty_matrix(self):
        return [[0.1]*self.device.columns for _ in range(self.device.rows)]

    def reject(self):
        # this fixes a bug where the snake app would not be
        # correctly deleted by gc and keep running. We have to delete the
        # snake instance.
        self.stepTimer = None
        self.snake = None
        self.accept()
