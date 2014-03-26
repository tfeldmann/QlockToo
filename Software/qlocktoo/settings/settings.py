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
    def on_btnDefault_clicked(self):
        """ Set the device back to default settings and load everything again
        """
        self.device.load_default()
        self.on_btnLoad_clicked()

    @QtCore.Slot()
    def on_btnLoad_clicked(self):
        try:
            minimum, maximum = self.device.get_brightness()
            self.ui.brightnessMin.setValue(minimum)
            self.ui.brightnessMax.setValue(maximum)

            (nightmode_enabled,
             brightness,
             time_start,
             time_end) = self.device.get_nightmode()
            self.ui.grpNightMode.setChecked(nightmode_enabled)
            self.ui.nightmodeBrightness.setValue(brightness)
            self.ui.nightmodeStart.setTime(time_start)
            self.ui.nightmodeEnd.setTime(time_end)

            (kiosk_enabled,
             d_word,
             d_seconds,
             d_temperature) = self.device.get_kioskmode()
            self.ui.grpKioskmode.setChecked(kiosk_enabled)
            self.ui.durationWords.setTime(d_word)
            self.ui.durationSeconds.setTime(d_seconds)
            self.ui.durationTemperature.setTime(d_temperature)
        except IOError:
            QtGui.QMessageBox.warning(
                self, 'No device connected', 'Could not read device settings')

    @QtCore.Slot()
    def on_btnSave_clicked(self):
        try:
            self.device.set_brightness(
                minimum=self.ui.brightnessMin.value(),
                maximum=self.ui.brightnessMax.value()
            )
            self.device.set_nightmode(
                enabled=self.ui.grpNightMode.isChecked(),
                brightness=self.ui.nightmodeBrightness.value(),
                time_start=self.ui.nightmodeStart.time().toPython(),
                time_end=self.ui.nightmodeEnd.time().toPython()
            )
            self.device.set_kioskmode(
                enabled=self.ui.grpKioskmode.isChecked(),
                time_words=self.ui.durationWords.time().toPython(),
                time_seconds=self.ui.durationSeconds.time().toPython(),
                time_temp=self.ui.durationTemperature.time().toPython()
            )

        except IOError:
            QtGui.QMessageBox.warning(
                self, 'No device connected', 'Could not save device settings')

    @QtCore.Slot(int)
    def on_brightnessMin_sliderMoved(self, value):
        if self.ui.brightnessMax.value() < value:
            self.ui.brightnessMax.setValue(value)

    @QtCore.Slot(int)
    def on_brightnessMax_sliderMoved(self, value):
        if self.ui.brightnessMin.value() > value:
            self.ui.brightnessMin.setValue(value)
