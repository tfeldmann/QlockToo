from PySide.QtCore import QTimer
from serialconnection import SerialConnection

import serial


class Hardware(object):

    """
    Hardware

    Wrapper class for the actual QlockToo device.
    Commands are send via a serial connection.
    """

    def __init__(self, port, baudrate=57600):
        self.width = 11
        self.height = 10
        self.callback = None

        self._serial = SerialConnection()
        self._serial.connect(port=port, baudrate=baudrate)

        self._timer = QTimer()
        self._timer.timeout.connect(self._serialRead)
        self._timer.start(50)

    def send(self, message):
        self._serial.send(message)

    def setMatrix(self, matrix):
        print "not yet implemented"

    def setCorners(self, corners):
        print "not yet implemented"

    def close(self):
        self._serial.stop()
        self.callback = None

    def _serialRead(self):
        " Reads incoming serial data from a queue "
        message_queue = self._serial.queue
        while not message_queue.empty():
            message = message_queue.get_nowait()
            if self.callback:
                self.callback(message)
            message_queue.task_done()
