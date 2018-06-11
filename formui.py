# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
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
        Form.resize(1159, 680)
        self.printBtn = QtGui.QPushButton(Form)
        self.printBtn.setGeometry(QtCore.QRect(450, 210, 93, 28))
        self.printBtn.setObjectName(_fromUtf8("printBtn"))
        self.dateEdit = QtGui.QDateEdit(Form)
        self.dateEdit.setGeometry(QtCore.QRect(450, 80, 110, 22))
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 140, 161, 41))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.roomBox = QtGui.QComboBox(self.layoutWidget)
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
        self.layoutWidget1 = QtGui.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(453, 112, 101, 91))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.dayBtn = QtGui.QRadioButton(self.layoutWidget1)
        self.dayBtn.setObjectName(_fromUtf8("dayBtn"))
        self.verticalLayout.addWidget(self.dayBtn)
        self.monthBtn = QtGui.QRadioButton(self.layoutWidget1)
        self.monthBtn.setObjectName(_fromUtf8("monthBtn"))
        self.verticalLayout.addWidget(self.monthBtn)
        self.yearBtn = QtGui.QRadioButton(self.layoutWidget1)
        self.yearBtn.setObjectName(_fromUtf8("yearBtn"))
        self.verticalLayout.addWidget(self.yearBtn)
        self.calWidget = QtGui.QCalendarWidget(Form)
        self.calWidget.setGeometry(QtCore.QRect(580, 0, 296, 236))
        self.calWidget.setObjectName(_fromUtf8("calWidget"))
        self.tabWidget = QtGui.QTableWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(30, 260, 1091, 391))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabWidget.setColumnCount(0)
        self.tabWidget.setRowCount(0)

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


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

