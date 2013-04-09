# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_demo.ui'
#
# Created: Tue Apr  9 21:28:19 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_demoapp(object):
    def setupUi(self, demoapp):
        demoapp.setObjectName("demoapp")
        demoapp.setWindowModality(QtCore.Qt.ApplicationModal)
        demoapp.resize(134, 194)
        demoapp.setSizeGripEnabled(False)
        self.verticalLayout = QtGui.QVBoxLayout(demoapp)
        self.verticalLayout.setObjectName("verticalLayout")
        self.black = QtGui.QPushButton(demoapp)
        self.black.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.black.setAutoDefault(False)
        self.black.setFlat(False)
        self.black.setObjectName("black")
        self.verticalLayout.addWidget(self.black)
        self.white = QtGui.QPushButton(demoapp)
        self.white.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.white.setAutoDefault(False)
        self.white.setFlat(False)
        self.white.setObjectName("white")
        self.verticalLayout.addWidget(self.white)
        self.fade = QtGui.QPushButton(demoapp)
        self.fade.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.fade.setAutoDefault(False)
        self.fade.setFlat(False)
        self.fade.setObjectName("fade")
        self.verticalLayout.addWidget(self.fade)
        self.wave = QtGui.QPushButton(demoapp)
        self.wave.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.wave.setAutoDefault(False)
        self.wave.setFlat(False)
        self.wave.setObjectName("wave")
        self.verticalLayout.addWidget(self.wave)

        self.retranslateUi(demoapp)
        QtCore.QMetaObject.connectSlotsByName(demoapp)

    def retranslateUi(self, demoapp):
        demoapp.setWindowTitle(QtGui.QApplication.translate("demoapp", "Demo", None, QtGui.QApplication.UnicodeUTF8))
        self.black.setText(QtGui.QApplication.translate("demoapp", "Schwarz", None, QtGui.QApplication.UnicodeUTF8))
        self.white.setText(QtGui.QApplication.translate("demoapp", "Weiß", None, QtGui.QApplication.UnicodeUTF8))
        self.fade.setText(QtGui.QApplication.translate("demoapp", "Puls", None, QtGui.QApplication.UnicodeUTF8))
        self.wave.setText(QtGui.QApplication.translate("demoapp", "Welle", None, QtGui.QApplication.UnicodeUTF8))

