# -*- coding: utf-8 -*-
"""
QlockTwo

Software for controlling our self-built QlockTwo remake
Author: Thomas Feldmann
"""

from PySide.QtGui import *
from PySide.QtCore import *
from pattern import PatternApp
from console import ConsoleApp
from simulator import Simulator
from device import Device
from serialconnection import SerialConnection
from ui_qlocktwo import Ui_qlocktwo as Ui


class QlockTwo(QMainWindow):
    """
    The QlockTwo software suite

    Provides links to the available apps and manages the serial devices and
    simulator.
    """

    def __init__(self):
        " Initializes the application's UI "
        super(QlockTwo, self).__init__()
        self.ui = Ui()
        self.ui.setupUi(self)

        self.refreshPorts()

        self.ui.refresh.clicked.connect(self.refreshPorts)
        self.ui.pattern.clicked.connect(self.startPattern)
        self.ui.console.clicked.connect(self.startConsole)
        self.ui.port.currentIndexChanged.connect(self.portSelect)

    def startPattern(self):
        " Starts the pattern app "
        app = PatternApp(device=self.device)

    def startConsole(self):
        " Start the console app "
        app = ConsoleApp(device=self.device)

    def refreshPorts(self):
        " refreshes the port list "
        self.ui.port.clear()
        self.ui.port.addItem('Getrennt')
        self.ui.port.addItem('Simulator')
        for port in SerialConnection.list_ports():
            self.ui.port.addItem(port)

    def portSelect(self, index):
        """
        Connects / disconnects a device

        This method is called when the user selected a device in the ports
        combo box. The Device can be either the simulator or a serial device.
        """
        # disconnect device / stop simulator
        self.device = None
        self.ui.appbox.setEnabled(False)

        if index == 1:
            # connect to the simulator
            self.device = Simulator()
            self.ui.appbox.setEnabled(True)

        if index > 1:
            # connect to actual QlockTwo remake
            try:
                port = self.ui.port.currentText()
                self.device = Device(port=port, baudrate=57600)
                self.ui.appbox.setEnabled(True)
            except Exception, e:
                QMessageBox.warning(self, "Error: ", e.message)


if __name__ == "__main__":
    import sys
    application = QApplication(sys.argv)
    qlocktwo = QlockTwo()
    qlocktwo.show()
    application.exec_()
