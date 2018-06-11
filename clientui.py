# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        # 开始装载样式表
        qss_file = open('clientQSS.qss').read()
        MainWindow.setStyleSheet(qss_file)

        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(507, 759)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.oBtn = QtGui.QPushButton(self.centralWidget)
        self.oBtn.setGeometry(QtCore.QRect(380, 20, 101, 91))
        self.oBtn.setObjectName(_fromUtf8("oBtn"))
        self.winFrame = QtGui.QFrame(self.centralWidget)
        self.winFrame.setGeometry(QtCore.QRect(50, 190, 209, 43))
        self.winFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.winFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.winFrame.setObjectName(_fromUtf8("winFrame"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.winFrame)
        self.horizontalLayout_2.setMargin(11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lowBtn = QtGui.QRadioButton(self.winFrame)
        self.lowBtn.setChecked(True)
        self.lowBtn.setObjectName(_fromUtf8("lowBtn"))
        self.horizontalLayout_2.addWidget(self.lowBtn)
        self.midBtn = QtGui.QRadioButton(self.winFrame)
        self.midBtn.setObjectName(_fromUtf8("midBtn"))
        self.horizontalLayout_2.addWidget(self.midBtn)
        self.highBtn = QtGui.QRadioButton(self.winFrame)
        self.highBtn.setObjectName(_fromUtf8("highBtn"))
        self.horizontalLayout_2.addWidget(self.highBtn)
        self.tabWidget = QtGui.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 280, 451, 421))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.stateTab = QtGui.QWidget()
        self.stateTab.setObjectName(_fromUtf8("stateTab"))
        self.showLab = QtGui.QLabel(self.stateTab)
        self.showLab.setGeometry(QtCore.QRect(30, 30, 331, 201))
        self.showLab.setObjectName(_fromUtf8("showLab"))
        self.tabWidget.addTab(self.stateTab, _fromUtf8(""))
        self.billTab = QtGui.QWidget()
        self.billTab.setObjectName(_fromUtf8("billTab"))
        self.billLab = QtGui.QLabel(self.billTab)
        self.billLab.setGeometry(QtCore.QRect(40, 40, 351, 301))
        self.billLab.setText(_fromUtf8(""))
        self.billLab.setObjectName(_fromUtf8("billLab"))
        self.tabWidget.addTab(self.billTab, _fromUtf8(""))
        self.condiTab = QtGui.QWidget()
        self.condiTab.setObjectName(_fromUtf8("condiTab"))
        self.textEdit = QtGui.QTextEdit(self.condiTab)
        self.textEdit.setGeometry(QtCore.QRect(30, 70, 361, 251))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.tabWidget.addTab(self.condiTab, _fromUtf8(""))
        self.layoutWidget = QtGui.QWidget(self.centralWidget)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 100, 191, 51))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.aimtemLabel = QtGui.QLabel(self.layoutWidget)
        self.aimtemLabel.setFrameShadow(QtGui.QFrame.Plain)
        self.aimtemLabel.setObjectName(_fromUtf8("aimtemLabel"))
        self.horizontalLayout.addWidget(self.aimtemLabel)
        self.temperaBox = QtGui.QDoubleSpinBox(self.layoutWidget)
        self.temperaBox.setMinimum(15.0)
        self.temperaBox.setMaximum(30.0)
        self.temperaBox.setProperty("value", 26.0)
        self.temperaBox.setObjectName(_fromUtf8("temperaBox"))
        self.horizontalLayout.addWidget(self.temperaBox)
        self.layoutWidget1 = QtGui.QWidget(self.centralWidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(250, 100, 101, 65))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setMargin(11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.commitBtn = QtGui.QPushButton(self.layoutWidget1)
        self.commitBtn.setObjectName(_fromUtf8("commitBtn"))
        self.verticalLayout_2.addWidget(self.commitBtn)
        self.cancelBtn = QtGui.QPushButton(self.layoutWidget1)
        self.cancelBtn.setObjectName(_fromUtf8("cancelBtn"))
        self.verticalLayout_2.addWidget(self.cancelBtn)
        self.roomLabel = QtGui.QLabel(self.centralWidget)
        self.roomLabel.setGeometry(QtCore.QRect(20, 0, 321, 71))
        self.roomLabel.setText(_fromUtf8(""))
        self.roomLabel.setObjectName(_fromUtf8("roomLabel"))
        self.tipLabel = QtGui.QLabel(self.centralWidget)
        self.tipLabel.setGeometry(QtCore.QRect(50, 70, 181, 31))
        self.tipLabel.setText(_fromUtf8(""))
        self.tipLabel.setObjectName(_fromUtf8("tipLabel"))
        self.tempSlider = QtGui.QSlider(self.centralWidget)
        self.tempSlider.setGeometry(QtCore.QRect(20, 80, 21, 131))
        self.tempSlider.setOrientation(QtCore.Qt.Vertical)
        self.tempSlider.setObjectName(_fromUtf8("tempSlider"))
        self.setBackLab = QtGui.QLabel(self.centralWidget)
        self.setBackLab.setGeometry(QtCore.QRect(20, 40, 341, 221))
        self.setBackLab.setText(_fromUtf8(""))
        self.setBackLab.setObjectName(_fromUtf8("setBackLab"))
        self.setBackLab.raise_()
        self.oBtn.raise_()
        self.winFrame.raise_()
        self.tabWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.roomLabel.raise_()
        self.tipLabel.raise_()
        self.tempSlider.raise_()
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.oBtn.setText(_translate("MainWindow", "开机", None))
        self.lowBtn.setText(_translate("MainWindow", "低风", None))
        self.midBtn.setText(_translate("MainWindow", "中风", None))
        self.highBtn.setText(_translate("MainWindow", "高风", None))
        self.showLab.setText(_translate("MainWindow", "主人没开机呢，我该显示些什么呢", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.stateTab), _translate("MainWindow", "房间状态", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.billTab), _translate("MainWindow", "账单", None))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; color:#a17c9c;\">亲，如果空调出现任何问题请咨询我们的管理员：yifei@bupt.com</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; font-weight:600; color:#a17c9c;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; color:#a17c9c;\">如果不会使用我们的空调请咨询(￣ˇ￣)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; color:#a17c9c;\">emmmm....等我去注册个邮箱先昂~</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.condiTab), _translate("MainWindow", "空调使用手册", None))
        self.aimtemLabel.setText(_translate("MainWindow", "目标温度：", None))
        self.commitBtn.setText(_translate("MainWindow", "更改目标温度", None))
        self.cancelBtn.setText(_translate("MainWindow", "取消更改", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

