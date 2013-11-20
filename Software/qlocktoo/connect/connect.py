import os
import time
import serial
from serial.tools import list_ports
from PySide.QtGui import QDialog, QMessageBox
from PySide.QtCore import Slot


class Device(object):

    def __init__(self, port=None, baudrate=19200, timeout=60):
        if port:
            self.connection = serial.Serial(port=port,
                                            baudrate=baudrate,
                                            timeout=timeout)
        else:
            self.connection = None

    def request(self, cmd, *args):
        c = self.connection
        c.write(cmd + " " + " ".join(args) + "\n")
        for line in c:
            line = line.strip()
            print(line)

            if not (line[0] == '!' or line[0] == '#' or line[0] == '@'):
                continue  # most likely garbage

            # check for errors
            if line[0] == '!':
                raise Exception(line)

            # check for result
            if cmd in line:
                result = line.split(" ")[1:]
                if len(result) == 1:
                    return result[0]
                else:
                    return result

    def device(self):
        result = self.request('@device')
        return {
            'device': result[0],
            'firmware': result[1]
        }


class ConnectDialog(QDialog):

    def __init__(self, parent=None):
        from connect_ui import Ui_ConnectDialog as Ui
        super(ConnectDialog, self).__init__(parent)
        self.ui = Ui()
        self.ui.setupUi(self)
        self.ui.lblDeviceConnected.setText('')
        self.parent = parent

        # get port list on startup
        self.on_btnRefresh_clicked()

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
        self.device = None
        self.ui.cmbPorts.clear()
        self.ui.cmbPorts.addItem('Disconnected')
        self.ui.cmbPorts.insertSeparator(1)
        for port in self.serial_ports():
            self.ui.cmbPorts.addItem(port)

    @Slot()
    def on_btnOk_clicked(self):
        print("ok")
        # if self.about['device'] == 'P1':
        #     self.parent.device = device.P1()
        #     self.parent.device.connection = self.device.connection
        # else:
        #     self.parent.device = None

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
                # try connecting to the default device class
                self.device = Device(
                    port=self.ui.cmbPorts.currentText(),
                    baudrate=115200,
                    timeout=5)

                time.sleep(2.0)

                self.device = self.device.device()
                about_line = ('Verbunden mit {device}'
                              ', Firmware v{firmware}').format(**self.device)

                self.ui.lblDeviceConnected.setText(about_line)
            except TypeError as e:
                self._disconnect()
                QMessageBox.warning(
                    self, 'Error: ', 'Received no answer from device')
            except Exception as e:
                self._disconnect()
                QMessageBox.warning(self, 'Error: ', str(e))

    def _disconnect(self):
        self.device = None
        self.ui.cmbPorts.setCurrentIndex(0)
        self.ui.lblDeviceConnected.setText('')
