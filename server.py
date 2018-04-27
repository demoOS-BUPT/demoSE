#-*- coding:utf-8 -*-
import SocketServer
import time
from Air import *
import sqlite3
import threading
import sys
from PyQt4 import QtCore, QtGui, uic

# 1 Set Host and Port
HOST, PORT = "127.0.0.1", int(2333)

# Ui Init
qtCreatorFile = "./server.ui"  # Window File
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class Server(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self,server):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # 连接信号和槽
        self.onBtn.clicked.connect(self.on)
        self.offBtn.clicked.connect(self.off)

    def on(self):
        #temperature = float(self.temperaBox.value())
        on_tips_string = u"您开启了空调服务器啦！"
        self.display.setText(on_tips_string)

        # 2 Start Server
        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.setDaemon(True)
        server_thread.start()

    def off(self):
        server.shutdown()

class HandleCheckin(SocketServer.StreamRequestHandler):
    # 3 Call this function when recv a connection from client
    def handle(self):
        # 4 Send the question
        # 初次开机，注意startTime字段在此次保存
        opStr = ""
        req = self.request
        res = req.recv(1024)
        opStr += res.decode()
        operate = opStr.split("_")


        if operate[0] != 'r' or len(operate) != 5:
            print( 'connect the air error!')
            return
        objAir = Air(room=operate[1], currentTemp=float(operate[2]), finalTemp=float(operate[3]), wind=int(operate[4]))


        opStr = ''
        operate = []
        while 1:
            objAir.work()#模拟运行

            res = req.recv(1024).strip()
            opStr += res
            operate = opStr.split("_")
            if operate[0] == 'r' and len(operate) == 5:
                #开机
                opStr = ''
                print (operate)
            if operate[0] == 'c' and len(operate) == 5:
                opStr = ''
            if operate[0] == 'close' and len(operate) == 2:
                opStr = ''
                #待机
            if operate[0] == 'wait' and len(operate) == 3:
                opStr = ''
                #啥是等待？
            if operate[0] == 'sleep' and len(operate) == 2:
                opStr = ''

            time.sleep(0.1)


class ThreadedServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

if __name__ == "__main__":
    server = ThreadedServer((HOST, PORT), HandleCheckin)
    server.allow_reuse_address = True

    app = QtGui.QApplication(sys.argv)
    serverui = Server(server)
    serverui.show()

    if app.exec_():
        server.shutdown()
        sys.exit(True)

