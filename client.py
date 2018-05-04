#-*- coding:utf-8 -*-
import socket
import time
import sys
from PyQt4 import QtCore, QtGui, uic
import threading
from Air import *
# Ui Init
qtCreatorFile = "client.ui"  # Window File
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

# Socket Init
HOST, PORT = "127.0.0.1", int(233)

room = 503
currentTemp = 15

#finalTemp = 25
#wind = 2

sock_flag = 0;

class Client(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # 连接信号和槽
        self.oBtn.clicked.connect(self.onOroff)
        self.commitBtn.setDisabled(False)

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.t = myThread(self.sock, self)

    def onOroff(self):
        global sock_flag
        if(sock_flag == 0):
            finalTemp = float(self.temperaBox.value())
            on_tips_string = u"您设置了空调温度：" + str(finalTemp)
            self.tipLabel.setText(on_tips_string)

            if(self.highBtn.isChecked()):
                wind = 2
            if(self.midBtn.isChecked()):
                wind = 1
            else:
                wind = 0

            # Connect to Server
            #try:
            self.sock.connect((HOST, PORT))
            #except Exception:
            #    print 'Server port not connect!'
            #    return

            time.sleep(0.2)
            #room=503, currentTemp=15, finalTemp=25, wind=2
            self.air = Air(room,currentTemp,finalTemp,wind)
            self.air.show_status()
            sendBuf = self.air.send_status()
            self.sock.send(sendBuf.encode(encoding="utf-8"))

            s = str(self.air.room) + u"房间的顾客您好呀! \nwe offering simple and comfort here~"
            self.roomLabel.setText(s)

            sock_flag = 1
            self.oBtn.setText(u"关机")
            self.t.start()

            self.commitBtn.clicked.connect(self.setTemp)
            self.cancelBtn.clicked.connect(self.cancelTemp)
        else:
            off_tips_string = u"耶 终于关空调了"
            self.tipLabel.setText(off_tips_string)
            sock_flag = 0;

            self.commitBtn.clicked.disconnect(self.setTemp)
            self.oBtn.setText(u"开机")

            self.sock.close()

    def showState(self):
        #self.stateLab.setText(str(self.air.))
        self.curtempLab.setText(str(self.air.currentTemp))
        self.aimtempLab.setText(str(self.air.finalTemp))

        if(self.air.wind == 2):
            wind_str = u"高风"
        if (self.air.wind == 1):
            wind_str = u"中风"
        else:
            wind_str = u"低风"
        self.windLab.setText(wind_str)
        #self.energyLab.setText(self.air.)
        #self.priceLab.setText(self.air.)

    #修改目标温度参数
    def setTemp(self):
        temperature = float(self.temperaBox.value())
        on_tips_string = u"您设置了空调温度：" + str(temperature)
        self.tipLabel.setText(on_tips_string)

        self.air.change_status(finalTemp=temperature)

    def cancelTemp(self):
        on_tips_string = u"成功取消目标温度更改"
        self.tipLabel.setText(on_tips_string)


        self.temperaBox.setValue(self.air.finalTemp)



class myThread(threading.Thread):  # 继承父类threading.Thread
    def __init__(self, sock,client):
        super(myThread, self).__init__()
        self.sock = sock
        self.client = client
    def run(self):
        global sock_flag
        opStr = ''
        while sock_flag:
            res = self.sock.recv(1024)
            opStr += res
            operate = opStr.split("_")

            self.client.showState()

            if operate[0] == 'a' and len(operate) == 10:
                opStr = ''
                print(operate)
            if operate[0] == 'close' and len(operate) == 2:
                opStr = ''
            # close
            if operate[0] == 'sleep' and len(operate) == 2:
                opStr = ''
            # 待机
            if operate[0] == 'wait' and len(operate) == 3:
                opStr = ''
            # 啥是等待？

            if 1 == 0:
                sendBuf = "aloha～"
                sock.send(sendBuf)
                print(sendBuf)

if __name__ == '__main__':
    ##ui
    sock_flag = 0;
    app = QtGui.QApplication(sys.argv)
    client = Client()
    client.show()

    sys.exit(app.exec_())

