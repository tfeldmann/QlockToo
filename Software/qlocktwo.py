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
        super(QlockTwo, self).__init__()
        self.ui = Ui_qlocktwo()
        self.ui.setupUi(self)

        self.ui.pattern.clicked.connect(self.pattern_app)
        self.ui.update.clicked.connect(self.check_updates)

    def pattern_app(self):
        app = PatternApp(self)

    def check_updates(self):
        pass


if __name__ == "__main__":
    import sys
    application = QApplication(sys.argv)
    qlocktwo = QlockTwo()
    qlocktwo.show()
    application.exec_()
