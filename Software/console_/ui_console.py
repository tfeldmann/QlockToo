# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_console.ui'
#
# Created: Tue Apr  9 15:43:45 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_console(object):
    def setupUi(self, console):
        console.setObjectName("console")
        console.setWindowModality(QtCore.Qt.ApplicationModal)
        console.resize(464, 337)
        console.setSizeGripEnabled(False)
        self.horizontalLayout = QtGui.QHBoxLayout(console)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.command = QtGui.QLineEdit(console)
        self.command.setObjectName("command")
        self.verticalLayout.addWidget(self.command)
        self.log = QtGui.QTextEdit(console)
        self.log.setUndoRedoEnabled(False)
        self.log.setReadOnly(True)
        self.log.setObjectName("log")
        self.verticalLayout.addWidget(self.log)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(console)
        QtCore.QMetaObject.connectSlotsByName(console)

    def retranslateUi(self, console):
        console.setWindowTitle(QtGui.QApplication.translate("console", "Konsole", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    console = QtGui.QDialog()
    ui = Ui_console()
    ui.setupUi(console)
    console.show()
    sys.exit(app.exec_())

