# -*- coding: UTF-8 -*-
# Ui Init
from PyQt4 import QtCore, QtGui,Qt

import sys
sys.path.append("./ui/")
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
        column = 8

        self.formForm.tabWidget.setColumnCount(column)
        self.formForm.tabWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)

        self.formForm.tabWidget.setHorizontalHeaderLabels([u'开关次数',  u'常用目标温度', u'常用风速',u'达到目标温度次数',u'被服务次数',u'详单数',u'总费用'])

        #设置自动填充
        #item=self.tabWidget.horizontalHeader()
        #item.setStretchLastSection(1)
        
         #设置指定列宽
        self.formForm.tabWidget.setColumnWidth(0,90)
        self.formForm.tabWidget.setColumnWidth(1,115)
        self.formForm.tabWidget.setColumnWidth(2,80)
        self.formForm.tabWidget.setColumnWidth(3,144)
        self.formForm.tabWidget.setColumnWidth(4,100)
        self.formForm.tabWidget.setColumnWidth(5,70)
        self.formForm.tabWidget.setColumnWidth(6,80)
        self.formForm.tabWidget.setColumnWidth(7,0)

        #设置表头字体加粗：
        font = self.formForm.tabWidget.horizontalHeader().font()

        font.setBold(True)
        self.formForm.tabWidget.horizontalHeader().setFont(font)

    def setDate(self):
        self.formForm.dateEdit.setDate(self.formForm.calWidget.selectedDate())

    # 0日报表 1周 2月
    def printAction(self):

        type_str = u"日报表"
        if (self.formForm.dayBtn.isChecked()):
            type = 0
        elif (self.formForm.monthBtn.isChecked()):
            type = 2
            type_str = u"月报表"
        else:
            type_str = u"周报表"
            type = 1

        room = 0
        if (self.formForm.roomBox.currentIndex() == 0):
            room = '306C'
        elif (self.formForm.roomBox.currentIndex() == 1):
            room = '306D'
        elif (self.formForm.roomBox.currentIndex() == 2):
            room = '307C'
        elif (self.formForm.roomBox.currentIndex() == 3):
            room = '307D'
        elif (self.formForm.roomBox.currentIndex() == 4):
            room = '308C'
        elif (self.formForm.roomBox.currentIndex() == 5):
            room = '308D'
        elif (self.formForm.roomBox.currentIndex() == 6):
            room = '309C'
        elif (self.formForm.roomBox.currentIndex() == 7):
            room = '309D'
        elif (self.formForm.roomBox.currentIndex() == 8):
            room = '310C'

        #获取所需打印的第一天的年月日
        year,month,day = self.formForm.dateEdit.date().getDate()
        t = str(year) + '/'+str(month) + '/'+ str(day)
        import time
        timeArray = time.strptime(t, "%Y/%m/%d")

        self.formForm.title.setText(u"以下是"+room+u"的"+type_str)
        self.formForm.tabWidget.setRowCount(1)

        list = None
        list = database.report(timeArray,room,type)

        column = 0
        wind = [0, u'低风', u'中风', u'高风']
        if list != None:
            for i in list:
                if column == 2:
                    self.formForm.tabWidget.setItem(0, column, QtGui.QTableWidgetItem(wind[i]))
                else:
                    self.formForm.tabWidget.setItem(0, column, QtGui.QTableWidgetItem(str(i)))
                column += 1

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    form = formUI()
    form.show()
    sys.exit(app.exec_())
