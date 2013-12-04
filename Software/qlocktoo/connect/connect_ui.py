# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './qlocktoo/connect/connect.ui'
#
# Created: Wed Dec  4 14:09:58 2013
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ConnectDialog(object):
    def setupUi(self, ConnectDialog):
        ConnectDialog.setObjectName("ConnectDialog")
        ConnectDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        ConnectDialog.resize(345, 173)
        ConnectDialog.setSizeGripEnabled(False)
        self.verticalLayout = QtGui.QVBoxLayout(ConnectDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtGui.QGroupBox(ConnectDialog)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cmbPorts = QtGui.QComboBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbPorts.sizePolicy().hasHeightForWidth())
        self.cmbPorts.setSizePolicy(sizePolicy)
        self.cmbPorts.setObjectName("cmbPorts")
        self.horizontalLayout.addWidget(self.cmbPorts)
        self.btnRefresh = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnRefresh.sizePolicy().hasHeightForWidth())
        self.btnRefresh.setSizePolicy(sizePolicy)
        self.btnRefresh.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/black32/fa-refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRefresh.setIcon(icon)
        self.btnRefresh.setObjectName("btnRefresh")
        self.horizontalLayout.addWidget(self.btnRefresh)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.lblDeviceConnected = QtGui.QLabel(self.groupBox)
        self.lblDeviceConnected.setObjectName("lblDeviceConnected")
        self.verticalLayout_2.addWidget(self.lblDeviceConnected)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout.addWidget(self.groupBox)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.btnCancel = QtGui.QPushButton(ConnectDialog)
        self.btnCancel.setObjectName("btnCancel")
        self.horizontalLayout_3.addWidget(self.btnCancel)
        self.btnOk = QtGui.QPushButton(ConnectDialog)
        self.btnOk.setDefault(True)
        self.btnOk.setObjectName("btnOk")
        self.horizontalLayout_3.addWidget(self.btnOk)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(ConnectDialog)
        QtCore.QObject.connect(self.btnCancel, QtCore.SIGNAL("clicked()"), ConnectDialog.reject)
        QtCore.QObject.connect(self.btnOk, QtCore.SIGNAL("clicked()"), ConnectDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(ConnectDialog)
        ConnectDialog.setTabOrder(self.cmbPorts, self.btnRefresh)
        ConnectDialog.setTabOrder(self.btnRefresh, self.btnCancel)
        ConnectDialog.setTabOrder(self.btnCancel, self.btnOk)

    def retranslateUi(self, ConnectDialog):
        ConnectDialog.setWindowTitle(QtGui.QApplication.translate("ConnectDialog", "Verbindung", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("ConnectDialog", "Verbindung", None, QtGui.QApplication.UnicodeUTF8))
        self.lblDeviceConnected.setText(QtGui.QApplication.translate("ConnectDialog", "Nicht verbunden", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCancel.setText(QtGui.QApplication.translate("ConnectDialog", "Abbrechen", None, QtGui.QApplication.UnicodeUTF8))
        self.btnOk.setText(QtGui.QApplication.translate("ConnectDialog", "OK", None, QtGui.QApplication.UnicodeUTF8))

from . import assets_rc
