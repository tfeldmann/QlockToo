# -*- coding: utf-8 -*-
"""
Console App

Send and read serial data from the clock
"""

from PySide.QtGui import *
from PySide.QtCore import *
from ui_console import Ui_console

class ConsoleApp(QDialog):
    def __init__(self, parent=None):
        super(ConsoleApp, self).__init__(parent)
        self.ui = Ui_console()
        self.ui.setupUi(self)

        self.ui.command.returnPressed.connect(self.send_command)
        self.show()

    def send_command(self):
        cmd = self.ui.command.text()
        if cmd:
            self.ui.command.clear()
            self.ui.log.append(cmd)
