# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_marquee.ui'
#
# Created: Thu Apr 11 15:28:08 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_marquee(object):
    def setupUi(self, marquee):
        marquee.setObjectName("marquee")
        marquee.setWindowModality(QtCore.Qt.ApplicationModal)
        marquee.resize(391, 367)
        marquee.setSizeGripEnabled(False)
        self.gridLayout = QtGui.QGridLayout(marquee)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtGui.QGroupBox(marquee)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.text = QtGui.QLineEdit(self.groupBox)
        self.text.setObjectName("text")
        self.verticalLayout_2.addWidget(self.text)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 2)
        self.groupBox_3 = QtGui.QGroupBox(marquee)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.speed = QtGui.QDial(self.groupBox_3)
        self.speed.setMinimum(-100)
        self.speed.setMaximum(100)
        self.speed.setSingleStep(20)
        self.speed.setProperty("value", -50)
        self.speed.setOrientation(QtCore.Qt.Horizontal)
        self.speed.setWrapping(False)
        self.speed.setNotchesVisible(True)
        self.speed.setObjectName("speed")
        self.gridLayout_2.addWidget(self.speed, 0, 0, 1, 1)
        self.speedLabel = QtGui.QLabel(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.speedLabel.sizePolicy().hasHeightForWidth())
        self.speedLabel.setSizePolicy(sizePolicy)
        self.speedLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.speedLabel.setObjectName("speedLabel")
        self.gridLayout_2.addWidget(self.speedLabel, 1, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.stepwise = QtGui.QRadioButton(self.groupBox_2)
        self.stepwise.setObjectName("stepwise")
        self.gridLayout_3.addWidget(self.stepwise, 2, 0, 1, 1)
        self.smooth = QtGui.QRadioButton(self.groupBox_2)
        self.smooth.setChecked(True)
        self.smooth.setObjectName("smooth")
        self.gridLayout_3.addWidget(self.smooth, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_2, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_3, 1, 0, 1, 2)

        self.retranslateUi(marquee)
        QtCore.QMetaObject.connectSlotsByName(marquee)

    def retranslateUi(self, marquee):
        marquee.setWindowTitle(QtGui.QApplication.translate("marquee", "Laufschrift", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("marquee", "Text", None, QtGui.QApplication.UnicodeUTF8))
        self.text.setPlaceholderText(QtGui.QApplication.translate("marquee", "Text eingeben...", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("marquee", "Einstellungen", None, QtGui.QApplication.UnicodeUTF8))
        self.speedLabel.setText(QtGui.QApplication.translate("marquee", "Nach links, 50 %", None, QtGui.QApplication.UnicodeUTF8))
        self.stepwise.setText(QtGui.QApplication.translate("marquee", "Einzelbuchstaben", None, QtGui.QApplication.UnicodeUTF8))
        self.smooth.setText(QtGui.QApplication.translate("marquee", "Flüssig", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    marquee = QtGui.QDialog()
    ui = Ui_marquee()
    ui.setupUi(marquee)
    marquee.show()
    sys.exit(app.exec_())

