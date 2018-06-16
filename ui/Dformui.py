# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dform.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui,Qt

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1150, 690)
        MainWindow.setWindowFlags(Qt.Qt.FramelessWindowHint)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1151, 691))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(_fromUtf8("border-image: url(:/aaa/images/lost7_CaB.jpg);\n"
"font: 10pt \"等线\";\n"
))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.gobackBtn = QtGui.QPushButton(self.centralwidget)
        self.gobackBtn.setGeometry(QtCore.QRect(1060, 630, 61, 41))
        self.gobackBtn.setStyleSheet(_fromUtf8("\n"
"QPushButton { \n"
"background-color: rgb(234, 229, 255);\n"
"    color:rgb(149, 135, 255);\n"
"    \n"
"border-radius:15px;}\n"
"\n"
"QPushButton:hover {\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 255, 125, 255), stop:0.52 rgba(0, 0, 0, 0), stop:0.565 rgba(82, 121, 76, 33), stop:0.65 rgba(159, 235, 148, 64), stop:0.721925 rgba(255, 238, 150, 129), stop:0.77 rgba(255, 128, 128, 204), stop:0.89 rgba(191, 128, 255, 64), stop:1 rgba(0, 0, 0, 0));\n"
"}\n"
"\n"
""))
        self.gobackBtn.setObjectName(_fromUtf8("gobackBtn"))
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 30, 1111, 581))
        self.listWidget.setStyleSheet(_fromUtf8("background-color: rgba(208, 206, 255, 155);"))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
#        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.gobackBtn.setText(_translate("MainWindow", "返回", None))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "我是什么", None))
        self.listWidget.setSortingEnabled(__sortingEnabled)

import loginqrc_rc
