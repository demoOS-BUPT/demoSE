# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'checkout.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(431, 554)
        Form.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.commitBtn = QtGui.QPushButton(Form)
        self.commitBtn.setGeometry(QtCore.QRect(310, 460, 91, 28))
        self.commitBtn.setStyleSheet(_fromUtf8("QPushButton {\n"
"    background-color: rgb(214, 214, 214);\n"
"border-radius:12px;}\n"
"\n"
"QPushButton:hover {background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 0), stop:0.52 rgba(0, 0, 0, 0), stop:0.565 rgba(82, 121, 76, 33), stop:0.65 rgba(159, 235, 148, 64), stop:0.721925 rgba(255, 238, 150, 129), stop:0.77 rgba(255, 128, 128, 204), stop:0.89 rgba(191, 128, 255, 64), stop:1 rgba(0, 0, 0, 0));\n"
"}\n"
""))
        self.commitBtn.setObjectName(_fromUtf8("commitBtn"))
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 460, 231, 71))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.roomBox = QtGui.QComboBox(self.layoutWidget)
        self.roomBox.setStyleSheet(_fromUtf8("selection-background-color: rgb(228, 228, 228);"))
        self.roomBox.setObjectName(_fromUtf8("roomBox"))
        self.roomBox.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.roomBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.priceLab = QtGui.QLabel(self.layoutWidget)
        self.priceLab.setText(_fromUtf8(""))
        self.priceLab.setObjectName(_fromUtf8("priceLab"))
        self.horizontalLayout_2.addWidget(self.priceLab)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(-20, 0, 451, 421))
        self.label_3.setStyleSheet(_fromUtf8("border-image: url(:/aaa/images/logiiiin.jpg);"))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.cancelBtn = QtGui.QPushButton(Form)
        self.cancelBtn.setGeometry(QtCore.QRect(310, 500, 91, 28))
        self.cancelBtn.setStyleSheet(_fromUtf8("QPushButton {\n"
"    background-color: rgb(214, 214, 214);\n"
"border-radius:12px;}\n"
"\n"
"QPushButton:hover {background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 0), stop:0.52 rgba(0, 0, 0, 0), stop:0.565 rgba(82, 121, 76, 33), stop:0.65 rgba(159, 235, 148, 64), stop:0.721925 rgba(255, 238, 150, 129), stop:0.77 rgba(255, 128, 128, 204), stop:0.89 rgba(191, 128, 255, 64), stop:1 rgba(0, 0, 0, 0));\n"
"}\n"
""))
        self.cancelBtn.setObjectName(_fromUtf8("cancelBtn"))
        self.layoutWidget.raise_()
        self.commitBtn.raise_()
        self.label_3.raise_()
        self.cancelBtn.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.commitBtn.setText(_translate("Form", "退房咯", None))
        self.label.setText(_translate("Form", "房间号：", None))
        self.roomBox.setItemText(0, _translate("Form", "307C", None))
        self.label_2.setText(_translate("Form", "消费金额：", None))
        self.cancelBtn.setText(_translate("Form", "不退咯", None))

import loginqrc_rc
