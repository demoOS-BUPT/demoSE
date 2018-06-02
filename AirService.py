#-*- coding:utf-8 -*-
import socket
import time
import re, ConfigParser

def read_setting():
    cp = ConfigParser.SafeConfigParser()
    cp.read('Air.conf')

    global WIND
    global ELEC_MONEY
    global ELEC_TEMP
    global MODE
    global TEMP_FROM
    global TEMP_TO
    global TEMP_WIDTH

    WIND = [0,float(cp.get('wind','low')), float(cp.get('wind','medium')), float(cp.get('wind', 'high'))]
    ELEC_MONEY = float(cp.get('elec', 'money'))
    ELEC_TEMP = float(cp.get('elec', 'temp'))
    MODE = cp.get('air', 'mode')
    TEMP_FROM = int(cp.get('air', 'tempFrom'))
    TEMP_TO = int(cp.get('air', 'tempTo'))
    TEMP_WIDTH = int(cp.get('air', 'tempWidth'))

    DEFAULT_WIND = cp.get('air', 'defaultWind')
    DEFAULT_TEMP = cp.get('air', 'defaultTemp')

    SYSTEM_TIME = cp.get('system', 'systemTime')

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
        self.totalElec = 0
        self.status_syn()


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
        self.status_syn()
        self.is_sleep()

    def recv_start(self, operate):
        status = {}
        status['room'] = operate[1]
        self.change_status(status)
        return 

    def recv_first_open(self, operate):
        status = {}
        status['room'] = operate[1]
        status['currentTemp'] = float(operate[2])
        status['finalTemp'] = operate[3]
        if operate[3] == '#':
            status['finalTemp'] = DEFAULT_TEMP
        status['wind'] = operate[4]
        if operate[4] == '#':
            status['finalTemp'] = DEFAULT_WIND
        self.change_status(status)
        return 

    def recv_open(self, operate):
        status = {}
        status['room'] = operate[1]
        status['currentTemp'] = float(operate[2])
        status['finalTemp'] = float(operate[3])
        status['wind'] = operate[4]
        self.change_status(status)
        return 

    def recv_change(self, operate):
        status = {}
        status['room'] = operate[1]
        status['currentTemp'] = float(operate[2])
        status['finalTemp'] = float(operate[3])
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
                'tempFrom':TEMP_FROM,
                'tempTo':TEMP_TO,
                'tempWidth':TEMP_WIDTH,
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
                    'tempChange':TEMP_CHANGE,
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
        print 'room:', self.room, 'currentTemp:', self.currentTemp, 'finalTemp:', self.finalTemp, 'wind:', self.wind




    #模拟运行
    def work(self):
        nowTime = int(time.time())
        
        #把风速同步到每秒扣多少钱
        self.status_syn()

        #模拟运行
        if nowTime <= self.lastTime + 3:
            return False

        if not self.sleep:
            print 'running'
            self.show_status()
            #正常运行
            self.totalElec += float(WIND[int(self.wind)])
            self.totalMoney += self.perMoney
            if self.mode == 'hot':
                self.currentTemp += WIND[int(self.wind)] * float(ELEC_TEMP)
            else:
                self.currentTemp -= WIND[int(self.wind)] * float(ELEC_TEMP)
        else:
            #睡眠了，不该运行
            #self.currentTemp -= COLD * (nowTime - self.lastTime)
            print '[sleep]',self.room,'sleeping'

        self.lastTime = nowTime
        sendBuf = self.is_sleep()
        return sendBuf
        


    #风速转每秒的钱数
    def status_syn(self):
        #根据风速得到每秒钱数，这里后面替换为ConfigParser
        if self.wind == 1 or self.wind == '1':
            self.perMoney = float(WIND[0]) * ELEC_MONEY
        elif self.wind == 2 or self.wind == '2':
            self.perMoney = float(WIND[1]) * ELEC_MONEY
        elif self.wind == 3 or self.wind == '3':
            self.perMoney = float(WIND[2]) * ELEC_MONEY

    #是否该休眠
    def is_sleep(self):
        if self.sleep:
            return False
        if self.mode == 'hot':
            if self.currentTemp >= self.finalTemp:
                print 'time to sleep~'
                self.sleep = True
                return self.send_sleep()
        else:
            if self.currentTemp <= self.finalTemp:
                print 'time to sleep~'
                self.sleep = True
                return self.send_sleep()
        return False
    '''
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
    '''
