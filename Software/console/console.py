# -*- coding: utf-8 -*-
from PySide.QtGui import QDialog
from console_ui import Ui_console as Ui


class ConsoleApp(QDialog):
    """
    Console App
    Send and read serial data from the clock
    """
    def __init__(self, device):
        super(ConsoleApp, self).__init__()
        self.device = device
        self.device.callback = self.incomingSerial
        self.ui = Ui()
        self.ui.setupUi(self)
        self.ui.command.returnPressed.connect(self.sendCommand)

    def sendCommand(self):
        cmd = self.ui.command.text()
        if cmd == 'clear':
            self.ui.log.clear()
            self.ui.command.clear()
        elif cmd:
            self.ui.log.append('<b>Gesendet:</b> <i>'+cmd+'</i>')
            self.device.send(cmd)
            self.ui.command.clear()

    def incomingSerial(self, input):
        identifier, message = input[0], input[1:]
        if identifier == '#':
            self.ui.log.append('<pre><font color=blue>'+message+'</font></pre>')
        elif identifier == '!':
            self.ui.log.append('<pre><font color=red>'+message+'</font></pre>')
        else:
            self.ui.log.append(message)
