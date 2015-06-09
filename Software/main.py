import sys
import logging
from PySide import QtGui
from qlocktoo.app import QlockToo


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    app = QtGui.QApplication(sys.argv)
    qlocktoo = QlockToo()
    qlocktoo.show()
    qlocktoo.raise_()
    sys.exit(app.exec_())
