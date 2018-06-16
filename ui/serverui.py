# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'server.ui'
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

class Ui_Serverui(object):
    def setupUi(self, Serverui):
        Serverui.setObjectName(_fromUtf8("Serverui"))
        Serverui.resize(960, 963)
        self.frame = QtGui.QFrame(Serverui)
        self.frame.setGeometry(QtCore.QRect(0, 10, 131, 31))
        self.frame.setStyleSheet(_fromUtf8("color:rgb(185, 223, 244);"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.display = QtGui.QLabel(Serverui)
        self.display.setGeometry(QtCore.QRect(410, 10, 331, 41))
        self.display.setStyleSheet(_fromUtf8("color:rgb(185, 223, 244);"))
        self.display.setText(_fromUtf8(""))
        self.display.setObjectName(_fromUtf8("display"))
        self.layoutWidget = QtGui.QWidget(Serverui)
        self.layoutWidget.setGeometry(QtCore.QRect(130, 120, 711, 171))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.C306Lab = QtGui.QLabel(self.layoutWidget)
        self.C306Lab.setStyleSheet(_fromUtf8("color:rgb(185, 223, 244);"))
        self.C306Lab.setObjectName(_fromUtf8("C306Lab"))
        self.horizontalLayout_2.addWidget(self.C306Lab)
        self.D306Lab = QtGui.QLabel(self.layoutWidget)
        self.D306Lab.setStyleSheet(_fromUtf8("color:rgb(185, 223, 244);"))
        self.D306Lab.setObjectName(_fromUtf8("D306Lab"))
        self.horizontalLayout_2.addWidget(self.D306Lab)
        self.C307Lab = QtGui.QLabel(self.layoutWidget)
        self.C307Lab.setStyleSheet(_fromUtf8("color:rgb(185, 223, 244);"))
        self.C307Lab.setObjectName(_fromUtf8("C307Lab"))
        self.horizontalLayout_2.addWidget(self.C307Lab)
        self.serverLab = QtGui.QLabel(Serverui)
        self.serverLab.setGeometry(QtCore.QRect(690, -20, 171, 141))
        self.serverLab.setObjectName(_fromUtf8("serverLab"))
        self.onBtn = QtGui.QPushButton(Serverui)
        self.onBtn.setGeometry(QtCore.QRect(450, 770, 101, 51))
        self.onBtn.setStyleSheet(_fromUtf8("QPushButton { \n"
"font: 75 14pt \"Adobe Arabic\";\n"
"    color: rgb(41, 69, 69);\n"
"    background-color: rgb(142, 136, 144);\n"
"border-radius:25px;}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.9, fx:0.5, fy:0.5, stop:0 rgba(0, 41, 71, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    color: rgb(231, 240, 248);\n"
"}"))
        self.onBtn.setObjectName(_fromUtf8("onBtn"))
        self.layoutWidget_2 = QtGui.QWidget(Serverui)
        self.layoutWidget_2.setGeometry(QtCore.QRect(130, 290, 711, 171))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.D308Lab = QtGui.QLabel(self.layoutWidget_2)
        self.D308Lab.setStyleSheet(_fromUtf8("color:rgb(185, 223, 244);"))
        self.D308Lab.setObjectName(_fromUtf8("D308Lab"))
        self.horizontalLayout_4.addWidget(self.D308Lab)
        self.D307Lab = QtGui.QLabel(self.layoutWidget_2)
        self.D307Lab.setStyleSheet(_fromUtf8("color:rgb(185, 223, 244);"))
        self.D307Lab.setObjectName(_fromUtf8("D307Lab"))
        self.horizontalLayout_4.addWidget(self.D307Lab)
        self.C308Lab = QtGui.QLabel(self.layoutWidget_2)
        self.C308Lab.setStyleSheet(_fromUtf8("color:rgb(185, 223, 244);"))
        self.C308Lab.setObjectName(_fromUtf8("C308Lab"))
        self.horizontalLayout_4.addWidget(self.C308Lab)
        self.layoutWidget_3 = QtGui.QWidget(Serverui)
        self.layoutWidget_3.setGeometry(QtCore.QRect(130, 460, 711, 171))
        self.layoutWidget_3.setObjectName(_fromUtf8("layoutWidget_3"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.C309Lab = QtGui.QLabel(self.layoutWidget_3)
        self.C309Lab.setStyleSheet(_fromUtf8("color:rgb(185, 223, 244);"))
        self.C309Lab.setObjectName(_fromUtf8("C309Lab"))
        self.horizontalLayout_5.addWidget(self.C309Lab)
        self.D309Lab = QtGui.QLabel(self.layoutWidget_3)
        self.D309Lab.setStyleSheet(_fromUtf8("color:rgb(185, 223, 244);"))
        self.D309Lab.setObjectName(_fromUtf8("D309Lab"))
        self.horizontalLayout_5.addWidget(self.D309Lab)
        self.C310Lab = QtGui.QLabel(self.layoutWidget_3)
        self.C310Lab.setStyleSheet(_fromUtf8("color:rgb(185, 223, 244);"))
        self.C310Lab.setObjectName(_fromUtf8("C310Lab"))
        self.horizontalLayout_5.addWidget(self.C310Lab)
        self.serverPic = QtGui.QLabel(Serverui)
        self.serverPic.setGeometry(QtCore.QRect(0, -90, 971, 1191))
        self.serverPic.setStyleSheet(_fromUtf8("border-image: url(:/aaa/images/server.gif);"))
        self.serverPic.setText(_fromUtf8(""))
        self.serverPic.setObjectName(_fromUtf8("serverPic"))
        self.setBtn = QtGui.QPushButton(Serverui)
        self.setBtn.setGeometry(QtCore.QRect(570, 910, 71, 41))
        self.setBtn.setStyleSheet(_fromUtf8("QPushButton { \n"
"font: 9pt \"Adobe Arabic\";\n"
"    color: rgb(41, 69, 69);\n"
"background-color: rgb(181, 173, 173);\n"
"border-radius:18px;}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(5, 54, 71, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}"))
        self.setBtn.setObjectName(_fromUtf8("setBtn"))
        self.checkoutBtn = QtGui.QPushButton(Serverui)
        self.checkoutBtn.setEnabled(True)
        self.checkoutBtn.setGeometry(QtCore.QRect(310, 860, 71, 41))
        self.checkoutBtn.setStyleSheet(_fromUtf8("QPushButton { \n"
"font: 9pt \"Adobe Arabic\";\n"
"    color: rgb(41, 69, 69);\n"
"background-color: rgb(181, 173, 173);\n"
"border-radius:18px;}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(5, 54, 71, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}"))
        self.checkoutBtn.setObjectName(_fromUtf8("checkoutBtn"))
        self.formBtn = QtGui.QPushButton(Serverui)
        self.formBtn.setGeometry(QtCore.QRect(420, 910, 71, 41))
        self.formBtn.setStyleSheet(_fromUtf8("QPushButton { \n"
"font: 9pt \"Adobe Arabic\";\n"
"    color: rgb(41, 69, 69);\n"
"    background-color: rgb(167, 165, 165);\n"
"border-radius:18px;}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(5, 54, 71, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}"))
        self.formBtn.setObjectName(_fromUtf8("formBtn"))
        self.serverPic.raise_()
        self.setBtn.raise_()
        self.checkoutBtn.raise_()
        self.formBtn.raise_()
        self.frame.raise_()
        self.display.raise_()
        self.serverLab.raise_()
        self.onBtn.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget_2.raise_()
        self.layoutWidget_3.raise_()

        self.retranslateUi(Serverui)
        QtCore.QMetaObject.connectSlotsByName(Serverui)

    def retranslateUi(self, Serverui):
        Serverui.setWindowTitle(_translate("Serverui", "Dialog", None))
        self.C306Lab.setText(_translate("Serverui", "306C房间", None))
        self.D306Lab.setText(_translate("Serverui", "306D房间", None))
        self.C307Lab.setText(_translate("Serverui", "307C房间", None))
        self.serverLab.setText(_translate("Serverui", "<html><head/><body><p><br/></p></body></html>", None))
        self.onBtn.setText(_translate("Serverui", "开", None))
        self.D308Lab.setText(_translate("Serverui", "308D房间", None))
        self.D307Lab.setText(_translate("Serverui", "307D房间", None))
        self.C308Lab.setText(_translate("Serverui", "308C房间", None))
        self.C309Lab.setText(_translate("Serverui", "309C房间", None))
        self.D309Lab.setText(_translate("Serverui", "309D房间", None))
        self.C310Lab.setText(_translate("Serverui", "310C房间", None))
        self.setBtn.setText(_translate("Serverui", "设置", None))
        self.checkoutBtn.setText(_translate("Serverui", "退房", None))
        self.formBtn.setText(_translate("Serverui", "报表", None))

import loginqrc_rc
