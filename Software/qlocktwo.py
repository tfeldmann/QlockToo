# -*- coding: utf-8 -*-
"""
QlockTwo

Software for controlling our self-built QlockTwo remake
@author Thomas Feldmann
"""

from PySide.QtGui import *
from PySide.QtCore import *
from ui_qlocktwo import Ui_qlocktwo
from Pattern.app import PatternApp
from Console.app import ConsoleApp

class QlockTwo(QMainWindow):
    def __init__(self):
        " Initialize the main application "
        super(QlockTwo, self).__init__()
        self.ui = Ui_qlocktwo()
        self.ui.setupUi(self)

        self.ui.refresh.clicked.connect(self.refresh_ports)
        self.ui.pattern.clicked.connect(self.pattern_app)
        self.ui.console.clicked.connect(self.console_app)

        self.refresh_ports()
        self.ui.appbox.setEnabled(True)  # comment if not needed

    def refresh_ports(self):
        " Refreshed the port list "
        self.ui.port.clear()
        self.ui.port.addItem('Getrennt')

    def pattern_app(self):
        " Start pattern app "
        app = PatternApp(self)

    def console_app(self):
        " Start the console app "
        app = ConsoleApp(self)

    def port_select(self, index):
        # disconnect
        if index == 0:
            self.serial.stop()
        # connect
        else:
            try:
                port = self.ui.serial_select.currentText()
                self.serial.connect(port=port, baud=19200)
            except Exception, e:
                QMessageBox.warning(self, "Error", e.message)


if __name__ == "__main__":
    import sys
    application = QApplication(sys.argv)
    qlocktwo = QlockTwo()
    qlocktwo.show()
    application.exec_()
