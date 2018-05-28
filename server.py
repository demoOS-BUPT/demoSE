#-*- coding:utf-8 -*-
import SocketServer, time
import sqlite3
from AirClient import *

    
class HandleCheckin(SocketServer.StreamRequestHandler):
    # 3 Call this function when recv a connection from client
    def handle(self):
        # 4 Send the question
        req = self.request

        #初次开机，注意startTime字段在此次保存
        operate = req.recv(1024).strip().split("_")
        if operate[0] != 'r' or len(operate) != 5:
            print 'connect the air error!'
            return
        objAir = AirClient(room=operate[1], currentTemp=float(operate[2]), finalTemp=float(operate[3]), wind=int(operate[4]))


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
                print operate
            if operate[0] == 'c' and len(operate) == 5:
                opStr = ''
            if operate[0] == 'close' and len(operate) == 2:
                opStr = ''
                #待机
            if operate[0] == 'wait' and len(operate) == 3:
                opStr = ''
                #啥是等待？

            time.sleep(0.1)


class ThreadedServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

if __name__ == "__main__":
    # 1 Set Host and Port
    HOST, PORT = "0.0.0.0", int(8000)

    # 2 Start Server
    server = ThreadedServer((HOST, PORT), HandleCheckin)
    server.allow_reuse_address = True
    server.serve_forever()
