# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_demo.ui'
#
# Created: Thu Apr 11 23:15:20 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_demoapp(object):
    def setupUi(self, demoapp):
        demoapp.setObjectName("demoapp")
        demoapp.setWindowModality(QtCore.Qt.ApplicationModal)
        demoapp.resize(220, 192)
        demoapp.setSizeGripEnabled(False)
        self.gridLayout = QtGui.QGridLayout(demoapp)
        self.gridLayout.setObjectName("gridLayout")
        self.black = QtGui.QPushButton(demoapp)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.black.sizePolicy().hasHeightForWidth())
        self.black.setSizePolicy(sizePolicy)
        self.black.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.black.setIconSize(QtCore.QSize(30, 30))
        self.black.setAutoDefault(False)
        self.black.setFlat(False)
        self.black.setObjectName("black")
        self.gridLayout.addWidget(self.black, 0, 0, 1, 1)
        self.fade = QtGui.QPushButton(demoapp)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fade.sizePolicy().hasHeightForWidth())
        self.fade.setSizePolicy(sizePolicy)
        self.fade.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.fade.setIconSize(QtCore.QSize(30, 30))
        self.fade.setAutoDefault(False)
        self.fade.setFlat(False)
        self.fade.setObjectName("fade")
        self.gridLayout.addWidget(self.fade, 2, 0, 1, 1)
        self.white = QtGui.QPushButton(demoapp)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.white.sizePolicy().hasHeightForWidth())
        self.white.setSizePolicy(sizePolicy)
        self.white.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.white.setIconSize(QtCore.QSize(30, 30))
        self.white.setAutoDefault(False)
        self.white.setFlat(False)
        self.white.setObjectName("white")
        self.gridLayout.addWidget(self.white, 0, 1, 1, 1)
        self.wave = QtGui.QPushButton(demoapp)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wave.sizePolicy().hasHeightForWidth())
        self.wave.setSizePolicy(sizePolicy)
        self.wave.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.wave.setIconSize(QtCore.QSize(30, 30))
        self.wave.setAutoDefault(False)
        self.wave.setFlat(False)
        self.wave.setObjectName("wave")
        self.gridLayout.addWidget(self.wave, 2, 1, 1, 1)

        self.retranslateUi(demoapp)
        QtCore.QMetaObject.connectSlotsByName(demoapp)

    def retranslateUi(self, demoapp):
        demoapp.setWindowTitle(QtGui.QApplication.translate("demoapp", "Demo", None, QtGui.QApplication.UnicodeUTF8))
        self.black.setText(QtGui.QApplication.translate("demoapp", "Schwarz", None, QtGui.QApplication.UnicodeUTF8))
        self.fade.setText(QtGui.QApplication.translate("demoapp", "Puls", None, QtGui.QApplication.UnicodeUTF8))
        self.white.setText(QtGui.QApplication.translate("demoapp", "Weiß", None, QtGui.QApplication.UnicodeUTF8))
        self.wave.setText(QtGui.QApplication.translate("demoapp", "Welle", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    demoapp = QtGui.QDialog()
    ui = Ui_demoapp()
    ui.setupUi(demoapp)
    demoapp.show()
    sys.exit(app.exec_())

