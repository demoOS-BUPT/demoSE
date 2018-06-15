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
        MainWindow.resize(795, 809)
        MainWindow.setWindowFlags(Qt.Qt.FramelessWindowHint)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 1051))
       #------------lx
        
        self.label.setScaledContents(True)
        label = QtGui.QMovie("./images/lost7_dogie.gif") 
        #设置cacheMode为CacheAll时表示gif无限循环，注意此时loopCount()返回-1
        label.setCacheMode(QtGui.QMovie.CacheAll) 
        #播放速度
        label.setSpeed(100) 
        #self.movie_screen是在qt designer里定义的一个QLabel对象的对象名，将gif显示在label上
        self.label.setMovie(label)   
        #开始播放，对应的是movie.start()
        label.start()
        
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 30, 751, 431))
        self.tableWidget.setStyleSheet(_fromUtf8("background-color: rgba(184, 215, 255, 0);\n"
"color: rgb(45, 91, 90);\n"
"font: 75 9pt \"Adobe Arabic\";\n"
"alternate-background-color: rgb(93, 178, 134);\n"
"selection-background-color: rgb(48, 115, 90);\n"
"gridline-color: rgb(44, 99, 85);\n"))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        
        item = QtGui.QTableWidgetItem()
        item.setBackground(QtGui.QColor(255, 255, 255, 0))
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.gobackBtn = QtGui.QPushButton(self.centralwidget)
        self.gobackBtn.setGeometry(QtCore.QRect(20, 740, 61, 41))
        self.gobackBtn.setStyleSheet(_fromUtf8("QPushButton { \n"
"background-color: rgb(41, 93, 91);\n"
"    color: rgb(209, 211, 184);\n"
"border-radius:15px;}\n"
"\n"
"QPushButton:hover {\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 255, 125, 255), stop:0.52 rgba(0, 0, 0, 0), stop:0.565 rgba(82, 121, 76, 33), stop:0.65 rgba(159, 235, 148, 64), stop:0.721925 rgba(255, 238, 150, 129), stop:0.77 rgba(255, 128, 128, 204), stop:0.89 rgba(191, 128, 255, 64), stop:1 rgba(0, 0, 0, 0));\n"
"}\n"
"\n"
""))
        self.gobackBtn.setObjectName(_fromUtf8("gobackBtn"))
       #MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.gobackBtn.setText(_translate("MainWindow", "返回", None))

import loginqrc_rc
