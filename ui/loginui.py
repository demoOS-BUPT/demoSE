# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(509, 603)
        Dialog.setWindowFlags(Qt.Qt.FramelessWindowHint)
        Dialog.setStyleSheet(_fromUtf8("background-color: rgb(251, 240, 209);"))
        self.UserNamelabel = QtGui.QLabel(Dialog)
        self.UserNamelabel.setGeometry(QtCore.QRect(30, 500, 121, 41))
        self.UserNamelabel.setStyleSheet(_fromUtf8("font: 14pt \"Chiller\";"))
        self.UserNamelabel.setObjectName(_fromUtf8("UserNamelabel"))
        self.Passwdlabel = QtGui.QLabel(Dialog)
        self.Passwdlabel.setGeometry(QtCore.QRect(30, 540, 111, 41))
        self.Passwdlabel.setStyleSheet(_fromUtf8("font: 16pt \"Chiller\";"))
        self.Passwdlabel.setObjectName(_fromUtf8("Passwdlabel"))
        self.UserNamelineEdit = QtGui.QLineEdit(Dialog)
        self.UserNamelineEdit.setGeometry(QtCore.QRect(160, 510, 191, 25))
        self.UserNamelineEdit.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);\n"
"font: 16pt \"Chiller\";"))
        self.UserNamelineEdit.setEchoMode(QtGui.QLineEdit.Normal)
        self.UserNamelineEdit.setObjectName(_fromUtf8("UserNamelineEdit"))
        self.PasslineEdit = QtGui.QLineEdit(Dialog)
        self.PasslineEdit.setGeometry(QtCore.QRect(160, 550, 191, 25))
        self.PasslineEdit.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);\n"
"font: 9pt \"Kristen ITC\";\n"
""))
        self.PasslineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.PasslineEdit.setObjectName(_fromUtf8("PasslineEdit"))
        self.Loginbtn = QtGui.QPushButton(Dialog)
        self.Loginbtn.setGeometry(QtCore.QRect(380, 510, 93, 28))
        self.Loginbtn.setStyleSheet(_fromUtf8("QPushButton { \n"
"background-color: rgb(249, 225, 165);\n"
"selection-background-color: rgb(251, 248, 229);\n"
"font: 16pt \"Chiller\";\n"
"border-radius:12px;\n"
"selection-color: rgb(248, 249, 233);}\n"
"\n"
"QPushButton:hover {\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 0), stop:0.52 rgba(0, 0, 0, 0), stop:0.565 rgba(82, 121, 76, 33), stop:0.65 rgba(159, 235, 148, 64), stop:0.721925 rgba(255, 238, 150, 129), stop:0.77 rgba(255, 128, 128, 204), stop:0.89 rgba(191, 128, 255, 64), stop:1 rgba(0, 0, 0, 0));}\n"
""))
        self.Loginbtn.setObjectName(_fromUtf8("Loginbtn"))
        self.Closebtn = QtGui.QPushButton(Dialog)
        self.Closebtn.setGeometry(QtCore.QRect(380, 550, 93, 28))
        self.Closebtn.setStyleSheet(_fromUtf8("QPushButton{\n"
"background-color: rgb(247, 226, 168);\n"
"font: 16pt \"Chiller\";\n"
"border-radius:12px;\n"
"selection-color: rgb(248, 249, 233);}\n"
"\n"
"QPushButton:hover {\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 0), stop:0.52 rgba(0, 0, 0, 0), stop:0.565 rgba(82, 121, 76, 33), stop:0.65 rgba(159, 235, 148, 64), stop:0.721925 rgba(255, 238, 150, 129), stop:0.77 rgba(255, 128, 128, 204), stop:0.89 rgba(191, 128, 255, 64), stop:1 rgba(0, 0, 0, 0));}\n"
""))
        self.Closebtn.setObjectName(_fromUtf8("Closebtn"))
        self.loginPic = QtGui.QLabel(Dialog)
        self.loginPic.setGeometry(QtCore.QRect(-10, 0, 531, 481))
        self.loginPic.setStyleSheet(_fromUtf8("border-image: url(:/aaa/images/lllll.jpg);"))
        self.loginPic.setText(_fromUtf8(""))
        self.loginPic.setObjectName(_fromUtf8("loginPic"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(140, 10, 241, 31))
        self.label.setStyleSheet(_fromUtf8("font: 24pt \"Chiller\";\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.loginPic.raise_()
        self.UserNamelabel.raise_()
        self.Passwdlabel.raise_()
        self.UserNamelineEdit.raise_()
        self.PasslineEdit.raise_()
        self.Loginbtn.raise_()
        self.Closebtn.raise_()
        self.label.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.UserNamelabel.setText(_translate("Dialog", "<html><head/><body><p align=\"right\"><span style=\" font-size:16pt; font-weight:600;\">room number:</span></p></body></html>", None))
        self.Passwdlabel.setText(_translate("Dialog", "<html><head/><body><p align=\"right\"><span style=\" font-size:14pt; font-weight:600;\">password:</span></p></body></html>", None))
        self.Loginbtn.setText(_translate("Dialog", "login", None))
        self.Closebtn.setText(_translate("Dialog", "cancel", None))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Welcome To Honey Hotel</span></p></body></html>", None))

import loginqrc_rc
