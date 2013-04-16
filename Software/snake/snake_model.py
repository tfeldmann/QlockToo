# -*- coding: utf-8 -*-
import random

class SnakeModel(object):
    " A simple snake game model "

    def __init__(self, width, height,
        gameOverCallback, ateFoodCallback):
        self._width = width
        self._height = height
        self._gameover = gameOverCallback
        self._ateFood = ateFoodCallback
        self.reset()

    def reset(self):
        self._dir = (0, -1)

        # You can access head, tail and food directly for drawing
        self.head = (self._width / 2, self._height - 2)
        self.tail = [(self._width / 2, self._height - 1)]
        self.food = (self._width / 2, self._height / 3)

    def step(self):
        # check for collisions
        if self.head in self.tail:
            self._gameover(len(self.tail))

        # eat food
        if self.head == self.food:
            self.tail.insert(0, self.head)
            self.food = self._newFoodLocation()
            self._ateFood(len(self.tail))

        # move snake
        self._moveSnake(*self._dir)

    def setSnakeDirection(self, dx, dy):
        self._dir = (dx, dy)

    def _moveSnake(self, dx, dy):
        x, y = self.head
        newX = (x + dx) % self._width
        newY = (y + dy) % self._height
        self.head = (newX, newY)
        self.tail.insert(0, (x, y))
        self.tail.pop()

    def _newFoodLocation(self):
        possible = set([(x, y) for x in range(self._width)
            for y in range(self._height)]) - set(self.tail) - set([self.head])
        return random.choice(list(possible))
