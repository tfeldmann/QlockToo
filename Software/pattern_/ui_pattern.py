# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_pattern.ui'
#
# Created: Thu Mar 21 14:16:15 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_pattern(object):
    def setupUi(self, pattern):
        pattern.setObjectName("pattern")
        pattern.setWindowModality(QtCore.Qt.ApplicationModal)
        pattern.resize(464, 337)
        pattern.setSizeGripEnabled(False)
        self.horizontalLayout = QtGui.QHBoxLayout(pattern)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.draw_area = PatternWidget(pattern)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.draw_area.sizePolicy().hasHeightForWidth())
        self.draw_area.setSizePolicy(sizePolicy)
        self.draw_area.setMinimumSize(QtCore.QSize(300, 300))
        self.draw_area.setAutoFillBackground(False)
        self.draw_area.setObjectName("draw_area")
        self.horizontalLayout.addWidget(self.draw_area)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtGui.QPushButton(pattern)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(pattern)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtGui.QPushButton(pattern)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(pattern)
        QtCore.QMetaObject.connectSlotsByName(pattern)

    def retranslateUi(self, pattern):
        pattern.setWindowTitle(QtGui.QApplication.translate("pattern", "Zeichnen", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("pattern", "Leeren", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("pattern", "Speichern", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("pattern", "Öffnen", None, QtGui.QApplication.UnicodeUTF8))

from patternwidget import PatternWidget

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    pattern = QtGui.QDialog()
    ui = Ui_pattern()
    ui.setupUi(pattern)
    pattern.show()
    sys.exit(app.exec_())

