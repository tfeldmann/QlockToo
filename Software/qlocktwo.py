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

class QlockTwo(QMainWindow):
    def __init__(self):
        """ Initialize the main application """
        super(QlockTwo, self).__init__()
        self.ui = Ui_qlocktwo()
        self.ui.setupUi(self)

        self.ui.refresh.clicked.connect(self.refresh_ports)
        self.ui.pattern.clicked.connect(self.pattern_app)
        self.ui.update.clicked.connect(self.check_updates)

        self.refresh_ports()

    def refresh_ports(self):
        """ Refreshed the port list """
        self.ui.port.clear()
        self.ui.port.addItem('Getrennt')

    def pattern_app(self):
        """ Start pattern app """
        app = PatternApp(self)

    def check_updates(self):
        """ Check for updates """
        pass


if __name__ == "__main__":
    import sys
    application = QApplication(sys.argv)
    qlocktwo = QlockTwo()
    qlocktwo.show()
    application.exec_()
