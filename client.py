#-*- coding:utf-8 -*-
import socket
import time
import sys
from PyQt4 import QtCore, QtGui
import threading
from AirClient import *

import sys
sys.path.append("./ui/")
from clientui import *
from ReadConfig import *


# Socket Init
HOST, PORT = "127.0.0.1", int(233)

HIGHWIND = 3
MIDWIND = 2
LOWWIND = 1

sock_flag = 0
first_open = 1

class Client(QtGui.QMainWindow):


    def __init__(self,user,parent=None):
        super(Client, self).__init__(parent)
        self.clientUI= Ui_MainWindow()
        self.clientUI.setupUi(self)


        self.room = user

        if DEFAULT_WIND == "1":
            self.clientUI.lowBtn.setChecked(True)
        elif DEFAULT_WIND == "2":
            self.clientUI.midBtn.setChecked(True)
        elif DEFAULT_WIND == "3":
            self.clientUI.highBtn.setChecked(True)


        # 设置温度控件的最大最小值
        self.clientUI.tempSlider.setMinimum(TEMP_FROM)
        self.clientUI.tempSlider.setMaximum(TEMP_TO)
        self.clientUI.temperaBox.setMinimum(TEMP_FROM)
        self.clientUI.temperaBox.setMaximum(TEMP_TO)

        # 设置温度条控件的初始值
        self.clientUI.tempSlider.setValue(int(DEFAULT_TEMP))
        self.clientUI.temperaBox.setValue(float(DEFAULT_TEMP))

        # 连接信号和槽
        self.clientUI.tempSlider.valueChanged[int].connect(self.changeBoxTemp)
        self.clientUI.temperaBox.valueChanged[float].connect(self.changeSliderTemp)
        self.clientUI.oBtn.clicked.connect(self.onOroff)

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((HOST, PORT))
        self.sock.setblocking(0)
        self.t = myThread(self.sock, self)

    def setTime(self,t):
        s = str(self.air.room) + u"房间的顾客您好呀! \nwe offering simple and comfort here~"
        t = time.strftime("%Y-%m-%d %H:%M:%S",time.strptime(t,"%Y/%m/%d/%H/%M/%S"))
        s += (u"\n当前时间为：" + str(t))
        self.clientUI.roomLabel.setText(s)

    def onOroff(self):
        global sock_flag
        global first_open
        if(sock_flag == 0):

            if first_open:
                finalTemp = float(self.clientUI.temperaBox.value())
                on_tips_string = u"您设置了空调温度：" + str(finalTemp)
                self.clientUI.tipLabel.setText(on_tips_string)

                win = self.getWind()
                time.sleep(0.2)

                self.air = AirClient()
                status={'room':self.room,
                        'currentTemp':20.3,
                        'finalTemp':float(self.clientUI.temperaBox.value()),
                        'wind':win,
                        }
                self.air.change_status(status)

                ##开机
                sendBuf = self.air.send_start()
                self.sock.send(sendBuf)
                print sendBuf

                time.sleep(0.2)
                opStr = self.sock.recv(1024)
                operate = opStr.split("_")
                if operate[0] == 'start' and len(operate) == 6 and operate[-1] == '$':
                    self.air.recv_start(operate)
                    print '[recv]first start!'
                else:
                    print '[error]recv first start error!'
                    exit()

                self.clientUI.highBtn.toggled[bool].connect(self.highBtnSlot)
                self.clientUI.midBtn.toggled[bool].connect(self.midBtnSlot)
                self.clientUI.lowBtn.toggled[bool].connect(self.lowBtnSlot)

            self.air.show_status()
            sendBuf = self.air.send_first_open()
            print sendBuf
            self.sock.send(sendBuf)
            time.sleep(0.2)

            sock_flag = 1
            if first_open:
                self.t.start()
                first_open = 0

            self.clientUI.tabWidget.setCurrentIndex(0)

            s = str(self.air.room) + u"房间的顾客您好呀! \nwe offering simple and comfort here~"
            t = time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime(time.time()))
            s += (u"\n当前时间为：" + str(t))
            self.clientUI.roomLabel.setText(s)

            self.clientUI.oBtn.setText(u"关机")


        else:#关空调

            off_tips_string = u"耶 终于关空调了"
            self.clientUI.tipLabel.setText(off_tips_string)

            self.clientUI.oBtn.setText(u"开机")

            sendBuf = self.air.send_close()
            self.sock.send(sendBuf)

            sock_flag = 0

            s=''
            self.clientUI.roomLabel.setText(s)
            #self.sock.close()

            self.clientUI.tabWidget.setCurrentIndex(2)

    def printDetail(self):
        self.clientUI.tabWidget.setCurrentIndex(1)

    def showState(self):
        stateStr = ""
        stateStr += u"\n当前温度："+(str(self.air.currentTemp))
        stateStr += u"\n目标温度：" +(str(self.air.finalTemp))
        stateStr += u"\n风速：" + self.getWindStr()
        stateStr += u"\n工作模式：" +self.air.mode
        stateStr += u"\n消费金额：" +str(self.air.totalMoney)
        self.clientUI.showLab.setText(stateStr)

    #修改目标温度参数
    def setTemp(self):
        temperature = float(self.clientUI.temperaBox.value())
        on_tips_string = u"您设置了空调温度：" + str(temperature)
        self.clientUI.tipLabel.setText(on_tips_string)

        status = { 'finalTemp': temperature,
                  }
        self.air.change_status(status)
        sendBuf = self.air.send_change()
        self.sock.send(sendBuf)

    def cancelTemp(self):
        on_tips_string = u"成功取消目标温度更改"
        self.clientUI.tipLabel.setText(on_tips_string)

        self.clientUI.temperaBox.setValue(self.air.finalTemp)
        self.clientUI.tempSlider.setValue(self.air.finaltemp)

    def changeBoxTemp(self,value):
        self.clientUI.temperaBox.setValue(value)
        if sock_flag :
            self.setTemp()

    def changeSliderTemp(self, value):
        self.clientUI.tempSlider.setValue(int(value))

    def highBtnSlot(self):
        if (self.clientUI.highBtn.isChecked()):
            status = {'wind': HIGHWIND,  # 高速
                      }
            self.air.change_status(status)
            sendBuf = self.air.send_change()
            self.sock.send(sendBuf)

    def midBtnSlot(self):
        if (self.clientUI.midBtn.isChecked()):
            status = {'wind': MIDWIND,  # 中速
                      }
            self.air.change_status(status)
            sendBuf = self.air.send_change()
            self.sock.send(sendBuf)

    def lowBtnSlot(self):
        if (self.clientUI.lowBtn.isChecked()):
            status = {'wind': LOWWIND,  # 中速
                      }
            self.air.change_status(status)
            sendBuf = self.air.send_change()
            self.sock.send(sendBuf)

    def getWind(self):
        if (self.clientUI.highBtn.isChecked()):
            wind = HIGHWIND
        elif (self.clientUI.midBtn.isChecked()):
            wind = MIDWIND
        else:
            wind = LOWWIND
        return wind

    def getWindStr(self):
        if (self.clientUI.highBtn.isChecked()):
            wind_str = u'高风'
        elif (self.clientUI.midBtn.isChecked()):
            wind_str = u'中风'
        else:
            wind_str = u'低风'
        return wind_str



class myThread(threading.Thread):  # 继承父类threading.Thread
    def __init__(self,sock,client):
        super(myThread, self).__init__()
        self.sock = sock
        self.client = client
    def run(self):

        global sock_flag
        opStr = ''

        #while sock_flag:
        while 1:
            try:
                res = self.sock.recv(1024)
            except:
                res = ''
            if res != '':
                print '[recv]', res
            opStr += res
            #print opStr
            operate = opStr.split("_")


            if operate[0] == 'a' and len(operate) == 11 and operate[-1] == '$':
                self.client.air.recv_a(operate)
                self.client.setTime(operate[4])

            if operate[0] == 'close' and len(operate) == 4 and operate[-1] == '$':
                self.client.air.recv_close(operate)
                self.client.printDetail()

            if operate[0] == 'sleep' and len(operate) == 3 and operate[-1] == '$':
                self.client.air.recv_sleep(operate)

                #待机
            if operate[0] == 'wait' and len(operate) == 5 and operate[-1] == '$':
                self.client.air.recv_wait(operate)


            opStr = ''

            sendBuf = self.client.air.work()
            if sendBuf != '' and sendBuf != False and sendBuf != None:
                self.sock.send(sendBuf)
                print '[send]', sendBuf
            
            if time.time() - self.client.air.startTime > 5 and time.time() - self.client.air.startTime < 6 and False:
                sendBuf = self.client.air.send_change()
                self.sock.send(sendBuf)
                time.sleep(1)

            self.client.showState()
            time.sleep(0.1)
        print '我要关闭咯'
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
