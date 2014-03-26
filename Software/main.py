import sys
import logging
from PySide import QtGui
from qlocktoo.app import QlockToo


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    application = QtGui.QApplication(sys.argv)
    app = QlockToo()
    app.show()
    app.raise_()
    application.exec_()
