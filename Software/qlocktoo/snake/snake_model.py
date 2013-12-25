import random


class SnakeModel(object):

    """
    Model for a snake-like game.
    """

    def __init__(self, width, height,
                 gameover_callback, atefood_callback):
        """
        Initializes the game

        gameover_callback and atefood_callback are callback functions. They
        are passed the current player score (length of the snake's tail) as an
        integer.
        """
        self.width = width
        self.height = height
        self.gameover_callback = gameover_callback
        self.atefood_callback = atefood_callback
        self.reset()

    def reset(self):
        """
        Starts a new game.

        Sets the starting position, length and direction of the snake as well
        as the position of the first food item.
        """
        self._dir = (0, -1)

        # You can read head, tail and food directly for drawing
        self.head = (self.width / 2, self.height - 2)
        self.tail = [(self.width / 2, self.height - 1)]
        self.food = (self.width / 2, self.height / 3)

    def step(self):
        """
        Advances the game one step
        """
        # check for collisions
        if self.head in self.tail:
            self.gameover_callback(len(self.tail))

        # eat food
        if self.head == self.food:
            self.tail.insert(0, self.head)
            self.food = self._new_food_location()
            self.atefood_callback(len(self.tail))

        # move snake
        self._move_snake()

    def set_snake_direction(self, dx, dy):
        """
        Sets the direction the snake will move on the next step
        """
        self._dir = (dx, dy)

    def _move_snake(self):
        """
        Moves the snake one step in the given direction.

        The snake can move through the game area's borders and comes out on the
        other side.
        """
        x, y = self.head
        dx, dy = self._dir
        newX = (x + dx) % self.width
        newY = (y + dy) % self.height
        self.head = (newX, newY)
        self.tail.insert(0, (x, y))
        self.tail.pop()

    def _new_food_location(self):
        """
        Returns a new possible food position which is not in the snake.
        """
        game_field = set([(x, y) for x in range(self.width)
                          for y in range(self.height)])
        possible = game_field - set(self.tail) - set([self.head])
        new_position = random.choice(list(possible))
        return new_position
