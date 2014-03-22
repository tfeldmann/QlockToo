#!/usr/bin/env python2
import logging
import sys
from PySide.QtGui import QApplication
from qlocktoo.app import QlockToo

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    application = QApplication(sys.argv)
    app = QlockToo()
    app.show()
    app.raise_()
    application.exec_()
