#-*- coding:utf-8 -*-
import socket
import time
import re, ConfigParser

COLD = 0.1

class Air(object):
    #初始化
    def __init__(self, room=503, currentTemp=15, finalTemp=25, wind=2):
        self.room = room
        self.currentTemp = currentTemp
        self.finalTemp = finalTemp
        self.wind = wind
        self.totalMoney = 0.0
        self.startTime = int(time.time())
        self.lastTime = int(time.time())
        self.sleep = False
        self.status_to_money()
        self.is_sleep()

    #改变状态
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

    #test：返回一个用于发送的字符串233
    def send_status(self):
        sendBuf = 'r_' + str(self.room) + '_' + str(self.currentTemp) + '_' + str(self.finalTemp) + '_' + str(self.wind)
        return sendBuf

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
            self.totalMoney += self.perMoney * self.perMoney
        else:
            #睡眠了
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
