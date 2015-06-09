# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qlocktoo/console/console.ui'
#
# Created: Sat May 16 18:47:23 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_console(object):
    def setupUi(self, console):
        console.setObjectName("console")
        console.setWindowModality(QtCore.Qt.ApplicationModal)
        console.resize(455, 415)
        console.setSizeGripEnabled(False)
        self.horizontalLayout = QtGui.QHBoxLayout(console)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.log = QtGui.QTextEdit(console)
        self.log.setFocusPolicy(QtCore.Qt.NoFocus)
        self.log.setUndoRedoEnabled(False)
        self.log.setReadOnly(True)
        self.log.setObjectName("log")
        self.verticalLayout.addWidget(self.log)
        self.command = QtGui.QLineEdit(console)
        self.command.setObjectName("command")
        self.verticalLayout.addWidget(self.command)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(console)
        QtCore.QMetaObject.connectSlotsByName(console)

    def retranslateUi(self, console):
        console.setWindowTitle(QtGui.QApplication.translate("console", "Konsole", None, QtGui.QApplication.UnicodeUTF8))
        self.command.setPlaceholderText(QtGui.QApplication.translate("console", "Befehl", None, QtGui.QApplication.UnicodeUTF8))

