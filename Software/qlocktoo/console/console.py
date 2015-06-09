from PySide.QtGui import QDialog
from .console_ui import Ui_console as Ui


class ConsoleApp(QDialog):

    """
    Console App
    Send and read serial data from the clock
    """

    def __init__(self, device=None, simulator=None):
        super(ConsoleApp, self).__init__()
        self.ui = Ui()
        self.ui.setupUi(self)

        self.device = device
        self.simulator = simulator

        if self.device.connection:
            self.ui.command.returnPressed.connect(self.sendCommand)
            if not self in self.device.observers:
                self.device.observers.append(self)
        else:
            self.ui.command.setText('Nicht verbunden')
            self.ui.command.setEnabled(False)

    def sendCommand(self):
        cmd = self.ui.command.text()
        if cmd == 'clear':
            self.ui.log.clear()
            self.ui.command.clear()
        elif cmd:
            try:
                self.ui.log.append('<b>Gesendet:</b> <i>' + cmd + '</i>')
                self.device.request(cmd.encode('utf-8'))
            except:
                pass
            finally:
                self.ui.command.clear()

    def notify_serial_receive(self, msg):
        if msg[0] == '!':
            self.ui.log.append(
                '<pre><font color=red>' + msg + '</font></pre>')
        else:
            self.ui.log.append(
                '<font color=blue><pre>' + msg + '</pre></font>')
