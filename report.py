# -*- coding:utf-8 -*-
import sqlite3
import time
import SocketServer
from AirClient import *
from AirService import *

class Database(object):
    def __init__(self):
        self.conn = sqlite3.connect('air.db')

    def init(self):
        #每个房间一个数据表
        create_table = [
            'DROP TABLE IF EXISTS `room306C`;',
            '''
        CREATE TABLE IF NOT EXISTS `room306C` (
          `id` INTEGER PRIMARY KEY NOT NULL,
          `operate` varchar(20) NOT NULL,
          `user` varchar(20) NOT NULL,
          `ip` varchar(20) NOT NULL,
          `date` timestamp NOT NULL,
          `timeLen` double NOT NULL ,
          `currentTemp` double DEFAULT NULL,
          `finalTemp` double DEFAULT NULL,
          `wind` int(5) DEFAULT NULL,
          `totalMoney` double DEFAULT NULL,
          `perMoney` double DEFAULT NULL
        );''',
             'DROP TABLE IF EXISTS `room306D`;',
            '''
        CREATE TABLE IF NOT EXISTS `room306D` (
          `id` INTEGER PRIMARY KEY NOT NULL,
          `operate` varchar(20) NOT NULL,
          `user` varchar(20) NOT NULL,
          `ip` varchar(20) NOT NULL,
          `date` timestamp NOT NULL,
          `timeLen` double NOT NULL ,
          `currentTemp` double DEFAULT NULL,
          `finalTemp` double DEFAULT NULL,
          `wind` int(5) DEFAULT NULL,
          `totalMoney` double DEFAULT NULL,
          `perMoney` double DEFAULT NULL
        );''',
             'DROP TABLE IF EXISTS `room307C`;',
            '''
        CREATE TABLE IF NOT EXISTS `room307C` (
          `id` INTEGER PRIMARY KEY NOT NULL,
          `operate` varchar(20) NOT NULL,
          `user` varchar(20) NOT NULL,
          `ip` varchar(20) NOT NULL,
          `date` timestamp NOT NULL,
          `timeLen` double NOT NULL ,
          `currentTemp` double DEFAULT NULL,
          `finalTemp` double DEFAULT NULL,
          `wind` int(5) DEFAULT NULL,
          `totalMoney` double DEFAULT NULL,
          `perMoney` double DEFAULT NULL
        );''',
        'DROP TABLE IF EXISTS `room307D`;',
            '''
        CREATE TABLE IF NOT EXISTS `room307D` (
          `id` INTEGER PRIMARY KEY NOT NULL,
          `operate` varchar(20) NOT NULL,
          `user` varchar(20) NOT NULL,
          `ip` varchar(20) NOT NULL,
          `date` timestamp NOT NULL,
          `timeLen` double NOT NULL ,
          `currentTemp` double DEFAULT NULL,
          `finalTemp` double DEFAULT NULL,
          `wind` int(5) DEFAULT NULL,
          `totalMoney` double DEFAULT NULL,
          `perMoney` double DEFAULT NULL
        );''',
        'DROP TABLE IF EXISTS `room308C`;',
            '''
        CREATE TABLE IF NOT EXISTS `room308C` (
          `id` INTEGER PRIMARY KEY NOT NULL,
          `operate` varchar(20) NOT NULL,
          `user` varchar(20) NOT NULL,
          `ip` varchar(20) NOT NULL,
          `date` timestamp NOT NULL,
          `timeLen` double NOT NULL ,
          `currentTemp` double DEFAULT NULL,
          `finalTemp` double DEFAULT NULL,
          `wind` int(5) DEFAULT NULL,
          `totalMoney` double DEFAULT NULL,
          `perMoney` double DEFAULT NULL
        );''',
        'DROP TABLE IF EXISTS `room308D`;',
            '''
        CREATE TABLE IF NOT EXISTS `room308D` (
          `id` INTEGER PRIMARY KEY NOT NULL,
          `operate` varchar(20) NOT NULL,
          `user` varchar(20) NOT NULL,
          `ip` varchar(20) NOT NULL,
          `date` timestamp NOT NULL,
          `timeLen` double NOT NULL ,
          `currentTemp` double DEFAULT NULL,
          `finalTemp` double DEFAULT NULL,
          `wind` int(5) DEFAULT NULL,
          `totalMoney` double DEFAULT NULL,
          `perMoney` double DEFAULT NULL
        );''',
        'DROP TABLE IF EXISTS `room309C`;',
            '''
        CREATE TABLE IF NOT EXISTS `room309C` (
          `id` INTEGER PRIMARY KEY NOT NULL,
          `operate` varchar(20) NOT NULL,
          `user` varchar(20) NOT NULL,
          `ip` varchar(20) NOT NULL,
          `date` timestamp NOT NULL,
          `timeLen` double NOT NULL ,
          `currentTemp` double DEFAULT NULL,
          `finalTemp` double DEFAULT NULL,
          `wind` int(5) DEFAULT NULL,
          `totalMoney` double DEFAULT NULL,
          `perMoney` double DEFAULT NULL
        );''',
        'DROP TABLE IF EXISTS `room309D`;',
            '''
        CREATE TABLE IF NOT EXISTS `room309D` (
          `id` INTEGER PRIMARY KEY NOT NULL,
          `operate` varchar(20) NOT NULL,
          `user` varchar(20) NOT NULL,
          `ip` varchar(20) NOT NULL,
          `date` timestamp NOT NULL,
          `timeLen` double NOT NULL ,
          `currentTemp` double DEFAULT NULL,
          `finalTemp` double DEFAULT NULL,
          `wind` int(5) DEFAULT NULL,
          `totalMoney` double DEFAULT NULL,
          `perMoney` double DEFAULT NULL
        );''',]
        for sqlQuery in create_table:
            cursor = self.conn.cursor()
            cursor.execute(sqlQuery)
            cursor.close()
            self.conn.commit()

    def test_unit(self):
        insert_table=[
            "INSERT INTO `room307C` (`id`, `operate`, `user`, `ip`, `date`,`timeLen`, `currentTemp`, `finalTemp`, `wind`, `totalMoney`, `perMoney`) VALUES (NULL, 'open', 'client', '127.0.0.1', '2018-06-11 00:00:00','25', '25.0', '28.0', '2', '15.2', '0.3');",
            "INSERT INTO `room307C` (`id`, `operate`, `user`, `ip`, `date`,`timeLen`, `currentTemp`, `finalTemp`, `wind`, `totalMoney`, `perMoney`) VALUES (NULL, 'serve', 'client', '127.0.0.1', '2018-06-11 00:00:00','30','25.0', '27.0', '3', '15.2', '0.3');",
            "INSERT INTO `room307C` (`id`, `operate`, `user`, `ip`, `date`,`timeLen`, `currentTemp`, `finalTemp`, `wind`, `totalMoney`, `perMoney`) VALUES (NULL, 'serve', 'client2', '127.0.0.1', '2018-06-11 00:00:00','15', '25.0', '28.0', '2', '15.2', '0.3');",
            "INSERT INTO `room307D` (`id`, `operate`, `user`, `ip`, `date`,`timeLen`, `currentTemp`, `finalTemp`, `wind`, `totalMoney`, `perMoney`) VALUES (NULL, 'close', 'client', '127.0.0.1', '2018-06-11 00:00:00','0', '25.0', '28.0', '2', '15.2', '0.3');"]

        for sqlQuery in insert_table:
            cursor = self.conn.cursor()
            cursor.execute(sqlQuery)
            cursor.close()
            self.conn.commit()

    #插入的函数还没调用
    def insert_operate(self,  objAir, user,op):
        if not isinstance(objAir, AirService):
            print 'not a airObj!'
            return
        insert=[
            "INSERT INTO `{tableName}` (`id`, `operate`, `user`, `ip`, `date`,`timeLen`, `currentTemp`, `finalTemp`, `wind`, `totalMoney`, `perMoney`) VALUES (NULL, '\"open\"', '{user}', '{ip}', datetime(),0 , '{currentTemp}', '{finalTemp}', '{wind}', 0, 0);".format(
            tableName=objAir.room, user=user, ip='127.0.0.1', #时间有问题！！！！！！
            currentTemp=objAir.currentTemp, finalTemp=objAir.finalTemp, wind=objAir.wind) ,
             "INSERT INTO `{tableName}` (`id`, `operate`, `user`, `ip`, `date`,`timeLen`, `currentTemp`, `finalTemp`, `wind`, `totalMoney`, `perMoney`) VALUES (NULL, '\"close\"', '{user}', '{ip}',  datetime(),'{timeLen}', '{currentTemp}', '{finalTemp}', '{wind}', '{totalMoney}', '{perMoney}');".format(
            tableName=objAir.room, user=user, ip='127.0.0.1', timeLen=objAir.lastTime,#时间有问题！！！！！！
            currentTemp=objAir.currentTemp, finalTemp=objAir.finalTemp, wind=objAir.wind, totalMoney=objAir.totalMoney,perMoney=objAir.perMoney) ,
            "INSERT INTO `{tableName}` (`id`, `operate`, `user`, `ip`, `date`,`timeLen`, `currentTemp`, `finalTemp`, `wind`, `totalMoney`, `perMoney`) VALUES (NULL, '\"serve\"', '{user}', '{ip}', datetime(),'{timeLen}', '{currentTemp}', '{finalTemp}', '{wind}', '{totalMoney}', '{perMoney}');".format(
            tableName=objAir.room, user=user, ip='127.0.0.1',timeLen=objAir.lastTime,#时间有问题！！！！！！
            currentTemp=objAir.currentTemp, finalTemp=objAir.finalTemp, wind=objAir.wind, totalMoney=objAir.totalMoney,perMoney=objAir.perMoney ) ,
        ]

        cursor = self.conn.cursor()
        if op=="open":
            cursor.execute(insert[0])
        elif op=="close":
            cursor.execute(insert[1])
        elif op=="serve":
            cursor.execute(insert[2])
        cursor.close()
        self.conn.commit()

    #报表 房间objRoom所在日期objDate的type类型报表 objDate有类型要求！！
    def report(self,t,objRoom,type):
        if type==0:
            pattern="%Y-%m-%d"
            objDate=time.strftime("%Y-%m-%d",t)
        elif type==1:
            pattern="%Y-%W"
            objDate=time.strftime("%Y-%W", t)
        elif type==2:
            pattern="%Y-%m"
            objDate=time.strftime("%Y-%m", t)
        select = [
            'Select  count(operate) from {tableName} where strftime("{pattern}",date)="{queryDate}" and operate=="open";'.format(tableName=objRoom,queryDate=objDate,pattern=pattern),
            #房间使用空调的次数（一次开关）

            '''
            Select  finalTemp,MAX(sumTime)from( select finalTemp,sum(timeLen)sumTime from {tableName} where strftime("{pattern}",date)="{queryDate}"
            group by finalTemp);
            '''.format(tableName=objRoom,queryDate=objDate,pattern=pattern),#最常用目标温度（该房间使用时间最长的目标温度）

            '''
            Select  wind,MAX(sumTime)from( select wind,sum(timeLen)sumTime from {tableName} where strftime("{pattern}",date)="{queryDate}"
            group by wind)
            ;'''.format(tableName=objRoom,queryDate=objDate,pattern=pattern),#最常用风速（时间最长的风速）

            'Select  count(*) from {tableName} where strftime("{pattern}",date)="{queryDate}" and operate=="serve" ;'.format(tableName=objRoom,queryDate=objDate,pattern=pattern),
            #达到目标温度次数---------没有考虑调度算法！！！！！！！

            'Select  count(operate) from {tableName} where strftime("{pattern}",date)="{queryDate}" and operate=="serve" ;'.format(tableName=objRoom,queryDate=objDate,pattern=pattern),
            #被调次数---------没有考虑调度算法！！！！！！！

            'Select  count(*) from {tableName} where strftime("{pattern}",date)="{queryDate}" group by user;'.format(tableName=objRoom,queryDate=objDate,pattern={pattern}),
            #详单数

            'Select sum(totalMoney) from {tableName} where strftime("{pattern}",date)="{queryDate}" and operate=="serve"  group by user;'.format(tableName=objRoom,queryDate=objDate,pattern=pattern)
            #总费用
            ]
        print(objRoom)
        list=[]
        for sqlQuery in select:
            cursor = self.conn.cursor()
            cursor.execute(sqlQuery)
            for row in cursor:
                list.append(row[0])
                #print(row[0]),
            cursor.close()
            self.conn.commit()
        print list
        return list

    #详单 用户user的所在房间objRoom的objDate那天的详单 以及总费用
    def detailed_bill(self,objRoom,user):
        select = [
            'Select  sum(totalMoney) from (Select  totalMoney from {tableName} where user="{user}");'.format(tableName=objRoom,user=user),
            #总钱数
            'Select  * from {tableName} where user="{user}";'.format(tableName=objRoom,user=user),
            #详单 是否要加日期？？？？一个用户多天都使用这个房间？？
            ]
        list=[]
        for sqlQuery in select:
            cursor = self.conn.cursor()
            cursor.execute(sqlQuery)
            for row in cursor:
                list.append(row)
                #print(row[0]),
            cursor.close()
            self.conn.commit()
        print list
        return list

    def getTotalMoney(self,objRoom,user):
        select = 'Select  sum(totalMoney) from (Select  totalMoney from {tableName} where user="{user}");'.format(tableName=objRoom,user=user)
            #总钱数
        cursor = self.conn.cursor()
        cursor.execute(select)
        for row in cursor:
            money = row

        cursor.close()
        self.conn.commit()
        print money[0]
        return money[0]


if __name__ == '__main__':
    read_setting()
    air = AirService()
    air.__init__("room307C",15,25,2)
    #print air
    database = Database()
    database.init()
    #执行动作时插入空调
    #database.insert_operate(air,"client1","open")
    #database.insert_operate(air,"zxh","open")
    #database.insert_operate(air,"zxh","close")
    #database.insert_operate(air,"zxh","serve")
    air.room="room307D"
    #database.insert_operate(air,"307D","open")
    #database.insert_operate(air,"307D","close")
    database.test_unit()
    #room在实例里修改 时间和类型在前端给出

    t = (2018, 6, 11, 17, 3, 38, 1, 48, 0)
    t = time.mktime(t)
    print"日报表"
    database.report(time.gmtime(t),"room307C",0)
    print"周报表"
    database.report(time.gmtime(t),"room307C",1)
    print"月报表"
    database.report(time.gmtime(t),"room307C",2)

    print "zxh","detailed_bill"
    database.detailed_bill("room307C","zxh")
