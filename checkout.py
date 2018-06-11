# -*- coding: UTF-8 -*-
# Ui Init
from PyQt4 import QtCore, QtGui,uic
from client import *
from checkoutui import *

class checkoutUI(QtGui.QDialog):
    def __init__(self,parent=None):
        super(checkoutUI,self).__init__(parent)
        self.checkoutForm = Ui_Form()
        self.checkoutForm.setupUi(self)
        self.checkoutForm.commitBtn.clicked.connect(self.commitAction)

    def commitAction(self):
        if (self.checkoutForm.roomBox.currentIndex() == 0):
            self.room = '307C'
        QtGui.QMessageBox.information(self, u"信息提示", u"OK")

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    checkout = checkoutUI()
    checkout.show()
    sys.exit(app.exec_())