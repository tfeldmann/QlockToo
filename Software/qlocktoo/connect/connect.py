import os
import serial
from serial.tools import list_ports
from PySide.QtCore import Slot
from PySide.QtGui import QDialog, QMessageBox
from .connect_ui import Ui_ConnectDialog as Ui


class ConnectDialog(QDialog):

    def __init__(self, parent=None):
        super(ConnectDialog, self).__init__(parent)
        self.ui = Ui()
        self.ui.setupUi(self)
        self.ui.lblDeviceConnected.setText('')
        self.parent = parent

        # get port list on startup
        self.on_btnRefresh_clicked()

        self.connection = None

    def serial_ports(self):
        """
        Returns a generator for all available serial ports
        """
        if os.name == 'nt':
            # windows
            for i in range(256):
                try:
                    s = serial.Serial(i)
                    s.close()
                    yield 'COM' + str(i + 1)
                except serial.SerialException:
                    pass
        else:
            # unix
            for port in list_ports.comports():
                yield port[0]

    @Slot()
    def on_btnRefresh_clicked(self):
        self.connection = None
        self.ui.cmbPorts.clear()
        self.ui.cmbPorts.addItem('Disconnected')
        self.ui.cmbPorts.insertSeparator(1)
        for port in self.serial_ports():
            self.ui.cmbPorts.addItem(port)

    @Slot()
    def on_btnOk_clicked(self):
        self.accept()

    @Slot(int)
    def on_cmbPorts_currentIndexChanged(self, index):
        # comboBox is being cleared
        if index == -1:
            return

        # disconnect
        elif index == 0:
            self._disconnect()

        # connect
        else:
            try:
                self.ui.btnOk.setEnabled(False)
                self.ui.lblDeviceConnected.setText('Please wait...')

                port = self.ui.cmbPorts.currentText()
                self.connection = serial.Serial(port=port,
                                                baudrate=115200,
                                                timeout=1.0)
                self.connection.write('@get_device\n')
                for i, _line in enumerate(self.connection):
                    line = _line.strip()
                    if i == 10:
                        # wait for maximum ten lines
                        break
                    if line.startswith('@get_device'):
                        _line = line.split(' ')
                        self.device = _line[1]
                        self.firmware = _line[2:]
                        self.ui.btnOk.setEnabled(True)
                        self.ui.lblDeviceConnected.setText(
                            'Connected to Device %s with Firmware %s' %
                            (self.device, ' '.join(self.firmware)))
                        return

                # found nothing
                self._disconnect()
                QMessageBox.warning(
                    self, 'Error: ', 'Received no answer from device')

            except Exception as e:
                self._disconnect()
                QMessageBox.warning(self, 'Error: ', str(e))

    def _disconnect(self):
        self.connection = None
        self.ui.cmbPorts.setCurrentIndex(0)
        self.ui.lblDeviceConnected.setText('')
