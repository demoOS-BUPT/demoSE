# -*- coding: UTF-8 -*-
# Ui Init
from PyQt4 import QtCore, QtGui,uic,Qt

form_qtCreatorFile = "form.ui"  # Window File
form_MainWindow, form_QtBaseClass = uic.loadUiType(form_qtCreatorFile)

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_formForm(QtGui.QMainWindow,form_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        form_MainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle( u"报表打印")

class formUI(QtGui.QDialog):
    def __init__(self,parent=None):
        super(formUI,self).__init__(parent)
        self.formForm = Ui_formForm()
        self.formForm.setupUi(self)
        self.formForm.dayBtn.setChecked(True)

        self.setDate()
        self.connect(self.formForm.printBtn,QtCore.SIGNAL("clicked()"),self.printAction)
        self.formForm.calWidget.clicked.connect(self.setDate)
        self.tableView()

    def tableView(self):
        column = 10
        row = 4
        self.formForm.tabWidget.setColumnCount(column)
        self.formForm.tabWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)

        self.formForm.tabWidget.setHorizontalHeaderLabels([u'Room',  u'Operate', u'User','IP','Time','InitTemperature','FinalTemperature','Wind','PerMoney', 'TotalMoney'])

        #设置表头字体加粗：
        font = self.formForm.tabWidget.horizontalHeader().font()

        font.setBold(True)
        self.formForm.tabWidget.horizontalHeader().setFont(font)

        self.formForm.tabWidget.setRowCount(row)

        row_index = 0

        self.formForm.tabWidget.setItem(row_index, 0, QtGui.QTableWidgetItem(u"308"))
        self.formForm.tabWidget.setItem(row_index, 1, QtGui.QTableWidgetItem("199"))
        self.formForm.tabWidget.setItem(row_index, 2, QtGui.QTableWidgetItem("20.5"))

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
        #其他房间

        #获取所需打印的第一天的年月日
        year,month,day = self.formForm.dateEdit.date().getDate()
        t = str(year) + '/'+str(month) + '/'+ str(day)
        import time
        timeArray = time.strptime(t, "%Y/%m/%d")
        timeStamp = int(time.mktime(timeArray))

        #传类型和日期
        print '不会打印啦'+str(type) +t + str(timeStamp) + room

        #收一堆信息展示
        '''
        self.formForm.tabWidget.setRowCount(4)
        '''


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    form = formUI()
    form.show()
    sys.exit(app.exec_())