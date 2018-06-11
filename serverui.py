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
        Serverui.resize(968, 825)
        self.frame = QtGui.QFrame(Serverui)
        self.frame.setGeometry(QtCore.QRect(30, 20, 531, 61))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.display = QtGui.QLabel(Serverui)
        self.display.setGeometry(QtCore.QRect(580, 120, 231, 101))
        self.display.setText(_fromUtf8(""))
        self.display.setObjectName(_fromUtf8("display"))
        self.layoutWidget = QtGui.QWidget(Serverui)
        self.layoutWidget.setGeometry(QtCore.QRect(200, 240, 711, 171))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.C306Lab = QtGui.QLabel(self.layoutWidget)
        self.C306Lab.setObjectName(_fromUtf8("C306Lab"))
        self.horizontalLayout_2.addWidget(self.C306Lab)
        self.D306Lab = QtGui.QLabel(self.layoutWidget)
        self.D306Lab.setObjectName(_fromUtf8("D306Lab"))
        self.horizontalLayout_2.addWidget(self.D306Lab)
        self.C307Lab = QtGui.QLabel(self.layoutWidget)
        self.C307Lab.setObjectName(_fromUtf8("C307Lab"))
        self.horizontalLayout_2.addWidget(self.C307Lab)
        self.serverLab = QtGui.QLabel(Serverui)
        self.serverLab.setGeometry(QtCore.QRect(30, 280, 141, 361))
        self.serverLab.setObjectName(_fromUtf8("serverLab"))
        self.onBtn = QtGui.QPushButton(Serverui)
        self.onBtn.setGeometry(QtCore.QRect(850, 70, 91, 71))
        self.onBtn.setObjectName(_fromUtf8("onBtn"))
        self.layoutWidget1 = QtGui.QWidget(Serverui)
        self.layoutWidget1.setGeometry(QtCore.QRect(31, 106, 311, 111))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.formBtn = QtGui.QPushButton(self.layoutWidget1)
        self.formBtn.setObjectName(_fromUtf8("formBtn"))
        self.horizontalLayout_3.addWidget(self.formBtn)
        self.checkoutBtn = QtGui.QPushButton(self.layoutWidget1)
        self.checkoutBtn.setObjectName(_fromUtf8("checkoutBtn"))
        self.horizontalLayout_3.addWidget(self.checkoutBtn)
        self.setBtn = QtGui.QPushButton(self.layoutWidget1)
        self.setBtn.setObjectName(_fromUtf8("setBtn"))
        self.horizontalLayout_3.addWidget(self.setBtn)
        self.layoutWidget_2 = QtGui.QWidget(Serverui)
        self.layoutWidget_2.setGeometry(QtCore.QRect(200, 420, 711, 171))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.D308Lab = QtGui.QLabel(self.layoutWidget_2)
        self.D308Lab.setObjectName(_fromUtf8("D308Lab"))
        self.horizontalLayout_4.addWidget(self.D308Lab)
        self.D307Lab = QtGui.QLabel(self.layoutWidget_2)
        self.D307Lab.setObjectName(_fromUtf8("D307Lab"))
        self.horizontalLayout_4.addWidget(self.D307Lab)
        self.C308Lab = QtGui.QLabel(self.layoutWidget_2)
        self.C308Lab.setObjectName(_fromUtf8("C308Lab"))
        self.horizontalLayout_4.addWidget(self.C308Lab)
        self.layoutWidget_3 = QtGui.QWidget(Serverui)
        self.layoutWidget_3.setGeometry(QtCore.QRect(200, 590, 711, 171))
        self.layoutWidget_3.setObjectName(_fromUtf8("layoutWidget_3"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.C309Lab = QtGui.QLabel(self.layoutWidget_3)
        self.C309Lab.setObjectName(_fromUtf8("C309Lab"))
        self.horizontalLayout_5.addWidget(self.C309Lab)
        self.D309Lab = QtGui.QLabel(self.layoutWidget_3)
        self.D309Lab.setObjectName(_fromUtf8("D309Lab"))
        self.horizontalLayout_5.addWidget(self.D309Lab)
        self.C310Lab = QtGui.QLabel(self.layoutWidget_3)
        self.C310Lab.setObjectName(_fromUtf8("C310Lab"))
        self.horizontalLayout_5.addWidget(self.C310Lab)

        self.retranslateUi(Serverui)
        QtCore.QMetaObject.connectSlotsByName(Serverui)

    def retranslateUi(self, Serverui):
        Serverui.setWindowTitle(_translate("Serverui", "Dialog", None))
        self.C306Lab.setText(_translate("Serverui", "这是306C", None))
        self.D306Lab.setText(_translate("Serverui", "这是306D", None))
        self.C307Lab.setText(_translate("Serverui", "这是307C", None))
        self.serverLab.setText(_translate("Serverui", "当前时间巴拉巴拉", None))
        self.onBtn.setText(_translate("Serverui", "开", None))
        self.formBtn.setText(_translate("Serverui", "报表", None))
        self.checkoutBtn.setText(_translate("Serverui", "退房", None))
        self.setBtn.setText(_translate("Serverui", "设置", None))
        self.D308Lab.setText(_translate("Serverui", "这是308D", None))
        self.D307Lab.setText(_translate("Serverui", "这是307D", None))
        self.C308Lab.setText(_translate("Serverui", "这是308C", None))
        self.C309Lab.setText(_translate("Serverui", "这是309C", None))
        self.D309Lab.setText(_translate("Serverui", "这是309D", None))
        self.C310Lab.setText(_translate("Serverui", "这是310C", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Serverui = QtGui.QDialog()
    ui = Ui_Serverui()
    ui.setupUi(Serverui)
    Serverui.show()
    sys.exit(app.exec_())

