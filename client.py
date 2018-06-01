#-*- coding:utf-8 -*-
import socket
import time
import sys
from PyQt4 import QtCore, QtGui, uic
import threading
from AirClient import *

# Ui Init
qtCreatorFile = "client.ui"  # Window File
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

# Socket Init
HOST, PORT = "127.0.0.1", int(233)

room = 503
currentTemp = 15
limit_l = 16
limit_h = 30
defalt_temp = 26
#finalTemp = 25
#wind = 2

sock_flag = 0;

class Client(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self,user):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        global room
        room = user

        # 开始装载样式表
        qss_file = open('clientQSS.qss').read()
        self.setStyleSheet(qss_file)

        # 设置滑动条控件的最大最小值
        self.tempSlider.setMinimum(limit_l)
        self.tempSlider.setMaximum(limit_h)
        # 设置滑动条控件的初始值
        self.tempSlider.setValue(defalt_temp)

        # 连接信号和槽
        self.tempSlider.valueChanged[int].connect(self.changetemp)
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

            #Connect to Server
            #try:
            self.sock.connect((HOST, PORT))
            #except Exception:
            #    print 'Server port not connect!'
            #    return

            time.sleep(0.2)
            #room=503, currentTemp=15, finalTemp=25, wind=2
            self.air = AirClient(room,currentTemp,finalTemp,wind)

            '''默认在哪设都行
            status = {'room': '307C',
                      'currentTemp': 20.3,
                      'finalTemp': 28.0,
                      'wind': 2,  # 中速
                      }
            self.air.change_status(status)
            '''

            ##开机
            sendBuf = self.air.send_start()
            print sendBuf
            self.sock.send(sendBuf)

            self.air.show_status()
            sendBuf = self.air.send_first_open()
            print sendBuf
            self.sock.send(sendBuf)

            '''
            self.air.show_status()
            sendBuf = self.air.send_status()
            print sendBuf
            self.sock.send(sendBuf.encode(encoding="utf-8"))
            '''
            s = str(self.air.room) + u"房间的顾客您好呀! \nwe offering simple and comfort here~"
            starttime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.air.startTime))
            s += ( u"\n开机时间为：" + str(starttime) )
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
        stateStr = ""
        stateStr += u"当前模式："+self.air.mode
        stateStr += u"\n当前温度："+(str(self.air.currentTemp))
        stateStr += u"\n目标温度：" +(str(self.air.finalTemp))

        if(self.air.wind == 2):
            wind_str = u"高风"
        if (self.air.wind == 1):
            wind_str = u"中风"
        else:
            wind_str = u"低风"

        stateStr += u"\n风速：" +(wind_str)
        stateStr += u"\n工作模式：" +self.air.mode
        stateStr += u"\n消费金额：" +str(self.air.totalMoney)

        self.stateBrowser.setText(str(stateStr))

    #修改目标温度参数
    def setTemp(self):
        temperature = float(self.temperaBox.value())
        on_tips_string = u"您设置了空调温度：" + str(temperature)
        self.tipLabel.setText(on_tips_string)

        status = {'finalTemp':temperature}
        self.air.change_status(status)

    def cancelTemp(self):
        on_tips_string = u"成功取消目标温度更改"
        self.tipLabel.setText(on_tips_string)

        self.temperaBox.setValue(self.air.finalTemp)
        self.tempSlider.setValue(self.air.finaltemp)

    def changetemp(self,value):
        self.temperaBox.setValue(value)



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
            print opStr
            operate = opStr.split("_")

            if operate[0] == 'start' and len(operate) == 7 and operate[-1] == '$':
                self.client.air.recv_start(operate)
                print 'first_start!'
                opStr = ''
                print operate
            if operate[0] == 'a' and len(operate) == 11 and operate[-1] == '$':
                self.client.air.recv_a(operate)
                opStr = ''
                print "received an a"

            if operate[0] == 'close' and len(operate) == 4 and operate[-1] == '$':
                self.client.air.recv_close(operate)
                opStr = ''
                print operate
            if operate[0] == 'sleep' and len(operate) == 3 and operate[-1] == '$':
                self.client.air.recv_sleep(operate)
                opStr = ''
                print operate
                # 待机
            if operate[0] == 'wait' and len(operate) == 5 and operate[-1] == '$':
                self.client.air.recv_wait(operate)
                opStr = ''
                # 阻塞，等待服务
            self.client.showState()

            if time.time() - self.client.air.startTime > 5 and time.time() - self.client.air.startTime < 6:
                sendBuf = self.client.air.send_change()
                self.sock.send(sendBuf)
                time.sleep(1)

            time.sleep(0.1)
        self.sock.close()

'''
if __name__ == '__main__':
    ##ui
    sock_flag = 0;
    app = QtGui.QApplication(sys.argv)
    #client = Client()
    #client.show();
    sys.exit(app.exec_())
'''
