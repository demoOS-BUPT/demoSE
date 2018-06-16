# -*- coding: UTF-8 -*-
# Ui Init
from PyQt4 import QtCore, QtGui

from report import *
import sys;
sys.path.append("./ui/")
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
        '''
        column = 13
        self.Dform.tableWidget.setColumnCount(column)
        self.Dform.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)

        self.Dform.tableWidget.setHorizontalHeaderLabels(
            ['id',u'操作','user',u'日期', u'时长', u'室温', u'目标温度', u'风速', u'单次服务用电',u'总耗电量',u'耗费/单位时间',u'单次服务金额',u'总金额'])
        self.Dform.tableWidget.setColumnHidden(0,True)
        self.Dform.tableWidget.setColumnHidden(2,True)

        #设置100%填充
        self.Dform.tableWidget.horizontalHeader().setStretchLastSection(True)
        
        #self.Dform.tableWidget.setRowHeight(1,50)
        '''
        #设置指定列宽
        '''
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
        '''

        '''
        print len(list)
        self.Dform.tableWidget.setRowCount(len(list))
        '''
        list = database.detailed_bill(self.room)
        row = 0
        column = 0
        wind = [0,u'低风',u'中风',u'高风']

        self.Dform.listWidget.clear()
        status = {}
        for items in list:
            #['id',u'操作','user',u'日期', u'时长', u'室温', u'目标温度', u'风速', u'单次服务用电',u'总耗电量',u'耗费/单位时间',u'单次服务金额',u'总金额'])
            status['op'] = items[1]
            status['date'] = items[3]
            status['timelen'] = items[4]
            status['roomtemp'] = items[5]
            status['targettemp'] = items[6]
            status['wind'] = wind[items[7]]
            status['singleelec'] = items[8]
            status['totalelec'] = items[9]
            status['permoney'] = items[10]
            status['singlemoney'] = items[11]
            status['totalmoney'] = items[12]

            if items[1] == "firstopen":
                showBuf = u'{date} 第一次开机啦'
            elif items[1] == "serve":
                showBuf = u'{date} 目标温度{targettemp}风速{wind}'
            elif items[1] == "open":
                showBuf = u'{date} 又开机啦'
            elif items[1] == "close":
                showBuf = u'{date} 关机啦 总共花费{totalmoney}'
            else:
                print items[1]
            showBuf = showBuf.format(**status)
            self.Dform.listWidget.addItem(showBuf)

        '''
            if items != None:
                for item in items:
                    if column == 7:
                        self.Dform.tableWidget.setItem(row, column, QtGui.QTableWidgetItem(wind[item]))
                    elif column == 1:
                        if str(item)=="firstopen":
                            s = u"第一次开"
                        if str(item) == "serve":
                            s = u"单次服务"
                        if str(item) == "open":
                            s = u"打开空调"
                        if str(item) == "close":
                            s = u"关闭空调"
                        self.Dform.tableWidget.setItem(row, column, QtGui.QTableWidgetItem(s))
                    else:
                        self.Dform.tableWidget.setItem(row, column, QtGui.QTableWidgetItem(str(item)))
                    column +=1
                row +=1
                column = 0
        '''

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dform = DformUI("307C")
    Dform.show()
    sys.exit(app.exec_())
