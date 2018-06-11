# -*- coding: UTF-8 -*-
# Ui Init
from PyQt4 import QtCore, QtGui,uic
from client import *
from setRateui import *

class setrateUI(QtGui.QDialog):
    def __init__(self,parent=None):
        super(setrateUI,self).__init__(parent)

        self.setrateForm = Ui_Form()
        self.setrateForm.setupUi(self)

        self.setrateForm.lowRateEdit.setText('1.5')
        self.setrateForm.midRateEdit.setText('2')
        self.setrateForm.highRateEdit.setText('2.5')

        self.setrateForm.commitBtn.clicked.connect(self.commitAction)

    def commitAction(self):


        self.lowrate = float(self.setrateForm.lowRateEdit.text())
        self.midrate = float(self.setrateForm.midRateEdit.text())
        self.highrate = float(self.setrateForm.highRateEdit.text())


        if self.lowrate < 10 and self.lowrate >1:
            QtGui.QMessageBox.information(self, u"信息提示", u"修改成功")
            self.accept()
        else:
            QtGui.QMessageBox.information(self, u"信息提示", u"修改规则：嗯嗯没写")

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    setrate = setrateUI()
    setrate.show()
    sys.exit(app.exec_())