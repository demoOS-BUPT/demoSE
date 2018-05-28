# -*- coding: UTF-8 -*-
# Ui Init
from PyQt4 import QtCore, QtGui,uic

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

    def printAction(self):
        if (self.formForm.dayBtn.isChecked()):
            type = 0
        if (self.formForm.monthBtn.isChecked()):
            type = 1
        else:
            type = 2

        print '不会打印啦'+str(type)+str(self.formForm.dateEdit.date())

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    form = formUI()
    form.show()
    sys.exit(app.exec_())