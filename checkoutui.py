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
        Form.resize(400, 300)
        self.commitBtn = QtGui.QPushButton(Form)
        self.commitBtn.setGeometry(QtCore.QRect(160, 160, 93, 28))
        self.commitBtn.setObjectName(_fromUtf8("commitBtn"))
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 80, 221, 71))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.roomBox = QtGui.QComboBox(self.layoutWidget)
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
        self.layoutWidget.raise_()
        self.commitBtn.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.commitBtn.setText(_translate("Form", "退房咯！", None))
        self.label.setText(_translate("Form", "房间号：", None))
        self.roomBox.setItemText(0, _translate("Form", "307C", None))
        self.label_2.setText(_translate("Form", "消费金额：", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

