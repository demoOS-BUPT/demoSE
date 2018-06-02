#-*- coding:utf-8 -*-
import SocketServer, time, threading
import sqlite3

from AirService import *
    
class HandleCheckin(SocketServer.StreamRequestHandler):
    def handle(self):
        req = self.request
        operate = req.recv(1024).strip().split("_")
        if operate[0] != 'start' or operate[-1] != '$':
            print 'connect the air error!'
            return
        print '[recv] start'
        self.objAir = AirService()

        req.sendall(self.objAir.send_start())
        print '[send] start'

        t1 = threading.Thread(target=self.listen, name='listen')
        t2 = threading.Thread(target=self.work, name='work')
        t1.start()
        t2.start()
        t1.join()
        t2.join()


    def listen(self):
        req = self.request        

        opStr = ''
        operate = []

        ii = 0
        while 1:

            res = req.recv(1024).strip()

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
            ii+=1
            if ii > 10:
                exit()

    def work(self):
        print '[work start]'
        req = self.request
        jj = 0
        while(1):
            sendBuf = self.objAir.work()
            print sendBuf
            if sendBuf != False and sendBuf != None:
                req.sendall(sendBuf)
                print '[send]' + sendBuf
            time.sleep(0.2)
            jj += 1
            if jj >= 150:
                exit()
            print '[work loop]'



class ThreadedServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

if __name__ == "__main__":
    # 1 Set Host and Port
    read_setting()
    HOST, PORT = "0.0.0.0", int(8000)

    # 2 Start Server
    server = ThreadedServer((HOST, PORT), HandleCheckin)
    server.allow_reuse_address = True
    server.serve_forever()
