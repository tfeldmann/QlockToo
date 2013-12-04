from PySide.QtGui import QMainWindow, QDialog
from PySide.QtCore import Slot
from qlocktoo.connect import ConnectDialog
from qlocktoo.console import ConsoleApp
from qlocktoo.snake import SnakeApp
from qlocktoo.marquee import MarqueeApp
from qlocktoo.settings import SettingsApp
from qlocktoo.demo import DemoApp
from qlocktoo.timewords import TimeWordsApp
from app_ui import Ui_qlocktoo as Ui

__version__ = '1.1'


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
        self.device.signal_linereceived.connect(self.brop)
        self.app = TimeWordsApp(device=self.device)

    @Slot()
    def on_actionConnect_triggered(self):
        """
        Show ConnectionDialog
        """
        if self.device.is_connected():
            self.device.disconnect()
            self.ui.actionConnect.setText('Verbinden')
        else:
            dialog = ConnectDialog(self)
            if dialog.exec_() == QDialog.Accepted:
                # take over connection from dialog and assign it to the device
                self.device.use_connection(dialog.connection)
                self.ui.actionConnect.setText("Trennen")

    @Slot(str)
    def brop(self, s):
        print s

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
