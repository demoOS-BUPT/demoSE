# -*- coding: UTF-8 -*-
# Ui Init
from PyQt4 import QtCore, QtGui,uic
from client import *
checkout_qtCreatorFile = "checkout.ui"  # Window File
checkout_MainWindow, checkout_QtBaseClass = uic.loadUiType(checkout_qtCreatorFile)

class Ui_checkoutForm(QtGui.QMainWindow,checkout_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        checkout_MainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle( u"买单")

class checkoutUI(QtGui.QDialog):
    def __init__(self,parent=None):
        super(checkoutUI,self).__init__(parent)
        self.checkoutForm = Ui_checkoutForm()
        self.checkoutForm.setupUi(self)
        self.checkoutForm.commitBtn.clicked.connect(self.commitAction)

    def commitAction(self):

        QtGui.QMessageBox.information(self, u"信息提示", u"OK")

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    checkout = checkoutUI()
    checkout.show()
    sys.exit(app.exec_())