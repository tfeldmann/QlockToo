# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_snake.ui'
#
# Created: Mon Apr 15 22:35:40 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_snake(object):
    def setupUi(self, snake):
        snake.setObjectName("snake")
        snake.setWindowModality(QtCore.Qt.ApplicationModal)
        snake.resize(256, 254)
        snake.setSizeGripEnabled(False)
        snake.setModal(True)
        self.gridLayout = QtGui.QGridLayout(snake)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(snake)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(snake)
        QtCore.QMetaObject.connectSlotsByName(snake)

    def retranslateUi(self, snake):
        snake.setWindowTitle(QtGui.QApplication.translate("snake", "Snake", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("snake", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">SNAKE</span></p><p align=\"center\"><br/></p><p align=\"center\"><span style=\" color:#ff0000;\">ENTER drücken um zu starten</span></p><p align=\"center\">Steuern: Pfeiltasten</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    snake = QtGui.QDialog()
    ui = Ui_snake()
    ui.setupUi(snake)
    snake.show()
    sys.exit(app.exec_())

