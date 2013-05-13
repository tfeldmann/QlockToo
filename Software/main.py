# -*- coding: utf-8 -*-
"""
QlockToo

Software suite for controlling the QlockToo hardware.
Author: Thomas Feldmann
"""

from PySide.QtGui import *
from PySide.QtCore import *
from pattern import PatternApp
from settings import SettingsApp
from console import ConsoleApp
from snake import SnakeApp
from marquee import MarqueeApp
from demo import DemoApp
from simulator import Simulator
from device import Device
from serialconnection import SerialConnection
from ui_main import Ui_qlocktoo as Ui


class QlockToo(QMainWindow):
    """
    The QlockToo software suite

    Provides links to the available apps and manages the serial devices and
    simulator.
    """

    def __init__(self):
        " Initializes the application's UI "
        super(QlockToo, self).__init__()
        self.ui = Ui()
        self.ui.setupUi(self)
        self.device = None

        self.refreshPorts()
        self.ui.console.clicked.connect(self.startConsole)
        self.ui.snake.clicked.connect(self.startSnake)
        self.ui.marquee.clicked.connect(self.startMarquee)
        self.ui.pattern.clicked.connect(self.startPattern)
        self.ui.settings.clicked.connect(self.startSettings)
        self.ui.demo.clicked.connect(self.startDemo)
        self.ui.refresh.clicked.connect(self.refreshPorts)
        self.ui.port.currentIndexChanged.connect(self.portSelect)

    def startConsole(self):
        " Start the console app "
        ConsoleApp(device=self.device)

    def startSnake(self):
        " Start Snake"
        SnakeApp(device=self.device)

    def startMarquee(self):
        " Start the marquee app "
        MarqueeApp(device=self.device)

    def startPattern(self):
        " Starts the pattern app "
        PatternApp(device=self.device)

    def startSettings(self):
        " Starts the settings panel "
        SettingsApp(device=self.device)

    def startDemo(self):
        " Start the demo app "
        DemoApp(device=self.device)

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
        if self.device:
            self.device.close()
            self.device = None
        self.ui.appbox.setEnabled(False)

        if index == 1:
            # connect to the simulator
            self.device = Simulator()
            self.ui.appbox.setEnabled(True)

        if index > 1:
            # connect to actual QlockToo device
            try:
                port = self.ui.port.currentText()
                self.device = Device(port=port)
                self.ui.appbox.setEnabled(True)
            except Exception, e:
                QMessageBox.warning(self, "Error: ", e.message)
                self.ui.port.setCurrentIndex(0)


if __name__ == "__main__":
    import sys
    application = QApplication(sys.argv)
    qlocktoo = QlockToo()
    qlocktoo.show()
    application.exec_()
