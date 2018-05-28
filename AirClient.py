#-*- coding:utf-8 -*-
import socket
import time
import re, ConfigParser

class AirClient(object):
    #初始化
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
        #self.is_sleep()

    def init(self, room=503, currentTemp=15, finalTemp=25, wind=2):
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
        #self.is_sleep()

    def send_start(self):
        #{:0>2d} 左边补0
        status = {'room':self.room}
        sendBuf = 'start_{room}_$'.format(**status)
        return sendBuf

    def send_first_open(self):
        sendBuf = 'r_{room}_{currentTemp}_{finalTemp}_{wind}_$'
        status = {'room':self.room,
                                    'currentTemp':self.currentTemp,
                                    'finalTemp':self.finalTemp,
                                    'wind':self.wind}
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
        return sendBuf

    def recv_start(self, operate):
        status = {}
        status['room'] = operate[1]
        if operate[2] == '1':
            status['mode'] = 'hot'
        else:
            status['mode'] = 'cold'
        status['tempFrom'] = operate[3].split('-')[0]
        status['tempTo'] = operate[3].split('-')[1]
        status['tempWidth'] = operate[4]

        self.change_status(status)

    def recv_a(self,operate):
        status = {}
        status['room'] = operate[1]
        status['currentTemp'] = operate[2]
        status['totalMoney'] = operate[3]
        status['time'] = operate[4]
        status['finalTemp'] = operate[5]
        status['wind'] = operate[6]
        status['tempChange'] = operate[7]
        status['preMoney'] = operate[8]
        status['totalElec'] = operate[9]

        self.change_status(status)

    def recv_close(self, operate):
        if operate[2] == '1':
            print('退房了!')
            return False
        self.open = True
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
            self.currentTemp = kwargs['currentTemp']
        if 'finalTemp' in kwargs:
            self.finalTemp = kwargs['finalTemp']
        if 'wind' in kwargs:
            self.wind = kwargs['wind']

    #test：展示状态
    def show_status(self):
        print 'room:', self.room, 'currentTemp:', self.currentTemp, 'finalTemp:', self.finalTemp, 'wind:', self.wind
        #print dir(self)
