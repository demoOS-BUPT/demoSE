#-*- coding:utf-8 -*-
import socket
import time
from Air import *
# Socket Init
HOST, PORT = "127.0.0.1", int(2333)
room = 503
currentTemp = 15
finalTemp = 25
wind = 3

if __name__ == '__main__':
    # Connect to Server
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    time.sleep(0.2)

    air = Air()
    air.show_status()    
    sendBuf = air.send_status()
    print sendBuf
    sock.send(sendBuf)
    

    opStr = ''
    while 1:
        res = sock.recv(1024)
        opStr += res
        operate = opStr.split("_")

        if operate[0] == 'a' and len(operate) == 10:
            opStr = ''
            print operate
        if operate[0] == 'close' and len(operate) == 2:
            opStr = ''
            print operate
        if operate[0] == 'sleep' and len(operate) == 2:
            opStr = ''
            #待机
        if operate[0] == 'wait' and len(operate) == 3:
            opStr = ''
            #啥是等待？


        time.sleep(0.1)
    sock.close()
