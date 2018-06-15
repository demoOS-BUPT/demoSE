# -*- coding: UTF-8 -*-
# Ui Init
from PyQt4 import QtCore, QtGui
from client import *

import sys
sys.path.append("./ui/")
from checkoutui import *
from Dform import *
from report import *

class checkoutUI(QtGui.QDialog):
    def __init__(self,parent=None):
        super(checkoutUI,self).__init__(parent)
        self.checkoutForm = Ui_Form()
        self.checkoutForm.setupUi(self)
        self.checkoutForm.commitBtn.clicked.connect(self.commitAction)
        self.checkoutForm.cancelBtn.clicked.connect(self.bye)
        self.checkoutForm.gotoDform.clicked.connect(self.dform)
        self.checkoutForm.gotoDform.hide()
        self.roomList = []

    def commitAction(self):
        if (self.checkoutForm.roomBox.currentIndex() == 0):
            self.room = '306C'
        elif (self.checkoutForm.roomBox.currentIndex() == 1):
            self.room = '306D'
        elif (self.checkoutForm.roomBox.currentIndex() == 2):
            self.room = '307C'
        elif (self.checkoutForm.roomBox.currentIndex() == 3):
            self.room = '307D'
        elif (self.checkoutForm.roomBox.currentIndex() == 4):
            self.room = '308C'
        elif (self.checkoutForm.roomBox.currentIndex() == 5):
            self.room = '308D'
        elif (self.checkoutForm.roomBox.currentIndex() == 6):
            self.room = '309C'
        elif (self.checkoutForm.roomBox.currentIndex() == 7):
            self.room = '309D'
        elif (self.checkoutForm.roomBox.currentIndex() == 8):
            self.room = '310C'

        self.roomList.append(self.room)

        QtGui.QMessageBox.information(self, u"信息提示", str(self.room) + u"退房成功")
        money = database.getTotalMoney(self.room)
        if money == None:
            money = 0
        self.checkoutForm.priceLab.setText(str(money))

        self.checkoutForm.gotoDform.show()

    def dform(self):
        self.Dform = DformUI(self.room)
        self.Dform.show()

    def bye(self):
        self.close()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    checkout = checkoutUI()
    checkout.show()
    sys.exit(app.exec_())