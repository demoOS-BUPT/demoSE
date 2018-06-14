# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setRate.ui'
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
        Form.setWindowFlags(Qt.Qt.FramelessWindowHint)
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(598, 793)
        Form.setStyleSheet(_fromUtf8(""))
        self.commitBtn = QtGui.QPushButton(Form)
        self.commitBtn.setGeometry(QtCore.QRect(410, 630, 111, 41))
        self.commitBtn.setStyleSheet(_fromUtf8("QPushButton { \n"
"background-color: rgb(7, 94, 85);\n"
"color: rgb(246, 246, 200);\n"
"border-radius:16px;}\n"
"\n"
"QPushButton:hover {\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 255, 125, 255), stop:0.52 rgba(0, 0, 0, 0), stop:0.565 rgba(82, 121, 76, 33), stop:0.65 rgba(159, 235, 148, 64), stop:0.721925 rgba(255, 238, 150, 129), stop:0.77 rgba(255, 128, 128, 204), stop:0.89 rgba(191, 128, 255, 64), stop:1 rgba(0, 0, 0, 0));}\n"
""))
        self.commitBtn.setObjectName(_fromUtf8("commitBtn"))
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 570, 341, 221))
        self.tabWidget.setStyleSheet(_fromUtf8("background-color: rgb(239, 247, 247);"))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.highRateEdit = QtGui.QLineEdit(self.tab)
        self.highRateEdit.setGeometry(QtCore.QRect(100, 130, 171, 31))
        self.highRateEdit.setObjectName(_fromUtf8("highRateEdit"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(40, 50, 41, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(30, 20, 72, 15))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lowRateEdit = QtGui.QLineEdit(self.tab)
        self.lowRateEdit.setGeometry(QtCore.QRect(100, 50, 171, 31))
        self.lowRateEdit.setObjectName(_fromUtf8("lowRateEdit"))
        self.midRateEdit = QtGui.QLineEdit(self.tab)
        self.midRateEdit.setGeometry(QtCore.QRect(100, 90, 171, 31))
        self.midRateEdit.setObjectName(_fromUtf8("midRateEdit"))
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(40, 130, 51, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 51, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.setRatePic = QtGui.QLabel(Form)
        self.setRatePic.setGeometry(QtCore.QRect(0, 0, 600, 591))

        #------------lx
        self.setRatePic.setScaledContents(True)
        setRatePic = QtGui.QMovie("./images/lost7_boy.gif") 
        #设置cacheMode为CacheAll时表示gif无限循环，注意此时loopCount()返回-1
        setRatePic.setCacheMode(QtGui.QMovie.CacheAll) 
        #播放速度
        setRatePic.setSpeed(100) 
        #self.movie_screen是在qt designer里定义的一个QLabel对象的对象名，将gif显示在label上
        self.setRatePic.setMovie(setRatePic)   
        #开始播放，对应的是movie.start()
        setRatePic.start()

        
        self.setRatePic.setText(_fromUtf8(""))
        self.setRatePic.setObjectName(_fromUtf8("setRatePic"))
        self.bgWhite = QtGui.QLabel(Form)
        self.bgWhite.setGeometry(QtCore.QRect(1, 574, 601, 221))
        self.bgWhite.setStyleSheet(_fromUtf8("background-color: rgb(239, 247, 247);"))
        self.bgWhite.setObjectName(_fromUtf8("bgWhite"))
        self.cancel = QtGui.QPushButton(Form)
        self.cancel.setGeometry(QtCore.QRect(410, 710, 111, 41))
        self.cancel.setStyleSheet(_fromUtf8("QPushButton { \n"
"background-color: rgb(35, 133, 91);\n"
"color: rgb(246, 246, 200);\n"
"border-radius:16px;}\n"
"\n"
"QPushButton:hover {\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 255, 125, 255), stop:0.52 rgba(0, 0, 0, 0), stop:0.565 rgba(82, 121, 76, 33), stop:0.65 rgba(159, 235, 148, 64), stop:0.721925 rgba(255, 238, 150, 129), stop:0.77 rgba(255, 128, 128, 204), stop:0.89 rgba(191, 128, 255, 64), stop:1 rgba(0, 0, 0, 0));}\n"
""))
        self.cancel.setObjectName(_fromUtf8("cancel"))
        self.bgWhite.raise_()
        self.setRatePic.raise_()
        self.commitBtn.raise_()
        self.tabWidget.raise_()
        self.cancel.raise_()

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.commitBtn.setText(_translate("Form", "提交", None))
        self.label.setText(_translate("Form", "低风", None))
        self.label_4.setText(_translate("Form", "设置费率", None))
        self.label_3.setText(_translate("Form", "高风", None))
        self.label_2.setText(_translate("Form", "中风", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "设置电率", None))
        self.bgWhite.setText(_translate("Form", "TextLabel", None))
        self.cancel.setText(_translate("Form", "返回", None))

import loginqrc_rc
