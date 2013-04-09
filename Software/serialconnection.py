# -*- coding: utf-8 -*-

import os
import serial
from serial.tools import list_ports
import thread
import Queue


class SerialConnection(object):
    """receives and sends serial data in a thread"""
    def __init__(self):
        self.queue = Queue.Queue()

    def connect(self, port, baudrate):
        self.connection = serial.Serial(port=port, baudrate=baudrate)
        thread.start_new_thread(self.update_serial, ())
        self._stop_serial_update_flag = False

    def stop(self):
        self._stop_serial_update_flag = True

    def update_serial(self):
        while self.connection:
            try:
                if self._stop_serial_update_flag:
                    self.connection.close()
                    thread.exit()
                else:
                    line = self.connection.readline().strip()
                    self.queue.put(line)
            except Exception, e:
                print e

    def send(self, str):
        self.connection.write(str + "\r\n")

    @classmethod
    def list_ports(self):
        if os.name == 'nt':
            # Windows
            available = []
            for i in range(256):
                try:
                    s = serial.Serial(i)
                    available.append('COM'+str(i + 1))
                    s.close()
                except serial.SerialException:
                    pass
            return available
        else:
            # Mac / Linux
            return [port[0] for port in list_ports.comports()]
