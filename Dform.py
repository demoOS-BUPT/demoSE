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
        self.Dform.gobackBtn.clicked.connect(self.bye)

    def bye(self):
        self.close()

    def showTab(self):

        column = 7
        row = 1
        self.Dform.tableWidget.setColumnCount(column)
        self.Dform.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)

        self.Dform.tableWidget.setHorizontalHeaderLabels(
            [u'开关次数', u'常用目标温度', u'常用风速', u'达到目标温度次数', u'被服务次数', u'详单数', u'总费用'])

        # 设置表头字体加粗：
        font = self.Dform.tableWidget.horizontalHeader().font()

        font.setBold(True)
        self.Dform.tableWidget.horizontalHeader().setFont(font)

        self.Dform.tableWidget.setRowCount(row)

        row_index = 0

        for i in list(range(0, 7)):
            self.Dform.tableWidget.setItem(row_index, i, QtGui.QTableWidgetItem(u"-"))
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