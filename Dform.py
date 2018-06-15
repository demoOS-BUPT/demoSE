# -*- coding: UTF-8 -*-
# Ui Init
from PyQt4 import QtCore, QtGui

from report import *
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

        column = 13
        self.Dform.tableWidget.setColumnCount(column)
        self.Dform.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)

        self.Dform.tableWidget.setHorizontalHeaderLabels(
            ['id',u'操作','user',u'日期', u'时长', u'室温', u'目标温度', u'风速', u'每度电费',u'总耗电量',u'permoney?',u'singlemoney?',u'总金额'])
        self.Dform.tableWidget.setColumnHidden(0,True)
        self.Dform.tableWidget.setColumnHidden(2,True)
        #设置100%填充
        #item=self.tableWidget.horizontalHeader()
        #item.setStretchLastSection(1)
        
        #self.Dform.tableWidget.setRowHeight(1,50)

        #设置指定列宽
        self.Dform.tableWidget.setColumnWidth(1,80)
        self.Dform.tableWidget.setColumnWidth(2,70)
        self.Dform.tableWidget.setColumnWidth(3,70)
        self.Dform.tableWidget.setColumnWidth(4,60)
        self.Dform.tableWidget.setColumnWidth(5,60)
        self.Dform.tableWidget.setColumnWidth(6,80)
        self.Dform.tableWidget.setColumnWidth(7,57)
        self.Dform.tableWidget.setColumnWidth(8,80)
        self.Dform.tableWidget.setColumnWidth(9,80)
        self.Dform.tableWidget.setColumnWidth(10,60)
        self.Dform.tableWidget.setColumnWidth(11,60)
        self.Dform.tableWidget.setColumnWidth(12,61)
        self.Dform.tableWidget.setColumnWidth(13,55)

        # 设置表头字体加粗：
        font = self.Dform.tableWidget.horizontalHeader().font()

        font.setBold(True)
        self.Dform.tableWidget.horizontalHeader().setFont(font)


        list = database.detailed_bill(self.room)
        print len(list)
        self.Dform.tableWidget.setRowCount(len(list))
        row = 0
        column = 0
        for items in list:
            for item in items:
                self.Dform.tableWidget.setItem(row, column, QtGui.QTableWidgetItem(str(item)))
                column +=1
            row +=1

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dform = DformUI("307C")
    Dform.show()
    sys.exit(app.exec_())
