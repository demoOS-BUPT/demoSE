# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName(_fromUtf8("Login"))
        Login.resize(401, 460)
        Login.setStyleSheet(_fromUtf8("background-color: rgb(251, 240, 209);"))
        self.UserNamelabel = QtGui.QLabel(Login)
        self.UserNamelabel.setGeometry(QtCore.QRect(10, 380, 121, 21))
        self.UserNamelabel.setStyleSheet(_fromUtf8("font: 9pt \"Kristen ITC\";"))
        self.UserNamelabel.setObjectName(_fromUtf8("UserNamelabel"))
        self.Passwdlabel = QtGui.QLabel(Login)
        self.Passwdlabel.setGeometry(QtCore.QRect(10, 420, 101, 21))
        self.Passwdlabel.setStyleSheet(_fromUtf8("font: 9pt \"Kristen ITC\";"))
        self.Passwdlabel.setObjectName(_fromUtf8("Passwdlabel"))
        self.UserNamelineEdit = QtGui.QLineEdit(Login)
        self.UserNamelineEdit.setGeometry(QtCore.QRect(130, 380, 131, 25))
        self.UserNamelineEdit.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);\n"
"font: 9pt \"Kristen ITC\";"))
        self.UserNamelineEdit.setEchoMode(QtGui.QLineEdit.Normal)
        self.UserNamelineEdit.setObjectName(_fromUtf8("UserNamelineEdit"))
        self.PasslineEdit = QtGui.QLineEdit(Login)
        self.PasslineEdit.setGeometry(QtCore.QRect(140, 420, 121, 25))
        self.PasslineEdit.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);\n"
"font: 9pt \"Kristen ITC\";\n"
""))
        self.PasslineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.PasslineEdit.setObjectName(_fromUtf8("PasslineEdit"))
        self.Loginbtn = QtGui.QPushButton(Login)
        self.Loginbtn.setGeometry(QtCore.QRect(290, 380, 93, 28))
        self.Loginbtn.setStyleSheet(_fromUtf8("background-color: rgb(249, 225, 165);\n"
"font: 9pt \"Kristen ITC\";\n"
"border-radius:12px;\n"
"selection-color: rgb(244, 240, 216);"))
        self.Loginbtn.setObjectName(_fromUtf8("Loginbtn"))
        self.Closebtn = QtGui.QPushButton(Login)
        self.Closebtn.setGeometry(QtCore.QRect(290, 420, 93, 28))
        self.Closebtn.setStyleSheet(_fromUtf8("background-color: rgb(247, 226, 168);\n"
"font: 9pt \"Kristen ITC\";\n"
"border-radius:12px;\n"
"selection-color: rgb(244, 240, 216);"))
        self.Closebtn.setObjectName(_fromUtf8("Closebtn"))
        self.loginPic = QtGui.QLabel(Login)
        self.loginPic.setGeometry(QtCore.QRect(-10, -10, 411, 371))
        self.loginPic.setStyleSheet(_fromUtf8(""))
        self.loginPic.setText(_fromUtf8(""))
        self.loginPic.setObjectName(_fromUtf8("loginPic"))
        self.loginPic.raise_()
        self.UserNamelabel.raise_()
        self.Passwdlabel.raise_()
        self.UserNamelineEdit.raise_()
        self.PasslineEdit.raise_()
        self.Loginbtn.raise_()
        self.Closebtn.raise_()

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        Login.setWindowTitle(_translate("Login", "Login", None))
        self.UserNamelabel.setText(_translate("Login", "<html><head/><body><p>room number:</p></body></html>", None))
        self.Passwdlabel.setText(_translate("Login", "<html><head/><body><p><span style=\" font-size:10pt;\">password:</span></p></body></html>", None))
        self.Loginbtn.setText(_translate("Login", "login", None))
        self.Closebtn.setText(_translate("Login", "cancel", None))



