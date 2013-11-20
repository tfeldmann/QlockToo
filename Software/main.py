import sys
import platform
from PySide.QtGui import QApplication, QFont
from qlocktoo.app import QlockToo

if __name__ == "__main__":
    # Fix OS X Mavericks QT font bug
    if platform.mac_ver()[0].split('.')[:2] == ['10', '9']:
        QFont.insertSubstitution('.Lucida Grande UI', 'Lucida Grande')

    application = QApplication(sys.argv)
    app = QlockToo()
    app.show()
    app.raise_()
    application.exec_()
