# -*- coding: UTF-8 -*-
# Ui Init
from PyQt4 import QtCore, QtGui,Qt
from formui import *
from report import *

class formUI(QtGui.QDialog):
    def __init__(self,parent=None):
        super(formUI,self).__init__(parent)
        self.formForm = Ui_Form()
        self.formForm.setupUi(self)
        self.formForm.dayBtn.setChecked(True)
        self.formForm.gobackBtn.clicked.connect(self.bye)

        self.setDate()
        self.connect(self.formForm.printBtn,QtCore.SIGNAL("clicked()"),self.printAction)
        self.formForm.calWidget.clicked.connect(self.setDate)
        self.tableView()

    def bye(self):
        self.close()

    def tableView(self):
        column = 7
        row = 1
        self.formForm.tabWidget.setColumnCount(column)
        self.formForm.tabWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)

        self.formForm.tabWidget.setHorizontalHeaderLabels([u'开关次数',  u'常用目标温度', u'常用风速',u'达到目标温度次数',u'被服务次数',u'详单数',u'总费用'])

        #设置表头字体加粗：
        font = self.formForm.tabWidget.horizontalHeader().font()

        font.setBold(True)
        self.formForm.tabWidget.horizontalHeader().setFont(font)

        self.formForm.tabWidget.setRowCount(row)

        row_index = 0

        for i in list(range(0,7)):
            self.formForm.tabWidget.setItem(row_index, i, QtGui.QTableWidgetItem(u"-"))

    def setDate(self):
        self.formForm.dateEdit.setDate(self.formForm.calWidget.selectedDate())

    # 0日报表 1周 2月
    def printAction(self):
        if (self.formForm.dayBtn.isChecked()):
            type = 0
        elif (self.formForm.monthBtn.isChecked()):
            type = 1
        else:
            type = 2

        if (self.formForm.roomBox.currentIndex() == 0):
            room = '0'
        elif (self.formForm.roomBox.currentIndex() == 1):
            room = '306C'
        elif (self.formForm.roomBox.currentIndex() == 2):
            room = '306D'
        elif (self.formForm.roomBox.currentIndex() == 3):
            room = '307C'
        #其他房间
        room ='307C'

        #获取所需打印的第一天的年月日
        year,month,day = self.formForm.dateEdit.date().getDate()
        t = str(year) + '/'+str(month) + '/'+ str(day)

        import time
        timeArray = time.strptime(t, "%Y/%m/%d")
        '''
        timeStamp = int(time.mktime(timeArray))
        '''
        #传类型和日期
        #print '不会打印啦'+str(type) +t + str(timeStamp) + room

        #收一堆信息展示
        '''
        self.formForm.tabWidget.setRowCount(4)
        '''
        list = database.report(timeArray,room,type)
        for i in list:
            self.formForm.tabWidget.setItem(0, i, QtGui.QTableWidgetItem(str(list[i])))
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    form = formUI()
    form.show()
    sys.exit(app.exec_())