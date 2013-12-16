# coding: utf-8
from PySide.QtGui import QWidget, QPainter, QColor, QFont
from PySide.QtCore import Qt, Slot, Signal, QTimer, QEventLoop
from itertools import chain


class Device(QWidget):

    """
    QlockToo Simulator

    This widget shows the QlockToo front with letters and corner leds.
    """
    connection = None
    signal_linereceived = Signal(str)

    def __init__(self, parent):
        super(Device, self).__init__()

        frontpanel = u"""
            E S K I S T A F Ü N F
            Z E H N Z W A N Z I G
            D R E I V I E R T E L
            V O R F U N K N A C H
            H A L B A E L F Ü N F
            E I N S X Ä M Z W E I
            D R E I A U J V I E R
            S E C H S N L A C H T
            S I E B E N Z W Ö L F
            Z E H N E U N K U H R"""

        self.columns = 11
        self.rows = 10
        self.matrix = [[1] * self.columns] * self.rows
        self.corners = [1] * 4
        self.letters = [row.split() for row in frontpanel.split("\n") if row]

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.listen_serial)
        self._buffer = ''

        self.stop_sign = ''
        self.eventloop = QEventLoop()

    def use_connection(self, connection):
        self.connection = connection
        self.connection.timeout = 0
        self.timer.start(25)  # ms

    def disconnect(self):
        self.timer.stop()
        if self.connection:
            self.send('@disconnect')
            self.connection.close()
            self.connection = None

    def is_connected(self):
        return self.connection is not None

    def send(self, cmd):
        print('<-- %s' % cmd)
        self.connection.write('%s\n' % cmd)

    @Slot()
    def listen_serial(self):
        while self.connection.inWaiting() > 0 and self.is_connected():
            self._buffer += self.connection.read()
            if len(self._buffer) > 0 and self._buffer[-1] == '\n':
                line = self._buffer.strip()
                if len(line) > 0:
                    self.signal_linereceived.emit(line)
                    print('--> %s' % line)
                    self.eventloop.quit()
                self._buffer = ''

    def encode_brightness(self, brightness):
        """ only use chars that have to control function """
        return int(33 + 93 * brightness)

    @property
    def matrix(self):
        return self._matrix

    @matrix.setter
    def matrix(self, value):
        self._matrix = value
        self.update()

        if self.is_connected():
            flat_matrix = list(chain.from_iterable(self.matrix))
            data = [self.encode_brightness(elem) for elem in flat_matrix]
            self.connection.write('@m ')
            self.connection.write(bytearray(data))
            self.connection.write('\n')
            self.eventloop.exec_()

    @property
    def corners(self):
        return self._corners

    @corners.setter
    def corners(self, value):
        self._corners = value
        self.update()

        if self.is_connected():
            data = [self.encode_brightness(elem) for elem in self.corners]
            self.connection.write('@c ')
            self.connection.write(bytearray(data))
            self.connection.write('\n')

    def paintEvent(self, e):
        """
        QWidget paintEvent implementation

        This method is called on window resizes or when self.update() is
        called.
        """
        size = self.size()
        ratio = 0.75
        letter_width = size.width() * ratio / 11
        letter_height = size.height() * ratio / 10

        qp = QPainter()
        qp.begin(self)
        qp.fillRect(0, 0, size.width(), size.height(), Qt.black)

        # draw letters
        qp.setFont(QFont('Helvetica', letter_width * 0.5))
        for y, row in enumerate(self.matrix):
            for x, cell in enumerate(row):
                color = QColor(*[255 * cell] * 3)
                qp.setPen(color)
                qp.drawText(
                    size.width() * (1 - ratio) / 2 + x * letter_width,
                    size.height() * (1 - ratio) / 2 + y * letter_height,
                    letter_width, letter_height,
                    Qt.AlignCenter,
                    self.letters[y][x])

        # draw corners
        colors = [QColor(*[255 * b] * 3) for b in self.corners]
        pos_top = (1 - ratio) * size.height() / 4
        pos_left = (1 - ratio) * size.width() / 4
        pos_bottom = size.height() - pos_top
        pos_right = size.width() - pos_left
        qp.fillRect(pos_left, pos_top, 2, 2, colors[0])
        qp.fillRect(pos_right, pos_top, 2, 2, colors[1])
        qp.fillRect(pos_left, pos_bottom, 2, 2, colors[2])
        qp.fillRect(pos_right, pos_bottom, 2, 2, colors[3])
        qp.end()
