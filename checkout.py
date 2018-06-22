# -*- coding: UTF-8 -*-
# Ui Init
from PyQt4 import QtCore, QtGui
from client import *

import sys
sys.path.append("./ui/")
from checkoutui import *
from Dform import *
from report import *

checkoutList = []

class checkoutUI(QtGui.QDialog):
    def __init__(self,parent=None):
        super(checkoutUI,self).__init__(parent)
        self.checkoutForm = Ui_Form()
        self.checkoutForm.setupUi(self)
        self.checkoutForm.commitBtn.clicked.connect(self.commitAction)
        self.checkoutForm.cancelBtn.clicked.connect(self.bye)
        self.checkoutForm.gotoDform.clicked.connect(self.dform)
        self.checkoutForm.gotoDform.hide()
        self.roomList = set()

    def commitAction(self):
        roomNum = {'306C', '306D', '307C', '307D', '308C', '308D', '309C', '309D', '310C'}
        self.room = roomNum[self.checkoutForm.roomBox.currentIndex()]

        global checkoutList

        if self.room in self.roomList:
            QtGui.QMessageBox.information(self, u"操作失败", str(self.room) + u"已退过房啦")
        else:
            self.roomList.add(self.room)
            checkoutList.append(self.room)
            print 'append '+checkoutList[0]
            QtGui.QMessageBox.information(self, u"操作成功", str(self.room) + u"退房成功")

        r_str = ''
        for r in self.roomList:
            r_str += r+' '
        self.checkoutForm.roomListLab.setText(r_str+u"成功退房")

        
        #获取消费金额
        money = database.getTotalMoney(self.room)
        if money == None:
            money = 0
        self.checkoutForm.priceLab.setText(str(money)+u"元")


        self.checkoutForm.gotoDform.setText(self.room+u"详单")
        self.checkoutForm.gotoDform.show()

    def dform(self):
        self.Dform = DformUI(self.room)
        self.Dform.show()

    def bye(self):
        self.accept()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    checkout = checkoutUI()
    checkout.show()
    sys.exit(app.exec_())