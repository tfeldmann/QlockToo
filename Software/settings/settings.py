# -*- coding: utf-8 -*-
from PySide.QtGui import QDialog
from PySide.QtCore import Qt, Slot
from settings_ui import Ui_settings as Ui
import time


class SettingsApp(QDialog):
    def __init__(self, device):
        super(SettingsApp, self).__init__()
        self.device = device
        self.ui = Ui()
        self.ui.setupUi(self)
        self.ui.syncTime.clicked.connect(self.syncTime)

    def syncTime(self):
        """
        Syncs the clock time with the pc time
        """
        localtime = time.localtime()
        cmd = "@settime %d %d %d %d %d %d" % (localtime.tm_year,
            localtime.tm_mon, localtime.tm_mday, localtime.tm_hour,
            localtime.tm_min, localtime.tm_sec)
        self.device.send(cmd)
