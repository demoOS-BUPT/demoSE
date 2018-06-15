# -*- coding: UTF-8 -*-
# Ui Init
from PyQt4 import QtCore, QtGui
from client import *
from loginui import *
from AirService import *

class loginUI(QtGui.QDialog):
    def __init__(self,parent=None):
        super(loginUI,self).__init__(parent)
        self.LoginForm = Ui_Dialog()
        self.LoginForm.setupUi(self)

        self.connect(self.LoginForm.Loginbtn,QtCore.SIGNAL("clicked()"),self.LoginAction)
        self.LoginForm.Closebtn.clicked.connect(self.bye)

    def LoginAction(self):
        user = unicode(self.LoginForm.UserNamelineEdit.text().toUtf8(),'utf8','ignore').encode('utf-8')
        passwd = unicode(self.LoginForm.PasslineEdit.text().toUtf8(),'utf8','ignore').encode('utf-8')

        if user == '':
            QtGui.QMessageBox.information(self,u"信息提示",u"房间号不能为空")
        else:
            if(passwd == ''):
                self.accept()
                self.client = Client(user)
                self.client.show()
            else:
                QtGui.QMessageBox.information(self, u"信息提示", u"密码不要填哦")

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
