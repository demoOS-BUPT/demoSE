#-*- coding:utf-8 -*-
import socket
import time
import re, ConfigParser

global localTempChange,localTempRange,localInitTemp
localTempChange=0.8
localTempRange=3.0
localInitTemp=26



class AirClient(object):

    def __init__(self, room=503, currentTemp=15, finalTemp=25, wind=2):
        self.room = room
        self.mode = 'hot'
        self.currentTemp = currentTemp
        self.finalTemp = finalTemp
        self.wind = wind
        self.totalMoney = 0.0
        self.startTime = int(time.time())
        self.lastTime = int(time.time())
        self.sleep = False
        self.open = True
        self.tempWidth = 2
        #self.is_sleep()

    def reset(self):
        self.mode = MODE
        self.currentTemp = DEFAULT_TEMP - 3
        self.finalTemp = DEFAULT_TEMP
        self.wind = DEFAULT_WIND
        self.totalMoney = 0.0
        self.perMoney = 1.2
        self.startTime = int(time.time())
        self.lastTime = int(time.time())
        self.sleep = False
        self.open = False
        self.totalElec = 0
        self.status_syn()

    def send_start(self):
        #{:0>2d} 左边补0
        status = {'room':self.room}
        sendBuf = 'start_{room}_$'.format(**status)
        return sendBuf

    def send_first_open(self):
        sendBuf = 'r_{room}_{currentTemp}_{finalTemp}_{wind}_$'
        status = {'room':self.room,
                                    'currentTemp':self.currentTemp,
                                    'finalTemp':'#',
                                    'wind':'#'}
        sendBuf = sendBuf.format(**status)
        return sendBuf

    def send_open(self):
        sendBuf = 'r_{room}_{currentTemp}_{finalTemp}_{wind}_$'
        status = {'room':self.room,
                                    'currentTemp':self.currentTemp,
                                    'finalTemp':self.finalTemp,
                                    'wind':self.wind}
        sendBuf = sendBuf.format(**status)
        return sendBuf

    def send_change(self):
        sendBuf = 'c_{room}_{currentTemp}_{finalTemp}_{wind}_$'
        status = {'room':self.room,
                                    'currentTemp':self.currentTemp,
                                    'finalTemp':self.finalTemp,
                                    'wind':self.wind}
        sendBuf = sendBuf.format(**status)
        return sendBuf

    def send_close(self):
        sendBuf = 'close_{room}_$'
        status = {'room':self.room}
        sendBuf = sendBuf.format(**status)
        self.open = False
        return sendBuf

    def recv_start(self, operate):
        status = {}
        #status['room'] = operate[1]
        status['mode'] = operate[2]
        status['tempFrom'] = operate[3].split('-')[0]
        status['tempTo'] = operate[3].split('-')[1]
        status['tempWidth'] = operate[4]

        self.change_status(status)

    def recv_a(self,operate):
        status = {}
        #status['room'] = operate[1]
        status['currentTemp'] = operate[2]
        status['totalMoney'] = operate[3]
        status['time'] = self.time_to_stamp(operate[4])
        status['finalTemp'] = operate[5]
        status['wind'] = operate[6]
        status['tempChange'] = operate[7]
        status['preMoney'] = operate[8]
        status['totalElec'] = operate[9]

        self.change_status(status)

    def recv_close(self, operate):
        if operate[2] == '1':
            print('退房了!')
            self.reset()
            return False
        self.open = False
        return True

    def recv_sleep(self, operate):
        self.sleep = True

    def recv_wait(self, operate):
        print 'i recv a wait message!'

    #改变状态,这里把参数补齐
    def change_status(self, kwargs):
        if 'room' in kwargs:
            self.room = kwargs['room']
        if 'currentTemp' in kwargs:
            self.currentTemp = float(kwargs['currentTemp'])
        if 'finalTemp' in kwargs:
            self.finalTemp = float(kwargs['finalTemp'])
        if 'wind' in kwargs:
            self.wind = int(kwargs['wind'])
        if 'totalMoney' in kwargs:
            self.totalMoney = float(kwargs['totalMoney'])
        if 'time'in kwargs:
            pass
            #self.lastTime = kwargs['time']
        if 'tempChange' in kwargs:
            self.tempChange = int(kwargs['tempChange'])
        if 'perMoney' in kwargs:
            self.perMoney = float(kwargs['perMoney'])
        if 'totalElec' in kwargs:
            self.totalElec = float(kwargs['totalElec'])
        if 'mode'in kwargs:
            if kwargs['mode'] == 1 or kwargs['mode'] == '1':
                self.mode = 'hot'
            else:
                self.mode = 'cold'
        if 'tempFrom' in kwargs:
            self.tempFrom = int(kwargs['tempFrom'])
        if 'tempTo' in kwargs:
            self.tempTo = int(kwargs['tempTo'])
        if 'tempWidth' in kwargs:
            self.tempWidth = int(kwargs['tempWidth'])



    #回温计算
    def work(self):
        #localTempChange 本地每秒温度变化速率 localTempRange 本地温度变化范围 #本地初始温度
        nowTime = int(time.time())

        #模拟运行
        if nowTime <= int( self.lastTime + 3 ):
            return False

        if not self.open:
            print '[closing]', self.room
            return False

        if self.sleep:
            print '[sleeping]'
            if self.mode == 'hot':
                self.currentTemp -= localTempChange
                if self.currentTemp <= self.finalTemp - self.tempWidth:
                    self.sleep = False
                    return self.send_open()
            else:
                self.currentTemp += localTempChange
                if self.currentTemp >= self.finalTemp + self.tempWidth:
                    self.sleep = False
                    return self.send_open()
        else:
            return False

        self.lastTime = nowTime

    def stamp_to_time(self, num):
        timeArray = time.localtime(num)
        return time.strftime("%Y/%m/%d/%H/%M/%S", timeArray)

    def time_to_stamp(self, tmpStr):
        timeArray = time.strptime(tmpStr, "%Y/%m/%d/%H/%M/%S")
        return int(time.mktime(timeArray))

    #test：展示状态
    def show_status(self):
        print 'room:', self.room, 'currentTemp:', self.currentTemp, 'finalTemp:', self.finalTemp,'mode',self.mode , 'wind:', self.wind
        #print dir(self)
