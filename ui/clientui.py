# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client.ui'
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
        MainWindow.resize(1155, 771)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(16, 132, 134);"))
        MainWindow.setWindowFlags(Qt.Qt.FramelessWindowHint)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.oBtn = QtGui.QPushButton(self.centralWidget)
        self.oBtn.setGeometry(QtCore.QRect(920, 640, 181, 91))
        self.oBtn.setStyleSheet(_fromUtf8("QPushButton { \n"
"font: 9pt \"幼圆\";\n"
"    font: 75 18pt \"Adobe Arabic\";\n"
"    color: rgb(51, 97, 175);\n"
"    background-color: rgb(154, 227, 245);\n"
"border-radius:25px;}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.228856 rgba(18, 182, 184, 255), stop:1 rgba(255, 255, 255, 200));}\n"
"\n"
""))
        self.oBtn.setObjectName(_fromUtf8("oBtn"))
        self.winFrame = QtGui.QFrame(self.centralWidget)
        self.winFrame.setGeometry(QtCore.QRect(110, 640, 361, 43))
        self.winFrame.setStyleSheet(_fromUtf8("border-radius:25px;\n"
"background-color: rgb(16, 148, 153);"))
        self.winFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.winFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.winFrame.setObjectName(_fromUtf8("winFrame"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.winFrame)
        self.horizontalLayout_2.setMargin(11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lowBtn = QtGui.QRadioButton(self.winFrame)
        self.lowBtn.setStyleSheet(_fromUtf8("color:#99e2f4;"))
        self.lowBtn.setChecked(True)
        self.lowBtn.setObjectName(_fromUtf8("lowBtn"))
        self.horizontalLayout_2.addWidget(self.lowBtn)
        self.midBtn = QtGui.QRadioButton(self.winFrame)
        self.midBtn.setStyleSheet(_fromUtf8("color:#99e2f4;"))
        self.midBtn.setObjectName(_fromUtf8("midBtn"))
        self.horizontalLayout_2.addWidget(self.midBtn)
        self.highBtn = QtGui.QRadioButton(self.winFrame)
        self.highBtn.setStyleSheet(_fromUtf8("color:#99e2f4;"))
        self.highBtn.setObjectName(_fromUtf8("highBtn"))
        self.horizontalLayout_2.addWidget(self.highBtn)
        self.tabWidget = QtGui.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(50, 230, 461, 251))
        self.tabWidget.setStyleSheet(_fromUtf8("background-color: rgb(39, 96, 99);"))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.stateTab = QtGui.QWidget()
        self.stateTab.setObjectName(_fromUtf8("stateTab"))
        self.showLab = QtGui.QLabel(self.stateTab)
        self.showLab.setGeometry(QtCore.QRect(11, 11, 431, 201))
        self.showLab.setStyleSheet(_fromUtf8("background-color: rgb(39, 90, 92);color:#99e2f4;"))
        self.showLab.setObjectName(_fromUtf8("showLab"))
        self.tabWidget.addTab(self.stateTab, _fromUtf8(""))
        self.billTab = QtGui.QWidget()
        self.billTab.setObjectName(_fromUtf8("billTab"))
        self.billLab = QtGui.QLabel(self.billTab)
        self.billLab.setGeometry(QtCore.QRect(20, 20, 411, 191))
        self.billTab.setStyleSheet(_fromUtf8("background-color: rgb(39, 90, 92);color:#99e2f4;"))
        self.billLab.setText(_fromUtf8(""))
        self.billLab.setObjectName(_fromUtf8("billLab"))
        self.tabWidget.addTab(self.billTab, _fromUtf8(""))
        self.condiTab = QtGui.QWidget()
        self.condiTab.setObjectName(_fromUtf8("condiTab"))
        self.textEdit = QtGui.QTextEdit(self.condiTab)
        self.textEdit.setGeometry(QtCore.QRect(20, 20, 411, 191))
        self.textEdit.setStyleSheet(_fromUtf8("background-color: rgb(39, 90, 92);"))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.tabWidget.addTab(self.condiTab, _fromUtf8(""))
        self.layoutWidget = QtGui.QWidget(self.centralWidget)
        self.layoutWidget.setGeometry(QtCore.QRect(110, 570, 361, 51))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.aimtemLabel = QtGui.QLabel(self.layoutWidget)
        self.aimtemLabel.setStyleSheet(_fromUtf8("color:#99e2f4;\n"
"background-color: rgb(16, 148, 153);"))
        self.aimtemLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.aimtemLabel.setObjectName(_fromUtf8("aimtemLabel"))
        self.horizontalLayout.addWidget(self.aimtemLabel)
        self.temperaBox = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.temperaBox.setStyleSheet(_fromUtf8("color:#99e2f4;\n"
"background-color: rgb(16, 148, 153);"))
        self.temperaBox.setMinimum(15.0)
        self.temperaBox.setMaximum(30.0)
        self.temperaBox.setProperty("value", 26.0)
        self.temperaBox.setObjectName(_fromUtf8("temperaBox"))
        self.horizontalLayout.addWidget(self.temperaBox)
        self.tempSlider = QtGui.QSlider(self.centralWidget)
        self.tempSlider.setGeometry(QtCore.QRect(70, 570, 21, 121))
        self.tempSlider.setStyleSheet(_fromUtf8("color:#99e2f4;\n"
"background-color: rgb(16, 148, 153);\n"
"border-radius:25px;"))
        self.tempSlider.setOrientation(QtCore.Qt.Vertical)
        self.tempSlider.setObjectName(_fromUtf8("tempSlider"))
        self.clientPic = QtGui.QLabel(self.centralWidget)
        self.clientPic.setGeometry(QtCore.QRect(0, 0, 1161, 931))
         #------------lx
        
        self.clientPic.setScaledContents(True)
        clientPic = QtGui.QMovie("./images/lost7_sleep.gif") 
        #设置cacheMode为CacheAll时表示gif无限循环，注意此时loopCount()返回-1
        clientPic.setCacheMode(QtGui.QMovie.CacheAll) 
        #播放速度
        clientPic.setSpeed(100) 
        #self.movie_screen是在qt designer里定义的一个QLabel对象的对象名，将gif显示在label上
        self.clientPic.setMovie(clientPic)   
        #开始播放，对应的是movie.start()
        clientPic.start()
        
        self.clientPic.setText(_fromUtf8(""))
        self.clientPic.setObjectName(_fromUtf8("clientPic"))
        self.tipLabel = QtGui.QLabel(self.centralWidget)
        self.tipLabel.setGeometry(QtCore.QRect(70, 520, 411, 31))
        self.tipLabel.setStyleSheet(_fromUtf8("background-color: rgb(16, 148, 153);\n"
"border-radius:35px;\n"
"color:#99e2f4;"))
        self.tipLabel.setText(_fromUtf8(""))
        self.tipLabel.setObjectName(_fromUtf8("tipLabel"))
        self.roomLabel = QtGui.QLabel(self.centralWidget)
        self.roomLabel.setGeometry(QtCore.QRect(470, 160, 241, 61))
        self.roomLabel.setStyleSheet(_fromUtf8("\n"
"background-color: rgba(255, 255, 255, 0);color:#99e2f4;"))
        self.roomLabel.setText(_fromUtf8(""))
        self.roomLabel.setObjectName(_fromUtf8("roomLabel"))
        self.clientPic.raise_()
        self.oBtn.raise_()
        self.winFrame.raise_()
        self.tabWidget.raise_()
        self.layoutWidget.raise_()
        self.tempSlider.raise_()
        self.tipLabel.raise_()
        self.roomLabel.raise_()
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.oBtn.setText(_translate("MainWindow", "开机", None))
        self.lowBtn.setText(_translate("MainWindow", "低风", None))
        self.midBtn.setText(_translate("MainWindow", "中风", None))
        self.highBtn.setText(_translate("MainWindow", "高风", None))
        self.showLab.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#92d5ef;\">主人没开机呢，我该显示些什么呢</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.stateTab), _translate("MainWindow", "房间状态", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.billTab), _translate("MainWindow", "账单", None))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#9ae1f4;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#9ae1f4;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#9ae1f4;\">亲，如果空调出现任何问题请咨询我们的管理员：yifei@bupt.com</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; font-weight:600; color:#9ae1f4;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#9ae1f4;\">如果不会使用我们的空调请咨询(￣ˇ￣)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#9ae1f4;\">emmmm....等我去注册个邮箱先昂~</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.condiTab), _translate("MainWindow", "空调使用手册", None))
        self.aimtemLabel.setText(_translate("MainWindow", "目标温度：", None))

import loginqrc_rc
