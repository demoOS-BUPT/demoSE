#-*- coding:utf-8 -*-
import socket
import time

# Socket Init
HOST, PORT = "127.0.0.1", int(2333)
room = 503
currentTemp = 15
finalTemp = 25
wind = 2

class Air(object):

    def __init__(self, room=503, currentTemp=15, finalTemp=25, wind=2):
        self.room = room
        self.currentTemp = currentTemp
        self.finalTemp = finalTemp
        self.wind = wind
        self.totalMoney = 0.0
        self.perMoney = 1.0

    def change_status(self, **kwargs):
        if 'room' in kwargs:
            self.room = kwargs['room']
        if 'currentTemp' in kwargs:
            self.currentTemp = kwargs['currentTemp']
        if 'finalTemp' in kwargs:
            self.finalTemp = kwargs['finalTemp']
        if 'wind' in kwargs:
            self.wind = kwargs['wind']

    def show_status(self):
        print 'room:', self.room, 'currentTemp:', self.currentTemp, 'finalTemp:', self.finalTemp, 'wind:', self.wind

    def send_status(self):
        sendBuf = 'r_' + str(self.room) + '_' + str(self.currentTemp) + '_' + str(self.finalTemp) + '_' + str(self.wind)
        return sendBuf



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
    		#close
    	if operate[0] == 'sleep' and len(operate) == 2:
    		opStr = ''
    		#待机
    	if operate[0] == 'wait' and len(operate) == 3:
    		opStr = ''
    		#啥是等待？

    	


    	if 1 == 0:
    		sendBuf = "aloha～"
    		sock.send(sendBuf)
    		print sendBuf

    	time.sleep(0.1)
    sock.close()
