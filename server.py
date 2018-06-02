#-*- coding:utf-8 -*-
import SocketServer, time, threading
import sqlite3

from AirService import *
    
class HandleCheckin(SocketServer.StreamRequestHandler):
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
            time.sleep(0.1)

            if not self.objAir.open:
                continue

            sendBuf = self.objAir.work()
            if sendBuf != False and sendBuf != None:
                self.request.sendall(sendBuf)
                print '[send]', sendBuf
                continue

            if not self.objAir.sleep:
                sendBuf = self.objAir.send_answer()
                #print '[send]', sendBuf
                self.request.sendall(sendBuf)


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
