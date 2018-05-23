#-*- coding:utf-8 -*-
import SocketServer, time
import sqlite3
from AirService import *
    
class HandleCheckin(SocketServer.StreamRequestHandler):
    # 3 Call this function when recv a connection from client
    def handle(self):
        # 4 Send the question
        req = self.request

        #初次开机，注意startTime字段在此次保存
        operate = req.recv(1024).strip().split("_")
        if operate[0] != 'start' or operate[-1] != '$':
            print 'connect the air error!'
            return
        print operate
        objAir = AirService()

        req.sendall(objAir.send_start())

        opStr = ''
        operate = []
        while 1:
            objAir.work()#模拟运行

            res = req.recv(1024).strip()
            opStr += res
            operate = opStr.split("_")
            if operate[0] == 'r' and operate[-1] == '$':
                objAir.recv_first_open(operate)
                opStr = ''
                print operate
            if operate[0] == 'c' and operate[-1] == '$':
                objAir.recv_change(operate)
                opStr = ''
                print operate
            if operate[0] == 'close' and operate[-1] == '$':
                objAir.recv_close(operate)
                opStr = ''
                #待机

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
