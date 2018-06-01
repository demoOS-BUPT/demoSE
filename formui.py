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

        self.connect(self.formForm.printBtn,QtCore.SIGNAL("clicked()"),self.printAction)
        self.formForm.calWidget.clicked.connect(self.setDate)
        self.tableView()
    def tableView(self):
        self.formForm.tabWidget.setColumnCount(3)
        self.formForm.tabWidget.setRowCount(4)
        self.formForm.tabWidget.setHorizontalHeaderLabels([u'房间号',  u'金额', u'能耗'])

        #设置表头字体加粗：
        font = self.formForm.tabWidget.horizontalHeader().font()

        font.setBold(True)
        self.formForm.tabWidget.horizontalHeader().setFont(font)

        newItem = QtGui.QTableWidgetItem(u"308")
        self.formForm.tabWidget.setItem(0, 0, newItem)

        newItem = QtGui.QTableWidgetItem("199")
        self.formForm.tabWidget.setItem(0, 1, newItem)

        newItem = QtGui.QTableWidgetItem("20.5")
        self.formForm.tabWidget.setItem(0, 2, newItem)

    def setDate(self):
        self.formForm.dateEdit.setDate(self.formForm.calWidget.selectedDate())

    # 0日报表 1周 2月
    def printAction(self):
        if (self.formForm.dayBtn.isChecked()):
            type = 0
        if (self.formForm.monthBtn.isChecked()):
            type = 1
        else:
            type = 2

        #获取所需打印的第一天的年月日
        year,month,day = self.formForm.dateEdit.date().getDate()
        print '不会打印啦'+str(type)+' year:'+str(year) + ' month: '+str(month) + 'day '+ str(day)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    form = formUI()
    form.show()
    sys.exit(app.exec_())