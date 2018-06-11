#-*- coding:utf-8 -*-
import SocketServer
import time
from AirService import *
from setrateui import *
from checkoutui import *
from formui import *
from algo import *
import sqlite3
import threading
import sys
from PyQt4 import QtCore, QtGui, uic

# 1 Set Host and Port
HOST, PORT = "127.0.0.1", int(233)

# Ui Init
qtCreatorFile = "./server.ui"  # Window File
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

global serverui
#global airserver
global onOff
global sockList
global algo

onOff=1
algo = Algo()
airList = []

class Server(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self,server):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # 连接信号和槽
        self.onBtn.clicked.connect(self.onOff)
        self.checkoutBtn.clicked.connect(self.checkOut)
        self.setBtn.clicked.connect(self.setRate)
        self.formBtn.clicked.connect(self.printForm)

    def setRate(self):
        self.setrate = setrateUI()
        self.setrate.show()

        if(self.setrate.exec_()):
            print self.setrate.lowrate
            print self.setrate.midrate
            print self.setrate.highrate


    def serverState(self):
        serverStr = ''
        serverStr += u'\n工作模式：\n模式明明是全局的啊\n'
        serverStr += u'\n工作状态 \n我想想啊\n '
        serverStr += u'\n当前时间：\n' + str(time.time())
        self.serverLab.setText(serverStr)

    def printForm(self):
        self.formui = formUI()
        self.formui.show()
        #self.formui.exec_()

    def checkOut(self):
        self.checkoutui = checkoutUI()
        self.checkoutui.show()

        if(self.checkoutui.exec_()):
            #从队列里找到self.checkoutui.room对应的airserver 再sendclose
            pass

    def showState(self,status):

        # 房间号，目标温度，当前温度，风速，累计的费用，累计的时长。
        if (status['wind'] == 3):
            status['wind'] = u'高风'
        elif (status['wind'] == 2):
            status['wind'] = u'中风'
        else:
            status['wind'] = u'低风'

        showBuf =u'房间号:{room}\n目标温度:{finalTemp}\n当前温度:{currentTemp}\n风速:{wind}\n累计费用:{totalMoney}\n累计时长:{totalTime}\n累计电量:{totalElec}'

        room = status['room']
        showBuf = showBuf.format(**status)

        if room == '306C':
            self.C306Lab.setText(showBuf)
        elif room == '306D':
            self.D306Lab.setText(showBuf)
        elif room == '307C':
            self.C307Lab.setText(showBuf)

        '''
        '306D'
        '307C'
        '307D'
        '308C'
        '308D'
        '309C'
        '309D'
        '310C'
        '''
    def showRoomState(self,room,state):

        #房间号，目标温度，当前温度，风速，累计的费用，累计的时长。
        client_str = room + ' is ' + state
        if room == '306C':
            self.C306Lab.setText(client_str)
        elif room == '306D':
            self.D306Lab.setText(client_str)
        elif room == '307C':
            self.C307Lab.setText(client_str)

    def onOff(self):
        if(onOff == 1):##开机啦
            on_tips_string = u"您开启了空调服务器啦！"
            self.display.setText(on_tips_string)
            self.serverState()

            # 2 Start Server
            server_thread = threading.Thread(target=server.serve_forever)
            server_thread.setDaemon(True)
            server_thread.start()
        else:##按的关机
            onOff == 0
            on_tips_string = u"您关闭了空调服务器啦！"
            self.display.setText(on_tips_string)

            server.shutdown()



class HandleCheckin(SocketServer.StreamRequestHandler):
    # 3 Call this function when recv a connection from client
    def handle(self):
        #req = self.request
        #self.objAir = airserver
        self.objAir = AirService()
        airList.append(self.objAir)

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
                algo.req_server(self.objAir.room)
                opStr = ''
                print operate
            if operate[0] == 'c' and operate[-1] == '$':
                self.objAir.recv_change(operate)
                opStr = ''
                print '[change]',operate
            if operate[0] == 'close' and operate[-1] == '$':
                algo.remove_server(self.objAir.room)
                self.objAir.recv_close(operate)
                serverui.showRoomState(self.objAir.room,'closed')
                opStr = ''
                #待机

            time.sleep(0.1)


    def work(self):
        global algo
        print '[work start]'
        
        while(1):
            time.sleep(0.2)
            if not self.objAir.open:
                algo.remove_server(self.objAir.room)
                continue

            if self.objAir.sleep:
                algo.remove_server(self.objAir.room)
                serverui.showRoomState(self.objAir.room,'sleeping')
                continue

            if self.objAir.room in algo.waitList:
                serverui.showRoomState(self.objAir.room,'waiting')

            if self.objAir.room in algo.serverList:
                self.objAir.work()
                if self.objAir.open and not self.objAir.sleep:
                    algo.req_server(self.objAir.room)

                # 房间号，目标温度，当前温度，风速，累计的费用，累计的时长。
                status = {'room': self.objAir.room,
                          'currentTemp': self.objAir.currentTemp,
                          'finalTemp': self.objAir.finalTemp,
                          'wind': self.objAir.wind,
                          'totalMoney': self.objAir.totalMoney,
                          'totalElec': self.objAir.totalElec,
                          'totalTime': str(int(time.time() - self.objAir.startTime))+'s'}
                serverui.showState(status)

                sendBuf = self.objAir.send_answer()
                #print '[send]', sendBuf
                self.request.sendall(sendBuf)
                time.sleep(0.1)

                sendBuf = self.objAir.is_sleep()
                if sendBuf != False and sendBuf != None:
                    self.request.sendall(sendBuf)
                    algo.remove_server(self.objAir.room)
                    print '[send]', sendBuf
                    continue

            


class ThreadedServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

if __name__ == "__main__":
    read_setting()
    server = ThreadedServer((HOST, PORT), HandleCheckin)
    server.allow_reuse_address = True

    app = QtGui.QApplication(sys.argv)
    #airserver = AirService()
    serverui = Server(server)
    serverui.show()


    if app.exec_():
        server.shutdown()
        sys.exit(True)

