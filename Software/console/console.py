# -*- coding: utf-8 -*-
"""
Console App

Send and read serial data from the clock
"""

from PySide.QtGui import *
from PySide.QtCore import *
from ui_console import Ui_console as Ui

class ConsoleApp(QDialog):
    def __init__(self, device):
        super(ConsoleApp, self).__init__()
        self.device = device
        self.ui = Ui()
        self.ui.setupUi(self)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.ui.command.returnPressed.connect(self.sendCommand)
        self.exec_()

    def sendCommand(self):
        cmd = self.ui.command.text()
        if cmd:
            self.ui.command.clear()
            self.ui.log.append('<b>Gesendet:</b> <i>'+cmd+'</i>')


