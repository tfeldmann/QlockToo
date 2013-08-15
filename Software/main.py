import sys
from PySide.QtGui import QApplication
from qlocktoo.app import QlockToo
import buildtools

if __name__ == "__main__":
    buildtools.run(ui=True, qrc=False)
    application = QApplication(sys.argv)
    app = QlockToo()
    app.show()
    app.raise_()
    application.exec_()
