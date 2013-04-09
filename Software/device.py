# -*- coding: utf-8 -*-
"""
Device
"""

from serialconnection import SerialConnection

class Device(object):
    def __init__(self, port, baudrate):
        self.matrix = [[0]*11]*10

        self.serial = SerialConnection()
        self.serial.connect(port=port, baudrate=baudrate)

    def setMatrix(self, m):
        print "not yet implemented"

    def serialRead(self):
        " Reads incoming serial data from a queue "
        message_queue = self.serial.queue
        while not message_queue.empty():
            message = message_queue.get_nowait()
            if self.app:
                self.app.incoming_serial(message)
            message_queue.task_done()
