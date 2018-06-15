# -*- coding: UTF-8 -*-
# Ui Init
from PyQt4 import QtCore, QtGui
from client import *
import sys
sys.path.append("./ui/")
from setrateui import *

H = 3
M = 2
L = 1

class setrateUI(QtGui.QDialog):

    def __init__(self,parent=None):
        super(setrateUI,self).__init__(parent)

        self.setrateForm = Ui_Form()
        self.setrateForm.setupUi(self)

        self.setrateForm.lowRateEdit.setText(str(WIND[L]))
        self.setrateForm.midRateEdit.setText(str(WIND[M]))
        self.setrateForm.highRateEdit.setText(str(WIND[H]))

        self.setrateForm.perMoneyEdit.setText(str(ELEC_MONEY))
        self.setrateForm.perTempEdit.setText(str(ELEC_TEMP))

        self.setrateForm.cancel.clicked.connect(self.bye)
        self.setrateForm.commitBtn.clicked.connect(self.commitAction)

    def commitAction(self):

        try:
            self.lowrate = float(self.setrateForm.lowRateEdit.text())
            self.midrate = float(self.setrateForm.midRateEdit.text())
            self.highrate = float(self.setrateForm.highRateEdit.text())
            self.perMoney = float(self.setrateForm.perMoneyEdit.text())
            self.perTemp = float(self.setrateForm.perTempEdit.text())
        except:
            QtGui.QMessageBox.information(self, u"信息提示", u"请填写数字")
            return

        if 0< self.lowrate < self.midrate and self.midrate < self.highrate < 5 and\
           0 < self.perMoney <10 and 0< self.perTemp < 5:
            WIND[L] = self.lowrate
            WIND[M] = self.midrate
            WIND[H] = self.highrate
            ELEC_MONEY = self.perMoney
            ELEC_TEMP = self.perTemp

            #修改配置文件
            cp.set("wind", "low",str(WIND[L]))
            cp.set("wind", "medium", str(WIND[M]))
            cp.set("wind", "high", str(WIND[H]))

            cp.set("elec", "money", str(ELEC_MONEY))
            cp.set("elec","temp",str(ELEC_TEMP))
            cp.write(open("Air.conf", "w"))

            self.accept()
            QtGui.QMessageBox.information(self, u"信息提示", u"修改成功")
        else:
            QtGui.QMessageBox.information(self, u"信息提示", u"修改规则\n(单位时间耗电数)低风<中风<高风\n每度电花费(0,10)元\n每度电温度变化(0,5)")

    def bye(self):
        self.close()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    setrate = setrateUI()
    setrate.show()
    sys.exit(app.exec_())