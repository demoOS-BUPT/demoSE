# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
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
        Form.resize(700, 873)
        Form.setWindowFlags(Qt.Qt.FramelessWindowHint)
        self.printBtn = QtGui.QPushButton(Form)
        self.printBtn.setGeometry(QtCore.QRect(210, 130, 93, 131))
        self.printBtn.setStyleSheet(_fromUtf8("QPushButton { \n"
"background-color: rgb(109, 94, 89);\n"
"    font: 75 12pt \"Adobe Arabic\";\n"
"color: rgb(240, 211, 177);\n"
"border-radius:21px;}\n"
"\n"
"QPushButton:hover {\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.9, fx:0.5, fy:0.5, stop:0 rgba(222, 163, 94, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    color: rgb(79, 68, 64);\n"
"}"))
        self.printBtn.setObjectName(_fromUtf8("printBtn"))
        self.dateEdit = QtGui.QDateEdit(Form)
        self.dateEdit.setGeometry(QtCore.QRect(30, 70, 281, 31))
        self.dateEdit.setStyleSheet(_fromUtf8("background-color: rgb(33, 31, 34);\n"
"color: rgb(240, 211, 177);"))
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 10, 281, 41))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setStyleSheet(_fromUtf8("color: rgb(240, 211, 177);\n"
"font: 75 9pt \"Adobe Arabic\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.roomBox = QtGui.QComboBox(self.layoutWidget)
        self.roomBox.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);\n"
"selection-background-color: rgb(30, 28, 31);\n"
"color: rgb(240, 211, 177);"))
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
        self.roomBox.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.roomBox)
        self.calWidget = QtGui.QCalendarWidget(Form)
        self.calWidget.setGeometry(QtCore.QRect(370, 20, 296, 236))
        self.calWidget.setStyleSheet(_fromUtf8("background-color: rgb(50, 48, 49);\n"
"alternate-background-color: rgb(109, 94, 89);\n"
"color: rgb(240, 211, 177);\n"
"selection-background-color: rgb(109, 94, 89);"))
        self.calWidget.setObjectName(_fromUtf8("calWidget"))
        self.tabWidget = QtGui.QTableWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(10, 290, 681, 101))
        self.tabWidget.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(240, 211, 177);"))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabWidget.setColumnCount(0)
        self.tabWidget.setRowCount(0)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 700, 875))
        self.label_2.setStyleSheet(_fromUtf8("border-image: url(:/aaa/images/lost7_night.jpg);"))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.dayBtn = QtGui.QRadioButton(Form)
        self.dayBtn.setGeometry(QtCore.QRect(31, 145, 71, 19))
        self.dayBtn.setStyleSheet(_fromUtf8("color: rgb(240, 211, 177);"))
        self.dayBtn.setObjectName(_fromUtf8("dayBtn"))
        self.monthBtn = QtGui.QRadioButton(Form)
        self.monthBtn.setGeometry(QtCore.QRect(31, 185, 72, 19))
        self.monthBtn.setStyleSheet(_fromUtf8("color: rgb(240, 211, 177);"))
        self.monthBtn.setObjectName(_fromUtf8("monthBtn"))
        self.yearBtn = QtGui.QRadioButton(Form)
        self.yearBtn.setGeometry(QtCore.QRect(31, 225, 72, 19))
        self.yearBtn.setStyleSheet(_fromUtf8("color: rgb(240, 211, 177);"))
        self.yearBtn.setObjectName(_fromUtf8("yearBtn"))
        self.label_2.raise_()
        self.printBtn.raise_()
        self.dateEdit.raise_()
        self.layoutWidget.raise_()
        self.calWidget.raise_()
        self.dayBtn.raise_()
        self.monthBtn.raise_()
        self.yearBtn.raise_()
        self.tabWidget.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.printBtn.setText(_translate("Form", "打印", None))
        self.label.setText(_translate("Form", "房间：", None))
        self.roomBox.setItemText(0, _translate("Form", "全部", None))
        self.roomBox.setItemText(1, _translate("Form", "306C", None))
        self.roomBox.setItemText(2, _translate("Form", "306D", None))
        self.roomBox.setItemText(3, _translate("Form", "307C", None))
        self.roomBox.setItemText(4, _translate("Form", "307D", None))
        self.roomBox.setItemText(5, _translate("Form", "308C", None))
        self.roomBox.setItemText(6, _translate("Form", "308D", None))
        self.roomBox.setItemText(7, _translate("Form", "309C", None))
        self.roomBox.setItemText(8, _translate("Form", "309D", None))
        self.roomBox.setItemText(9, _translate("Form", "310C", None))
        self.dayBtn.setText(_translate("Form", "日报表", None))
        self.monthBtn.setText(_translate("Form", "周报表", None))
        self.yearBtn.setText(_translate("Form", "月报表", None))

import loginqrc_rc
