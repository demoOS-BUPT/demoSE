#-*- coding:utf-8 -*-
import SocketServer
import time
from AirService import *
from setrateui import *
from formui import *
import sqlite3
import threading
import sys
from PyQt4 import QtCore, QtGui, uic

# 1 Set Host and Port
HOST, PORT = "127.0.0.1", int(233)

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
        self.setBtn.clicked.connect(self.setRate)
        self.formBtn.clicked.connect(self.printForm)

    def setRate(self):
        self.setrate = setrateUI()
        self.setrate.show()

        if(self.setrate.exec_()):
            print self.setrate.lowrate
            print self.setrate.midrate
            print self.setrate.highrate
            print self.setrate.schedule
            print self.setrate.mode

    def printForm(self):
        self.formui = formUI()
        self.formui.show()
        #self.formui.exec_()

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
        #req = self.request
        self.objAir = AirService()

        operate = self.request.recv(1024).strip().split("_")
        if operate[0] != 'start' or operate[-1] != '$':
            print '[error]recv start error!'
            return
        else:
            print '[recv]start'
            self.objAir.recv_start(operate)

            sendBuf = self.objAir.send_start()
            self.request.sendall(sendBuf)
            print '[send] start', sendBuf
            time.sleep(0.5)

        t1 = threading.Thread(target=self.listen, name='listen')
        t2 = threading.Thread(target=self.work, name='work')
        t1.start()
        t2.start()
        t1.join()
        t2.join()


    def listen(self):
        
        opStr = ''
        operate = []

        while 1:

            res = self.request.recv(1024).strip()

            opStr += res
            operate = opStr.split("_")
            print operate

            if operate[0] == 'r' and operate[-1] == '$':
                self.objAir.recv_first_open(operate)
                opStr = ''
                print operate
            if operate[0] == 'c' and operate[-1] == '$':
                self.objAir.recv_change(operate)
                opStr = ''
                print '[change]',operate
            if operate[0] == 'close' and operate[-1] == '$':
                self.objAir.recv_close(operate)
                opStr = ''
                #待机

            time.sleep(0.1)


    def work(self):
        print '[work start]'
        
        while(1):
            if not self.objAir.open:
                continue

            self.objAir.work()

            if not self.objAir.sleep:
                sendBuf = self.objAir.send_answer()
                #print '[send]', sendBuf
                self.request.sendall(sendBuf)
                time.sleep(0.1)

            sendBuf = self.is_sleep()
            if sendBuf != False and sendBuf != None:
                self.request.sendall(sendBuf)
                print '[send]', sendBuf
                continue

            


class ThreadedServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

if __name__ == "__main__":
    read_setting()
    server = ThreadedServer((HOST, PORT), HandleCheckin)
    server.allow_reuse_address = True

    app = QtGui.QApplication(sys.argv)
    serverui = Server(server)
    serverui.show()

    if app.exec_():
        server.shutdown()
        sys.exit(True)

