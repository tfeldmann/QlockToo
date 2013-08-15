from PySide.QtGui import QDialog
from pattern_ui import Ui_pattern


class PatternApp(QDialog):
    """
    Pattern App

    Lets the user control each LED in the clock individually and create patterns
    """
    def __init__(self, device):
        super(PatternApp, self).__init__()
        self.ui = Ui_pattern()
        self.ui.setupUi(self)
        self.exec_()
