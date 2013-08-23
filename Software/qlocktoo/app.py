from PySide.QtGui import QMainWindow, QMessageBox
from PySide.QtCore import Slot
import device
from connect.serialconnection import SerialConnection
from console import ConsoleApp
from snake import SnakeApp
from marquee import MarqueeApp
from settings import SettingsApp
from demo import DemoApp
from timewords import TimeWordsApp
from app_ui import Ui_qlocktoo as Ui

__version__ = '1.0'


class QlockToo(QMainWindow):

    """
    QlockToo

    The main window that contains the simulator widget. From here you can start
    all the provided apps.
    """

    def __init__(self):
        """
        Initializes the application's UI
        """
        super(QlockToo, self).__init__()
        self.ui = Ui()
        self.ui.setupUi(self)
        self.setWindowTitle('QlockToo v{0}'.format(__version__))
        self.device = self.ui.simulator
        self.app = TimeWordsApp(device=self.device)

    @Slot()
    def on_actionConsole_triggered(self):
        """Start the console app"""
        self.startApp(ConsoleApp)

    @Slot()
    def on_actionSnake_triggered(self):
        """Start Snake"""
        self.startApp(SnakeApp)

    @Slot()
    def on_actionMarquee_triggered(self):
        """Start the marquee app"""
        self.startApp(MarqueeApp)

    @Slot()
    def on_actionSettings_triggered(self):
        """Starts the settings panel"""
        self.startApp(SettingsApp)

    @Slot()
    def on_actionDemo_triggered(self):
        """Start the demo app"""
        self.startApp(DemoApp)

    def startApp(self, App):
        """
        Given a QlockTooApp Class, this method will instanciate and execute the
        app. After execution, the standard timewords app is shown.
        """
        self.app = App(device=self.device)
        self.app.exec_()
        self.app = TimeWordsApp(device=self.device)

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
            self.device = device.Simulator()
            self.ui.appbox.setEnabled(True)

        if index > 1:
            # connect to actual QlockToo device
            try:
                port = self.ui.port.currentText()
                self.device = device.Device(port=port)
                self.ui.appbox.setEnabled(True)
            except Exception, e:
                QMessageBox.warning(self, "Error: ", e.message)
                self.ui.port.setCurrentIndex(0)
