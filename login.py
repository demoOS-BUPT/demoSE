# -*- coding: UTF-8 -*-
# Ui Init
from PyQt4 import QtCore, QtGui,uic
from client import *
from loginui import *
login_qtCreatorFile = "login.ui"  # Window File
login_MainWindow, login_QtBaseClass = uic.loadUiType(login_qtCreatorFile)

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

class loginUI(QtGui.QDialog):
    def __init__(self,parent=None):
        super(loginUI,self).__init__(parent)
        self.LoginForm = Ui_Login()
        self.LoginForm.setupUi(self)

        self.connect(self.LoginForm.Loginbtn,QtCore.SIGNAL("clicked()"),self.LoginAction)
        self.LoginForm.Closebtn.clicked.connect(self.bye)

    def LoginAction(self):
        user = unicode(self.LoginForm.UserNamelineEdit.text().toUtf8(),'utf8','ignore').encode('utf-8')
        passwd = unicode(self.LoginForm.PasslineEdit.text().toUtf8(),'utf8','ignore').encode('utf-8')

        if user == '' or passwd == '':
            #QtGui.QMessageBox.information(self,u"信息提示",u"房间号或者密码不能为空")
            self.accept()
            self.client = Client(user)
            self.client.show()

        else:
            if(passwd == '307C'):
                self.accept()
                self.client = Client(user)
                self.client.show()
            else:
                QtGui.QMessageBox.information(self, u"信息提示", u"密码错误")

    def bye(self):
        QtGui.QMessageBox.information(self, u"信息提示", u"欢迎下次光临")
        self.close()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    login = loginUI()
    login.show()

    if( app.exec_() ):
        print 'aa'
        exit()
