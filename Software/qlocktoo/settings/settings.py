from PySide import QtCore, QtGui
from settings_ui import Ui_settings as Ui
import time


class SettingsApp(QtGui.QDialog):

    def __init__(self, simulator, device):
        super(SettingsApp, self).__init__()
        self.ui = Ui()
        self.ui.setupUi(self)

        self.device = device
        self.simulator = simulator

        self.on_btnLoad_clicked()

    @QtCore.Slot()
    def on_btnSyncTime_clicked(self):
        self.device.set_time(time.localtime())

    @QtCore.Slot()
    def on_btnLoad_clicked(self):
        minimum, maximum = self.device.get_brightness()
        self.ui.brightnessMin.setValue(minimum)
        self.ui.brightnessMax.setValue(maximum)

    @QtCore.Slot()
    def on_btnSave_clicked(self):
        self.device.set_brightness(minimum=self.ui.brightnessMin.value(),
                                   maximum=self.ui.brightnessMax.value())

    @QtCore.Slot(int)
    def on_brightnessMin_sliderMoved(self, value):
        if self.ui.brightnessMax.value() < value:
            self.ui.brightnessMax.setValue(value)

    @QtCore.Slot(int)
    def on_brightnessMax_sliderMoved(self, value):
        if self.ui.brightnessMin.value() > value:
            self.ui.brightnessMin.setValue(value)
