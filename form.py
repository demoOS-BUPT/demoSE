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

    def bye(self):
        self.close()

    def setDate(self):
        self.formForm.dateEdit.setDate(self.formForm.calWidget.selectedDate())

    # 0日报表 1周 2月
    def printAction(self):
        #类型
        type_str = u"日报表"
        if (self.formForm.dayBtn.isChecked()):
            type = 0
        elif (self.formForm.monthBtn.isChecked()):
            type = 2
            type_str = u"月报表"
        else:
            type_str = u"周报表"
            type = 1

        #房间
        roomNum = {'306C', '306D', '307C', '307D', '308C', '308D', '309C', '309D', '310C'}
        room = roomNum[self.formForm.roomBox.currentIndex()]

        #年月日
        year,month,day = self.formForm.dateEdit.date().getDate()
        t = str(year) + '/'+str(month) + '/'+ str(day)
        import time
        timeArray = time.strptime(t, "%Y/%m/%d")



        #从持久层接口获取报表
        list = None
        list = database.report(timeArray,room,type)

        #界面展示信息
        column = 0
        wind = [0, u'低风', u'中风', u'高风']
        if list != None and list != [0, None, None, 0, 0, 0]:
            for i in list:
                if column == 2:
                    self.formForm.tabWidget.setItem(0, column, QtGui.QTableWidgetItem(wind[i]))
                else:
                    self.formForm.tabWidget.setItem(0, column, QtGui.QTableWidgetItem(str(i)))
                column += 1
        self.formForm.title.setText(u"以下是"+room+u"的"+type_str)
        self.formForm.tabWidget.setRowCount(1)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    form = formUI()
    form.show()
    sys.exit(app.exec_())
