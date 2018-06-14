# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'checkout.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(415, 568)
        Form.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        Form.setWindowFlags(Qt.Qt.FramelessWindowHint)
        self.commitBtn = QtGui.QPushButton(Form)
        self.commitBtn.setGeometry(QtCore.QRect(40, 510, 91, 28))
        self.commitBtn.setStyleSheet(_fromUtf8("QPushButton {\n"
"    background-color: rgb(214, 214, 214);\n"
"border-radius:12px;}\n"
"\n"
"QPushButton:hover {background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 0), stop:0.52 rgba(0, 0, 0, 0), stop:0.565 rgba(82, 121, 76, 33), stop:0.65 rgba(159, 235, 148, 64), stop:0.721925 rgba(255, 238, 150, 129), stop:0.77 rgba(255, 128, 128, 204), stop:0.89 rgba(191, 128, 255, 64), stop:1 rgba(0, 0, 0, 0));\n"
"}\n"
""))
        self.commitBtn.setObjectName(_fromUtf8("commitBtn"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(-20, 0, 451, 421))
        self.label_3.setStyleSheet(_fromUtf8("border-image: url(:/aaa/images/logiiiin.jpg);"))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.cancelBtn = QtGui.QPushButton(Form)
        self.cancelBtn.setGeometry(QtCore.QRect(280, 510, 91, 28))
        self.cancelBtn.setStyleSheet(_fromUtf8("QPushButton {\n"
"    background-color: rgb(214, 214, 214);\n"
"border-radius:12px;}\n"
"\n"
"QPushButton:hover {background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 0), stop:0.52 rgba(0, 0, 0, 0), stop:0.565 rgba(82, 121, 76, 33), stop:0.65 rgba(159, 235, 148, 64), stop:0.721925 rgba(255, 238, 150, 129), stop:0.77 rgba(255, 128, 128, 204), stop:0.89 rgba(191, 128, 255, 64), stop:1 rgba(0, 0, 0, 0));\n"
"}\n"
""))
        self.cancelBtn.setObjectName(_fromUtf8("cancelBtn"))
        self.gotoDform = QtGui.QPushButton(Form)
        self.gotoDform.setGeometry(QtCore.QRect(160, 510, 91, 28))
        self.gotoDform.setStyleSheet(_fromUtf8("QPushButton {\n"
"    background-color: rgb(214, 214, 214);\n"
"border-radius:12px;}\n"
"\n"
"QPushButton:hover {background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 0), stop:0.52 rgba(0, 0, 0, 0), stop:0.565 rgba(82, 121, 76, 33), stop:0.65 rgba(159, 235, 148, 64), stop:0.721925 rgba(255, 238, 150, 129), stop:0.77 rgba(255, 128, 128, 204), stop:0.89 rgba(191, 128, 255, 64), stop:1 rgba(0, 0, 0, 0));\n"
"}\n"
""))
        self.gotoDform.setObjectName(_fromUtf8("gotoDform"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 460, 61, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.roomBox = QtGui.QComboBox(Form)
        self.roomBox.setGeometry(QtCore.QRect(130, 460, 61, 21))
        self.roomBox.setStyleSheet(_fromUtf8("selection-background-color: rgb(228, 228, 228);"))
        self.roomBox.setObjectName(_fromUtf8("roomBox"))
        self.roomBox.addItem(_fromUtf8(""))
        self.roomBox.addItem(_fromUtf8(""))
        self.roomBox.addItem(_fromUtf8(""))
        self.roomBox.addItem(_fromUtf8(""))
        self.roomBox.addItem(_fromUtf8(""))
        self.roomBox.addItem(_fromUtf8(""))
        self.roomBox.addItem(_fromUtf8(""))
        self.roomBox.addItem(_fromUtf8(""))
        self.roomBox.addItem(_fromUtf8(""))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(244, 460, 71, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.priceLab = QtGui.QLabel(Form)
        self.priceLab.setGeometry(QtCore.QRect(320, 460, 61, 21))
        self.priceLab.setStyleSheet(_fromUtf8(""))
        self.priceLab.setText(_fromUtf8(""))
        self.priceLab.setObjectName(_fromUtf8("priceLab"))
        self.commitBtn.raise_()
        self.label_3.raise_()
        self.cancelBtn.raise_()
        self.gotoDform.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.commitBtn.setText(_translate("Form", "退房咯", None))
        self.cancelBtn.setText(_translate("Form", "返回", None))
        self.gotoDform.setText(_translate("Form", "查看详单", None))
        self.label.setText(_translate("Form", "房间号：", None))
        self.roomBox.setItemText(0, _translate("Form", "306C", None))
        self.roomBox.setItemText(1, _translate("Form", "306D", None))
        self.roomBox.setItemText(2, _translate("Form", "307C", None))
        self.roomBox.setItemText(3, _translate("Form", "307D", None))
        self.roomBox.setItemText(4, _translate("Form", "308C", None))
        self.roomBox.setItemText(5, _translate("Form", "308D", None))
        self.roomBox.setItemText(6, _translate("Form", "309C", None))
        self.roomBox.setItemText(7, _translate("Form", "309D", None))
        self.roomBox.setItemText(8, _translate("Form", "310C", None))
        self.label_2.setText(_translate("Form", "消费金额：", None))

import loginqrc_rc
