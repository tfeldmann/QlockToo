# -*- coding: utf-8 -*-
"""
QlockTwo

Software for controlling our self-built QlockTwo remake
@author Thomas Feldmann
"""

from PySide.QtGui import *
from PySide.QtCore import *
from qlocktwo_gui import Ui_QlockTwo


class QlockTwo(QMainWindow):
    def __init__(self):
        super(QlockTwo, self).__init__()
        self.ui = Ui_QlockTwo()
        self.ui.setupUi(self)

        self.ui.update.clicked.connect(self.update)

    def update(self):
        pass


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    qlocktwo = QlockTwo()
    qlocktwo.show()
    app.exec_()
