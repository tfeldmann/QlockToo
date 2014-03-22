from PySide import QtCore, QtGui
from settings_ui import Ui_settings as Ui
import time


class SettingsApp(QtGui.QDialog):

    def __init__(self, simulator, device):
        super(SettingsApp, self).__init__()
        self.ui = Ui()
        self.ui.setupUi(self)

        self.simulator = simulator
        self.device = device

    @QtCore.Slot()
    def on_btnSyncTime_clicked(self):
        self.device.set_time(time.localtime())

    @QtCore.Slot()
    def on_btnLoad_clicked(self):
        brightness_min, brightness_max = self.device.get_brightness()
        self.ui.brightnessMin.setValue(brightness_min)
        self.ui.brightnessMax.setValue(brightness_max)

    @QtCore.Slot()
    def on_btnSave_clicked(self):
        self.device.set_brightness(min=0, max=255)
