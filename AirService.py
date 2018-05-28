#-*- coding:utf-8 -*-
import socket
import time
import re, ConfigParser

MODE = '1'
TEMPFROM = '20.0'
TEMPTO = '30.0'
TEMPWIDTH = '2.0'
WIND = '3'
FINALTEMP = '28'
TEMPCHANGE = 1.2

class AirService(object):
    #初始化
    def __init__(self, room=503, currentTemp=15, finalTemp=25, wind=2):
        self.room = room
        self.mode = 'hot'
        self.currentTemp = currentTemp
        self.finalTemp = finalTemp
        self.wind = wind
        self.totalMoney = 0.0
        self.perMoney = 1.2
        self.startTime = int(time.time())
        self.lastTime = int(time.time())
        self.sleep = False
        self.open = True
        self.status_to_money()
        self.is_sleep()

    def init(self, room=503, currentTemp=15, finalTemp=25, wind=2):
        self.room = room
        self.mode = 'hot'
        self.currentTemp = currentTemp
        self.finalTemp = finalTemp
        self.wind = wind
        self.totalMoney = 0.0
        self.perMoney = 1.2
        self.startTime = int(time.time())
        self.lastTime = int(time.time())
        self.sleep = False
        self.open = True
        self.status_to_money()
        self.is_sleep()

    def recv_start(self, operate):
        status = {}
        status['room'] = operate[1]
        self.change_status(status)
        return 

    def recv_first_open(self, operate):
        status = {}
        status['room'] = operate[1]
        status['currentTemp'] = operate[2]
        status['finalTemp'] = operate[3]
        if operate[3] == '#':
            status['finalTemp'] = FINALTEMP
        status['wind'] = operate[4]
        if operate[4] == '#':
            status['finalTemp'] = WIND
        self.change_status(status)
        return 

    def recv_open(self, operate):
        status = {}
        status['room'] = operate[1]
        status['currentTemp'] = operate[2]
        status['finalTemp'] = operate[3]
        status['wind'] = operate[4]
        self.change_status(status)
        return 

    def recv_change(self, operate):
        status = {}
        status['room'] = operate[1]
        status['currentTemp'] = operate[2]
        status['finalTemp'] = operate[3]
        status['wind'] = operate[4]
        self.change_status(status)
        return 

    def recv_close(self, operate):
        print operate[1] + 'closed!'
        return

    def send_start(self):
        sendBuf = 'start_{room}_{mode}_{tempFrom}-{tempTo}_{tempWidth}_$'
        status = {'room':self.room,
                'mode':MODE,
                'tempFrom':TEMPFROM,
                'tempTo':TEMPTO,
                'tempWidth':TEMPWIDTH,
                }
        sendBuf = sendBuf.format(**status)
        return sendBuf

    def send_answer(self):
        sendBuf = 'a_{room}_{currentTemp}_{totalMoney}_{time}_{finalTemp}_{wind}_{tempChange}_{preMoney}_{totalElec}_$'
        status = {'room':self.room,
                    'currentTemp':self.currentTemp,
                    'totalMoney':self.totalMoney,
                    'time':time.time(),
                    'finalTemp': self.finalTemp,
                    'wind':self.wind,
                    'tempChange':TEMPCHANGE,
                    'preMoney':self.preMoney,
                    'totalElec':self.totalElec}
        sendBuf = sendBuf.format(**status)
        return sendBuf

    def send_close(self, flag):
        #退房标识
        sendBuf = 'close_{room}_{flag}_$'
        status = {'room':self.room,
                    'flag':flag}
        sendBuf = sendBuf.format(**status)
        return sendBuf

    def send_sleep(self):
        sendBuf = 'sleep_{room}_$'
        status = {'room':self.room}
        sendBuf = sendBuf.format(**status)
        return sendBuf

    def send_wait(self, waitNum, waitType):
        #调度
        sendBuf = 'wait_{room}_{num}_{type}_$'
        status = {'room':self.room,
                    'num':waitNum,
                    'type':waitType,}
        sendBuf = sendBuf.format(**status)



    #改变状态,这里把参数补齐
    def change_status(self, kwargs):
        if 'room' in kwargs:
            self.room = kwargs['room']
        if 'currentTemp' in kwargs:
            self.currentTemp = kwargs['currentTemp']
        if 'finalTemp' in kwargs:
            self.finalTemp = kwargs['finalTemp']
        if 'wind' in kwargs:
            self.wind = kwargs['wind']

    #test：展示状态
    def show_status(self):
        #print 'room:', self.room, 'currentTemp:', self.currentTemp, 'finalTemp:', self.finalTemp, 'wind:', self.wind
        print dir(self)



    #模拟运行
    def work(self):
        nowTime = int(time.time())
        #先确认状态
        self.status_to_money()

        #模拟运行
        if nowTime == self.lastTime:
            return
        
        if not self.is_sleep():
            #正常运行
            self.currentTemp += (nowTime - self.lastTime) * self.wind
            self.totalMoney += (nowTime - self.lastTime) * self.perMoney
        else:
            #睡眠了，不该运行
            self.currentTemp -= COLD * (nowTime - self.lastTime)
            print self.currentTemp

        self.lastTime = nowTime


    #风速转每秒的钱数
    def status_to_money(self):
        #根据风速得到每秒钱数，这里后面替换为ConfigParser
        if self.currentTemp == self.finalTemp:
            self.perMoney = 0
            return
        if self.wind == 1:
            self.perMoney = 0.5
        elif self.wind == 2:
            self.perMoney = 1
        elif self.wind == 3:
            self.perMoney = 2

    #是否该休眠
    def is_sleep(self):
        if self.sleep == False:
            if self.currentTemp > self.finalTemp:
                print 'time to sleep~'
                self.sleep = True
        else:
            if self.currentTemp < self.finalTemp - 5:
                print 'time to get up~'
                self.sleep = False
        return self.sleep


    def is_sleep_2(self):
        if self.sleep == False:
            if self.mode=='hot':
                if self.currentTemp>self.finalTemp:
                    print 'time to sleep~'
                    self.sleep = True
            elif self.mode=='cold':
                if self.currentTemp<self.finalTemp:
                    print 'time to sleep~'
                    self.sleep = True
        else:
            if self.mode=='hot':
                if self.currentTemp<self.finalTemp-localTempRange:
                    print 'time to get up~'
                    self.sleep = False
            elif self.mode=='cold':
                if self.currentTemp>self.finalTemp+localTempRange:
                    print 'time to get up~'
                    self.sleep = False
        return self.sleep