# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './qlocktoo/snake/snake.ui'
#
# Created: Wed Mar 26 21:51:37 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_snake(object):
    def setupUi(self, snake):
        snake.setObjectName("snake")
        snake.setWindowModality(QtCore.Qt.ApplicationModal)
        snake.resize(281, 273)
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
        self.label_2 = QtGui.QLabel(snake)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)
        self.label = QtGui.QLabel(snake)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
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
        self.label_2.setText(QtGui.QApplication.translate("snake", "<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600;\">SNAKE</span><br/></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("snake", "<html><head/><body><p align=\"center\"><span style=\" color:#ff0000;\">ENTER drücken um zu starten</span></p><p align=\"center\">Steuerung mit den Pfeiltasten</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

