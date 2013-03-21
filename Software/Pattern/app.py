# -*- coding: utf-8 -*-
"""
Pattern App

Lets the user control each LED in the clock individually and create patterns
"""

from PySide.QtGui import *
from PySide.QtCore import *
from ui_pattern import Ui_pattern

class PatternApp(QDialog):
    def __init__(self, parent=None):
        super(PatternApp, self).__init__(parent)
        self.ui = Ui_pattern()
        self.ui.setupUi(self)
        self.show()
