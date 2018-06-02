#-*- coding:utf-8 -*-
import socket
import time
from AirClient import *
# Socket Init
HOST, PORT = "127.0.0.1", int(8000)
cold = 0.1

if __name__ == '__main__':
    # Connect to Server
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    sock.setblocking(0)
    time.sleep(0.2)

    air = AirClient()
    status={'room':'307C',
            'currentTemp':20.3,
            'finalTemp':24.0,
            'wind':'2',#中速
            }
    air.change_status(status)

    sendBuf = air.send_start()
    print '[send]',sendBuf
    sock.send(sendBuf)

    time.sleep(0.2)
    opStr = sock.recv(1024)
    operate = opStr.split("_")
    if operate[0] == 'start' and len(operate) == 6 and operate[-1] == '$':
        air.recv_start(operate)
        print '[recv]first start!'
        opStr = ''
    else:
        print '[error]recv first start error!'
        exit()

    sendBuf = air.send_first_open()
    print '[send]',sendBuf
    sock.send(sendBuf)

    starttime = time.time()
    #print starttime
    time.sleep(0.2)

    air.show_status()
    print '--------connect success---------'

    opStr = ''
    while 1:
        try:
            res = sock.recv(1024)
        except:
            res = ''
        if res != '':
            # a 太多了
            if res[0] != 'a':
                print '[recv]', res
        opStr += res
        #print opStr
        operate = opStr.split("_")

        
            
        if operate[0] == 'a' and len(operate) == 11 and operate[-1] == '$':
            air.recv_a(operate)

        if operate[0] == 'close' and len(operate) == 4 and operate[-1] == '$':
            air.recv_close(operate)

        if operate[0] == 'sleep' and len(operate) == 3 and operate[-1] == '$':
            air.recv_sleep(operate)

            #待机
        if operate[0] == 'wait' and len(operate) == 5 and operate[-1] == '$':
            air.recv_wait(operate)

        opStr = ''

        air.show_status()

        sendBuf = air.work()
        if sendBuf != '' and sendBuf != False and sendBuf != None:
            sock.send(sendBuf)

        #调试用
        if time.time() - starttime > 5 and time.time() - starttime < 6:
            sendBuf = ''#air.send_change()
            #sock.send(sendBuf)
            #time.sleep(1)

        time.sleep(0.1)
    sock.close()
