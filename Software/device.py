# -*- coding: utf-8 -*-
"""
Device
"""

from serialconnection import SerialConnection

class Device(object):
    def __init__(self, port, baudrate):
        self.width = 11
        self.height = 10
        self.matrix = [[1]*self.width]*self.height
        self.corners = [1]*4

        self.serial = SerialConnection()
        self.serial.connect(port=port, baudrate=baudrate)

    def setMatrix(self, matrix):
        print "not yet implemented"

    def setCorners(self, corners):
        print "not yet implemented"

    def serialRead(self):
        " Reads incoming serial data from a queue "
        message_queue = self.serial.queue
        while not message_queue.empty():
            message = message_queue.get_nowait()
            if self.app:
                self.app.incoming_serial(message)
            message_queue.task_done()
