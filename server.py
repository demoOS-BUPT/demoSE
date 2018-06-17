#-*- coding:utf-8 -*-
import SocketServer
import time
from AirService import *
from setrate import *
from checkout import *
from form import *

import sys
sys.path.append("./ui/")
from serverui import *
from algo import *
from ReadConfig import *
import sqlite3
import threading
from PyQt4 import QtCore, QtGui
from report import *

# 1 Set Host and Port

HOST, PORT = "127.0.0.1", int(233)


global serverui
#global airserver
global onOff
global sockList
global algo

onOff=1
algo = Algo()
airList = []


class Server(QtGui.QMainWindow):
    def __init__(self,server,parent=None):
        super(Server, self).__init__(parent)

        self.serverUI = Ui_Serverui()
        self.serverUI.setupUi(self)
        # 连接信号和槽
        self.serverUI.onBtn.clicked.connect(self.onOff)
        self.serverUI.onBtn.setText(u"开机")

        self.serverUI.checkoutBtn.clicked.connect(self.checkOut)
        self.serverUI.setBtn.clicked.connect(self.setRate)
        self.serverUI.formBtn.clicked.connect(self.printForm)

    def serverState(self):
        serverStr = ''
        serverStr += u'\n工作模式：\n'+ MODE
        serverStr += u'\n工作状态：'

        if(onOff == 0):
            serverStr += u'\n开机'
        else:
            serverStr += u'\n关机'

        self.serverUI.serverLab.setText(serverStr)

    ######################服务端的更改空调配置，打印报表，前台退房等功能

    def setRate(self):
        self.setrate = setrateUI()
        self.setrate.show()

        if (self.setrate.exec_()):
            print self.setrate.lowrate
            print self.setrate.midrate
            print self.setrate.highrate

    def printForm(self):
        self.formui = formUI()
        self.formui.show()

    def checkOut(self):
        self.checkoutui = checkoutUI()
        self.checkoutui.show()
        if(self.checkoutui.exec_()):
            #从队列里找到self.checkoutui.room对应的airserver 再sendclose
            global checkoutList
            print checkoutList
            print '[sync] checkoutList'


    ######################

    ######################展示房间状态

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

        self.everyRoomLab(room,showBuf)

    def showRoomState(self,room,state):

        #房间号，目标温度，当前温度，风速，累计的费用，累计的时长。
        showBuf = room + ' is ' + state
        self.everyRoomLab(room, showBuf)

    def everyRoomLab(self, room, showBuf):
        if room == '306C':
            self.serverUI.C306Lab.setText(showBuf)
        elif room == '307C':
            self.serverUI.C307Lab.setText(showBuf)
        elif room == '306D':
            self.serverUI.D306Lab.setText(showBuf)
        elif room == '307D':
            self.serverUI.D307Lab.setText(showBuf)
        elif room == '308C':
            self.serverUI.C308Lab.setText(showBuf)
        elif room == '308D':
            self.serverUI.D308Lab.setText(showBuf)
        elif room == '309C':
            self.serverUI.C309Lab.setText(showBuf)
        elif room == '309D':
            self.serverUI.D309Lab.setText(showBuf)
        elif room == '310C':
            self.serverUI.C310Lab.setText(showBuf)

    ######################

    def onOff(self):
        global onOff
        if(onOff == 1):##开机啦
            on_tips_string = u"您开启了空调服务器啦！"
            self.serverUI.display.setText(on_tips_string)
            self.serverState()

            # 2 Start Server
            server_thread = threading.Thread(target=server.serve_forever)
            server_thread.setDaemon(True)
            server_thread.start()
            self.serverUI.onBtn.setText(u"关机")
            onOff = 0

        else:##按的关机

            self.serverUI.onBtn.setText(u"开机")
            on_tips_string = u"您关闭了啦！"
            self.serverUI.display.setText(on_tips_string)

            server.shutdown()
            onOff = 1
        self.serverState()

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
                if operate[3]=='#'and operate[4]=='#':
                    self.objAir.recv_first_open(operate)
                else:
                    self.objAir.recv_open(operate)
                algo.req_server(self.objAir.room, self.objAir.wind,self.objAir)
                opStr = ''
                print operate
            if operate[0] == 'c' and operate[-1] == '$':
                self.objAir.recv_change(operate)
                opStr = ''
                print '[change]',operate

            if operate[0] == 'close' and operate[-1] == '$':
                algo.remove_server(self.objAir.room,self.objAir)
                self.objAir.recv_close(operate)
                serverui.showRoomState(self.objAir.room,'closed')
                opStr = ''
                #待机

            time.sleep(0.1)


    def work(self):
        global algo
        global checkoutList
        print '[work start]'


        while(1):
            time.sleep(0.1)
            if self.objAir.room in checkoutList:
                print self.objAir.room+"sleeping"
                checkoutList.remove(self.objAir.room)
                sendBuf = self.objAir.send_close('1')
                print '[close]',sendBuf
                self.request.sendall(sendBuf)
                self.objAir.reset()
                self.objAir.open = False
                self.objAir.sleep = False
                time.sleep(0.2)

            if self.objAir.room in algo.first_wait:
                if algo.first_wait[self.objAir.room] == 0:
                    sendBuf = self.objAir.send_wait('2', '1')
                    self.request.sendall(sendBuf)
                    algo.first_wait[self.objAir.room] = 1
                    time.sleep(0.1)

            if not self.objAir.open:
                serverui.showRoomState(self.objAir.room, 'closed')
                algo.remove_server(self.objAir.room,self.objAir)
                continue

            if self.objAir.sleep:
                algo.remove_server(self.objAir.room,self.objAir)
                serverui.showRoomState(self.objAir.room,'sleeping')
                continue

            if self.objAir.room in algo.waitList:
                serverui.showRoomState(self.objAir.room,'waiting')

            if self.objAir.room in algo.serverList:
                self.objAir.work()
                if self.objAir.open and not self.objAir.sleep:
                    algo.req_server(self.objAir.room, self.objAir.wind,self.objAir)

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
                    algo.remove_server(self.objAir.room,self.objAir)
                    print '[send]', sendBuf
                    continue

            


class ThreadedServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

if __name__ == "__main__":
    server = ThreadedServer((HOST, PORT), HandleCheckin)
    server.allow_reuse_address = True

    app = QtGui.QApplication(sys.argv)
    #airserver = AirService()
    serverui = Server(server)
    serverui.show()


    if app.exec_():
        server.shutdown()
        sys.exit(True)

