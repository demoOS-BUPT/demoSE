#-*- coding:utf-8 -*-
import socket
import time
import threading
from Air import *
# Socket Init
HOST, PORT = "127.0.0.1", int(2333)
room = 503
currentTemp = 15
finalTemp = 25
wind = 1

# -*- coding:utf-8 -*-
import socket
import time
import sys
from PyQt4 import QtCore, QtGui, uic

# Ui Init
qtCreatorFile = "client.ui"  # Window File
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

# Socket Init
HOST, PORT = "127.0.0.1", int(2333)
room = 503
currentTemp = 15
finalTemp = 25
wind = 2

sock_flag = 0;

class Client(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # 连接信号和槽
        self.offBtn.clicked.connect(self.off)
        self.onBtn.clicked.connect(self.on)

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.t = myThread(self.sock)

    def on(self):
        temperature = float(self.temperaBox.value())
        on_tips_string = u"您设置了空调温度：" + str(temperature)
        self.tipLabel.setText(on_tips_string)

        # Connect to Server
        self.sock.connect((HOST, PORT))
        time.sleep(0.2)

        air = Air()
        air.show_status()
        sendBuf = air.send_status()
        self.sock.send(sendBuf.encode(encoding="utf-8"))

        '''
        ################处理一下此时服务器没开的情况
        '''

        ##开始线程处理和服务器间的通信啦'''#
        '''
        self.t = threading.Thread(target=run(self.sock))
        self.t = setDaemon(True)
        self.t.start()
        '''
        sock_flag = 1
        self.t.start()

    def off(self):
        off_tips_string = u"耶 终于关空调了"
        self.tipLabel.setText(off_tips_string)
        sock_flag=0;
        self.sock.close()


class myThread(threading.Thread):  # 继承父类threading.Thread
    def __init__(self, sock):
        threading.Thread.__init__(self)
        self.sock = sock
    def run(self):
        opStr = ''
        while sock_flag:
            res = self.sock.recv(1024)
            opStr += res.decode()
            operate = opStr.split("_")

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
    app = QtGui.QApplication(sys.argv)
    client = Client()
    client.show()

    sys.exit(app.exec_())

