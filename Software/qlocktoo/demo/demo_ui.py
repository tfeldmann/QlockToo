# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './qlocktoo/demo/demo.ui'
#
# Created: Wed Dec  4 14:09:58 2013
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_demoapp(object):
    def setupUi(self, demoapp):
        demoapp.setObjectName("demoapp")
        demoapp.setWindowModality(QtCore.Qt.ApplicationModal)
        demoapp.resize(408, 290)
        demoapp.setSizeGripEnabled(False)
        self.gridLayout = QtGui.QGridLayout(demoapp)
        self.gridLayout.setObjectName("gridLayout")
        self.fade = QtGui.QPushButton(demoapp)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fade.sizePolicy().hasHeightForWidth())
        self.fade.setSizePolicy(sizePolicy)
        self.fade.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/black32/fa-arrows-h.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fade.setIcon(icon)
        self.fade.setIconSize(QtCore.QSize(32, 32))
        self.fade.setAutoDefault(False)
        self.fade.setFlat(False)
        self.fade.setObjectName("fade")
        self.gridLayout.addWidget(self.fade, 2, 1, 1, 1)
        self.helix = QtGui.QPushButton(demoapp)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.helix.sizePolicy().hasHeightForWidth())
        self.helix.setSizePolicy(sizePolicy)
        self.helix.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/black32/fa-random.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.helix.setIcon(icon1)
        self.helix.setIconSize(QtCore.QSize(32, 32))
        self.helix.setAutoDefault(False)
        self.helix.setFlat(False)
        self.helix.setObjectName("helix")
        self.gridLayout.addWidget(self.helix, 4, 2, 1, 1)
        self.wave = QtGui.QPushButton(demoapp)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wave.sizePolicy().hasHeightForWidth())
        self.wave.setSizePolicy(sizePolicy)
        self.wave.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/black32/fa-bullseye.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.wave.setIcon(icon2)
        self.wave.setIconSize(QtCore.QSize(32, 32))
        self.wave.setAutoDefault(False)
        self.wave.setFlat(False)
        self.wave.setObjectName("wave")
        self.gridLayout.addWidget(self.wave, 2, 2, 1, 1)
        self.pong = QtGui.QPushButton(demoapp)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pong.sizePolicy().hasHeightForWidth())
        self.pong.setSizePolicy(sizePolicy)
        self.pong.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/black32/fa-gamepad.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pong.setIcon(icon3)
        self.pong.setIconSize(QtCore.QSize(32, 32))
        self.pong.setAutoDefault(False)
        self.pong.setFlat(False)
        self.pong.setObjectName("pong")
        self.gridLayout.addWidget(self.pong, 4, 1, 1, 1)
        self.pulse = QtGui.QPushButton(demoapp)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pulse.sizePolicy().hasHeightForWidth())
        self.pulse.setSizePolicy(sizePolicy)
        self.pulse.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/black32/fa-refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pulse.setIcon(icon4)
        self.pulse.setIconSize(QtCore.QSize(32, 32))
        self.pulse.setAutoDefault(False)
        self.pulse.setFlat(False)
        self.pulse.setObjectName("pulse")
        self.gridLayout.addWidget(self.pulse, 2, 0, 1, 1)
        self.white = QtGui.QPushButton(demoapp)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.white.sizePolicy().hasHeightForWidth())
        self.white.setSizePolicy(sizePolicy)
        self.white.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/black32/fa-square-o.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.white.setIcon(icon5)
        self.white.setIconSize(QtCore.QSize(32, 32))
        self.white.setAutoDefault(False)
        self.white.setFlat(False)
        self.white.setObjectName("white")
        self.gridLayout.addWidget(self.white, 1, 0, 1, 1)
        self.black = QtGui.QPushButton(demoapp)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.black.sizePolicy().hasHeightForWidth())
        self.black.setSizePolicy(sizePolicy)
        self.black.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/black32/fa-square.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.black.setIcon(icon6)
        self.black.setIconSize(QtCore.QSize(32, 32))
        self.black.setAutoDefault(False)
        self.black.setFlat(False)
        self.black.setObjectName("black")
        self.gridLayout.addWidget(self.black, 1, 1, 1, 1)
        self.matrix = QtGui.QPushButton(demoapp)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.matrix.sizePolicy().hasHeightForWidth())
        self.matrix.setSizePolicy(sizePolicy)
        self.matrix.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/black32/fa-sort-alpha-asc.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.matrix.setIcon(icon7)
        self.matrix.setIconSize(QtCore.QSize(32, 32))
        self.matrix.setAutoDefault(False)
        self.matrix.setFlat(False)
        self.matrix.setObjectName("matrix")
        self.gridLayout.addWidget(self.matrix, 4, 0, 1, 1)
        self.gameoflife = QtGui.QPushButton(demoapp)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gameoflife.sizePolicy().hasHeightForWidth())
        self.gameoflife.setSizePolicy(sizePolicy)
        self.gameoflife.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/black32/fa-globe.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.gameoflife.setIcon(icon8)
        self.gameoflife.setIconSize(QtCore.QSize(32, 32))
        self.gameoflife.setAutoDefault(False)
        self.gameoflife.setFlat(False)
        self.gameoflife.setObjectName("gameoflife")
        self.gridLayout.addWidget(self.gameoflife, 1, 2, 1, 1)

        self.retranslateUi(demoapp)
        QtCore.QMetaObject.connectSlotsByName(demoapp)

    def retranslateUi(self, demoapp):
        demoapp.setWindowTitle(QtGui.QApplication.translate("demoapp", "Demo", None, QtGui.QApplication.UnicodeUTF8))
        self.fade.setText(QtGui.QApplication.translate("demoapp", "Verlauf", None, QtGui.QApplication.UnicodeUTF8))
        self.helix.setText(QtGui.QApplication.translate("demoapp", "Helix", None, QtGui.QApplication.UnicodeUTF8))
        self.wave.setText(QtGui.QApplication.translate("demoapp", "Welle", None, QtGui.QApplication.UnicodeUTF8))
        self.pong.setText(QtGui.QApplication.translate("demoapp", "Pong", None, QtGui.QApplication.UnicodeUTF8))
        self.pulse.setText(QtGui.QApplication.translate("demoapp", "Puls", None, QtGui.QApplication.UnicodeUTF8))
        self.white.setText(QtGui.QApplication.translate("demoapp", "Weiß", None, QtGui.QApplication.UnicodeUTF8))
        self.black.setText(QtGui.QApplication.translate("demoapp", "Schwarz", None, QtGui.QApplication.UnicodeUTF8))
        self.matrix.setText(QtGui.QApplication.translate("demoapp", "Matrix", None, QtGui.QApplication.UnicodeUTF8))
        self.gameoflife.setText(QtGui.QApplication.translate("demoapp", "GoL", None, QtGui.QApplication.UnicodeUTF8))

from . import assets_rc