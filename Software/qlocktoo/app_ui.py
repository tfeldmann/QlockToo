# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './qlocktoo/app.ui'
#
# Created: Wed Dec 25 18:46:36 2013
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_qlocktoo(object):
    def setupUi(self, qlocktoo):
        qlocktoo.setObjectName("qlocktoo")
        qlocktoo.resize(545, 469)
        qlocktoo.setStyleSheet("")
        self.centralwidget = QtGui.QWidget(qlocktoo)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.simulator = Device(self.centralwidget)
        self.simulator.setObjectName("simulator")
        self.verticalLayout_3.addWidget(self.simulator)
        qlocktoo.setCentralWidget(self.centralwidget)
        self.toolBar = QtGui.QToolBar(qlocktoo)
        self.toolBar.setStyleSheet("QToolButton {\n"
"    width: 80px;\n"
"}ss")
        self.toolBar.setMovable(True)
        self.toolBar.setAllowedAreas(QtCore.Qt.AllToolBarAreas)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName("toolBar")
        qlocktoo.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
        self.actionConsole = QtGui.QAction(qlocktoo)
        self.actionConsole.setCheckable(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/black32/fa-terminal.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionConsole.setIcon(icon)
        self.actionConsole.setObjectName("actionConsole")
        self.actionSnake = QtGui.QAction(qlocktoo)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/black32/fa-gamepad.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSnake.setIcon(icon1)
        self.actionSnake.setObjectName("actionSnake")
        self.actionMarquee = QtGui.QAction(qlocktoo)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/black32/fa-text-width.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMarquee.setIcon(icon2)
        self.actionMarquee.setObjectName("actionMarquee")
        self.actionSettings = QtGui.QAction(qlocktoo)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/black32/fa-cogs.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettings.setIcon(icon3)
        self.actionSettings.setObjectName("actionSettings")
        self.actionDemo = QtGui.QAction(qlocktoo)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/black32/fa-th-large.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDemo.setIcon(icon4)
        self.actionDemo.setObjectName("actionDemo")
        self.actionConnect = QtGui.QAction(qlocktoo)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/black32/fa-compress.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionConnect.setIcon(icon5)
        self.actionConnect.setObjectName("actionConnect")
        self.toolBar.addAction(self.actionConnect)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionDemo)
        self.toolBar.addAction(self.actionSnake)
        self.toolBar.addAction(self.actionMarquee)
        self.toolBar.addAction(self.actionSettings)
        self.toolBar.addAction(self.actionConsole)

        self.retranslateUi(qlocktoo)
        QtCore.QMetaObject.connectSlotsByName(qlocktoo)

    def retranslateUi(self, qlocktoo):
        qlocktoo.setWindowTitle(QtGui.QApplication.translate("qlocktoo", "QlockToo", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("qlocktoo", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConsole.setIconText(QtGui.QApplication.translate("qlocktoo", "Konsole", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSnake.setText(QtGui.QApplication.translate("qlocktoo", "Snake", None, QtGui.QApplication.UnicodeUTF8))
        self.actionMarquee.setText(QtGui.QApplication.translate("qlocktoo", "Laufschrift", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSettings.setText(QtGui.QApplication.translate("qlocktoo", "Einstellungen", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDemo.setText(QtGui.QApplication.translate("qlocktoo", "Demo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConnect.setText(QtGui.QApplication.translate("qlocktoo", "Verbinden", None, QtGui.QApplication.UnicodeUTF8))

from device import Device
from . import assets_rc
