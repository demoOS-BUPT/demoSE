#-*- coding:utf-8 -*-
import socket
import time
from AirClient import *
# Socket Init
HOST, PORT = "192.168.43.26", int(8002)
cold = 0.1

if __name__ == '__main__':
    # Connect to Server
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    time.sleep(0.2)

    air = AirClient()
    status={'room':'307C',
            'currentTemp':20.3,
            'finalTemp':28.0,
            'wind':2,#中速
            }
    air.change_status(status)

    sendBuf = air.send_start()
    print sendBuf
    sock.send(sendBuf)

    air.show_status()    
    sendBuf = air.send_first_open()
    print sendBuf
    sock.send(sendBuf)

    starttime = time.time()
    print starttime
    time.sleep(0.2)

    opStr = ''
    while 1:
        res = sock.recv(1024)
        opStr += res
        print opStr
        operate = opStr.split("_")
        if operate[0] == 'start' and len(operate) == 7 and operate[-1] == '$':
            air.recv_start(operate)
            print 'first_start!'
            opStr = ''
            print operate
        if operate[0] == 'a' and len(operate) == 11 and operate[-1] == '$':
            air.recv_a(operate)
            opStr = ''
            print operate
        if operate[0] == 'close' and len(operate) == 4 and operate[-1] == '$':
            air.recv_close(operate)
            opStr = ''
            print operate
        if operate[0] == 'sleep' and len(operate) == 3 and operate[-1] == '$':
            air.recv_sleep(operate)
            opStr = ''
            print operate
            #待机
        if operate[0] == 'wait' and len(operate) == 5 and operate[-1] == '$':
            air.recv_wait(operate)
            opStr = ''
            #阻塞，等待服务
        air.show_status()

        if time.time() - starttime > 5 and time.time() - starttime < 6:
            sendBuf = air.send_change() 
            sock.send(sendBuf)
            time.sleep(1)

        time.sleep(0.1)
    sock.close()
