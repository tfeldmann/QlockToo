# -*- coding: utf-8 -*-
"""
QlockToo

Software suite for controlling the QlockToo hardware.
Author: Thomas Feldmann
"""

from PySide.QtGui import QApplication, QMainWindow
from PySide.QtCore import Slot
from settings import SettingsApp
from console import ConsoleApp
from snake import SnakeApp
from demo import DemoApp
from marquee import MarqueeApp
from device import Device
from serialconnection import SerialConnection
from main_ui import Ui_qlocktoo as Ui


class QlockToo(QMainWindow):
    """
    The QlockToo software suite

    Provides links to the available apps and manages the serial devices and
    simulator.
    """
    def __init__(self):
        """
        Initializes the application's UI
        """
        super(QlockToo, self).__init__()
        self.ui = Ui()
        self.ui.setupUi(self)
        self.device = self.ui.simulator

    @Slot()
    def on_actionConsole_triggered(self):
        """"
        Start the console app
        """
        ConsoleApp(device=self.device)

    @Slot()
    def on_actionSnake_triggered(self):
        """
        Start Snake
        """
        SnakeApp(device=self.device)

    @Slot()
    def on_actionMarquee_triggered(self):
        """
        Start the marquee app
        """
        MarqueeApp(device=self.device)

    @Slot()
    def on_actionSettings_triggered(self):
        """
        Starts the settings panel
        """
        SettingsApp(device=self.device)

    @Slot()
    def on_actionDemo_triggered(self):
        """
        Start the demo app
        """
        DemoApp(device=self.device)

    def refreshPorts(self):
        """
        Refreshes the port list
        """
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
    qlocktoo.raise_()
    application.exec_()
