# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_marquee.ui'
#
# Created: Fri Apr 12 17:02:19 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_marquee(object):
    def setupUi(self, marquee):
        marquee.setObjectName("marquee")
        marquee.setWindowModality(QtCore.Qt.ApplicationModal)
        marquee.resize(567, 155)
        marquee.setSizeGripEnabled(False)
        self.gridLayout = QtGui.QGridLayout(marquee)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtGui.QGroupBox(marquee)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.text = QtGui.QLineEdit(self.groupBox)
        self.text.setObjectName("text")
        self.verticalLayout_2.addWidget(self.text)
        self.play = QtGui.QCheckBox(self.groupBox)
        self.play.setCursor(QtCore.Qt.PointingHandCursor)
        self.play.setObjectName("play")
        self.verticalLayout_2.addWidget(self.play)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 2)
        self.groupBox_3 = QtGui.QGroupBox(marquee)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.speed = QtGui.QDial(self.groupBox_3)
        self.speed.setCursor(QtCore.Qt.PointingHandCursor)
        self.speed.setToolTip("")
        self.speed.setStatusTip("")
        self.speed.setMinimum(-100)
        self.speed.setMaximum(100)
        self.speed.setSingleStep(20)
        self.speed.setProperty("value", 50)
        self.speed.setTracking(True)
        self.speed.setOrientation(QtCore.Qt.Horizontal)
        self.speed.setWrapping(False)
        self.speed.setNotchesVisible(True)
        self.speed.setObjectName("speed")
        self.horizontalLayout.addWidget(self.speed)
        self.gridLayout.addWidget(self.groupBox_3, 0, 3, 1, 1)

        self.retranslateUi(marquee)
        QtCore.QObject.connect(self.play, QtCore.SIGNAL("toggled(bool)"), self.text.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(marquee)

    def retranslateUi(self, marquee):
        marquee.setWindowTitle(QtGui.QApplication.translate("marquee", "Laufschrift", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("marquee", "Text", None, QtGui.QApplication.UnicodeUTF8))
        self.text.setPlaceholderText(QtGui.QApplication.translate("marquee", "Text eingeben...", None, QtGui.QApplication.UnicodeUTF8))
        self.play.setText(QtGui.QApplication.translate("marquee", "Abspielen", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("marquee", "Geschwindigkeit", None, QtGui.QApplication.UnicodeUTF8))

