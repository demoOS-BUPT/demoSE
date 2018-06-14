# -*- coding: UTF-8 -*-
# Ui Init
from PyQt4 import QtCore, QtGui,uic

from Dformui import *


class DformUI(QtGui.QDialog):
    def __init__(self,room,parent=None):
        super(DformUI,self).__init__(parent)
        self.Dform = Ui_MainWindow()
        self.Dform.setupUi(self)
        self.room = room
        self.showTab()

    def showTab(self):

        '''
        user = "zxh"
        money = database.getTotalMoney("room"+self.room,user)
        '''
        QtGui.QMessageBox.information(self, u"信息提示", u"OK")

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dform = DformUI()
    Dform.show()
    sys.exit(app.exec_())