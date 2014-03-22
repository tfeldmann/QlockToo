from PySide.QtGui import QMainWindow, QDialog, QIcon
from PySide.QtCore import Slot
from qlocktoo.connect import ConnectDialog
from qlocktoo.console import ConsoleApp
from qlocktoo.snake import SnakeApp
from qlocktoo.marquee import MarqueeApp
from qlocktoo.settings import SettingsApp
from qlocktoo.demo import DemoApp
from qlocktoo.timewords import TimeWordsApp

from qlocktoo.device import Device

from app_ui import Ui_qlocktoo as Ui

__version__ = '1.3'


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

        self.device = Device()
        self.simulator = self.ui.simulator
        self.app = TimeWordsApp(device=self.simulator)

    @Slot()
    def on_actionConnect_triggered(self):
        """ Show ConnectionDialog """
        if self.device.connection:
            self.device.disconnect()
            self.ui.actionConnect.setIcon(
                QIcon(':icons/black32/fa-compress.png'))
            self.ui.actionConnect.setText('Verbinden')
        else:
            dialog = ConnectDialog(parent=self)
            if dialog.exec_() == QDialog.Accepted:
                # take over connection from dialog and assign it to the device
                self.device.connection = dialog.connection
                self.ui.actionConnect.setIcon(
                    QIcon(':icons/black32/fa-eject.png'))
                self.ui.actionConnect.setText("Trennen")

    @Slot()
    def on_actionConsole_triggered(self):
        """Start the console app"""
        self.start_app(ConsoleApp)

    @Slot()
    def on_actionSnake_triggered(self):
        """Start Snake"""
        self.start_app(SnakeApp)

    @Slot()
    def on_actionMarquee_triggered(self):
        """Start the marquee app"""
        self.start_app(MarqueeApp)

    @Slot()
    def on_actionSettings_triggered(self):
        """Starts the settings panel"""
        self.start_app(SettingsApp)

    @Slot()
    def on_actionDemo_triggered(self):
        """Start the demo app"""
        self.start_app(DemoApp)

    def start_app(self, App):
        """
        Given a QlockTooApp Class, this method will instanciate and execute the
        app. After execution, the standard timewords app is shown.
        """
        self.app = App(device=self.device,
                       simulator=self.simulator)
        self.app.exec_()
        self.app = TimeWordsApp(device=self.device,
                                simulator=self.simulator)

    def closeEvent(self, event):
        """
        Is called when the user exits the application
        """
        self.device.disconnect()
        event.accept()
