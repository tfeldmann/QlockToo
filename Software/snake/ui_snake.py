# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_snake.ui'
#
# Created: Tue Apr 16 12:25:56 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_snake(object):
    def setupUi(self, snake):
        snake.setObjectName("snake")
        snake.setWindowModality(QtCore.Qt.ApplicationModal)
        snake.resize(288, 285)
        snake.setSizeGripEnabled(False)
        snake.setModal(True)
        self.gridLayout = QtGui.QGridLayout(snake)
        self.gridLayout.setObjectName("gridLayout")
        self.score = QtGui.QLabel(snake)
        self.score.setObjectName("score")
        self.gridLayout.addWidget(self.score, 0, 0, 1, 1)
        self.highscore = QtGui.QLabel(snake)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.highscore.sizePolicy().hasHeightForWidth())
        self.highscore.setSizePolicy(sizePolicy)
        self.highscore.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.highscore.setObjectName("highscore")
        self.gridLayout.addWidget(self.highscore, 0, 1, 1, 1)
        self.label = QtGui.QLabel(snake)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 2)

        self.retranslateUi(snake)
        QtCore.QMetaObject.connectSlotsByName(snake)

    def retranslateUi(self, snake):
        snake.setWindowTitle(QtGui.QApplication.translate("snake", "Snake", None, QtGui.QApplication.UnicodeUTF8))
        self.score.setText(QtGui.QApplication.translate("snake", "Punkte: 0", None, QtGui.QApplication.UnicodeUTF8))
        self.highscore.setText(QtGui.QApplication.translate("snake", "Highscore: 0", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("snake", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">SNAKE</span></p><p align=\"center\"><br/></p><p align=\"center\"><span style=\" color:#ff0000;\">ENTER drücken um zu starten</span></p><p align=\"center\">Steuern: Pfeiltasten<br/>Pause: P</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    snake = QtGui.QDialog()
    ui = Ui_snake()
    ui.setupUi(snake)
    snake.show()
    sys.exit(app.exec_())

