# -*- coding:utf-8 -*-
import sqlite3
import time
import SocketServer
from AirClient import *
from AirService import *

class Database(object):
    def __init__(self):
        self.conn = sqlite3.connect('air.db',check_same_thread=False)

    def init(self):
        #每个房间一个数据表
        create_table = [
            'DROP TABLE IF EXISTS `room306C`;',
            '''
        CREATE TABLE IF NOT EXISTS `room306C` (
          `id` INTEGER PRIMARY KEY NOT NULL,
          `operate` varchar(20) NOT NULL,
          `user` int(5) DEFAULT NULL,
          `date` timestamp NOT NULL,
          `timeLen` double NOT NULL ,
          `currentTemp` double DEFAULT NULL,
          `finalTemp` double DEFAULT NULL,
          `wind` int(5) DEFAULT NULL,
          `singleElec`double DEFAULT NULL,
          `totalElec`double DEFAULT NULL,
          `perMoney` double DEFAULT NULL,
          `singleMoney`double DEFAULT NULL,
          `totalMoney` double DEFAULT NULL
        );''',
             'DROP TABLE IF EXISTS `room306D`;',
            '''
        CREATE TABLE IF NOT EXISTS `room306D` (
          `id` INTEGER PRIMARY KEY NOT NULL,
          `operate` varchar(20) NOT NULL,
          `user` int(5) DEFAULT NULL,
          `date` timestamp NOT NULL,
          `timeLen` double NOT NULL ,
          `currentTemp` double DEFAULT NULL,
          `finalTemp` double DEFAULT NULL,
          `wind` int(5) DEFAULT NULL,
          `singleElec`double DEFAULT NULL,
          `totalElec`double DEFAULT NULL,
          `perMoney` double DEFAULT NULL,
          `singleMoney`double DEFAULT NULL,
          `totalMoney` double DEFAULT NULL
        );''',
             'DROP TABLE IF EXISTS `room307C`;',
            '''
        CREATE TABLE IF NOT EXISTS `room307C` (
          `id` INTEGER PRIMARY KEY NOT NULL,
          `operate` varchar(20) NOT NULL,
          `user` int(5) DEFAULT NULL,
          `date` timestamp NOT NULL,
          `timeLen` double NOT NULL ,
          `currentTemp` double DEFAULT NULL,
          `finalTemp` double DEFAULT NULL,
          `wind` int(5) DEFAULT NULL,
          `singleElec`double DEFAULT NULL,
          `totalElec`double DEFAULT NULL,
          `perMoney` double DEFAULT NULL,
          `singleMoney`double DEFAULT NULL,
          `totalMoney` double DEFAULT NULL
        );''',
        'DROP TABLE IF EXISTS `room307D`;',
            '''
        CREATE TABLE IF NOT EXISTS `room307D` (
          `id` INTEGER PRIMARY KEY NOT NULL,
          `operate` varchar(20) NOT NULL,
          `user` int(5) DEFAULT NULL,
          `date` timestamp NOT NULL,
          `timeLen` double NOT NULL ,
          `currentTemp` double DEFAULT NULL,
          `finalTemp` double DEFAULT NULL,
          `wind` int(5) DEFAULT NULL,
          `singleElec`double DEFAULT NULL,
          `totalElec`double DEFAULT NULL,
          `perMoney` double DEFAULT NULL,
          `singleMoney`double DEFAULT NULL,
          `totalMoney` double DEFAULT NULL
        );''',
        'DROP TABLE IF EXISTS `room308C`;',
            '''
        CREATE TABLE IF NOT EXISTS `room308C` (
          `id` INTEGER PRIMARY KEY NOT NULL,
          `operate` varchar(20) NOT NULL,
          `user` int(5) DEFAULT NULL,
          `date` timestamp NOT NULL,
          `timeLen` double NOT NULL ,
          `currentTemp` double DEFAULT NULL,
          `finalTemp` double DEFAULT NULL,
          `wind` int(5) DEFAULT NULL,
          `singleElec`double DEFAULT NULL,
          `totalElec`double DEFAULT NULL,
          `perMoney` double DEFAULT NULL,
          `singleMoney`double DEFAULT NULL,
          `totalMoney` double DEFAULT NULL
        );''',
        'DROP TABLE IF EXISTS `room308D`;',
            '''
        CREATE TABLE IF NOT EXISTS `room308D` (
          `id` INTEGER PRIMARY KEY NOT NULL,
          `operate` varchar(20) NOT NULL,
          `user` int(5) DEFAULT NULL,
          `date` timestamp NOT NULL,
          `timeLen` double NOT NULL ,
          `currentTemp` double DEFAULT NULL,
          `finalTemp` double DEFAULT NULL,
          `wind` int(5) DEFAULT NULL,
          `singleElec`double DEFAULT NULL,
          `totalElec`double DEFAULT NULL,
          `perMoney` double DEFAULT NULL,
          `singleMoney`double DEFAULT NULL,
          `totalMoney` double DEFAULT NULL
        );''',
        'DROP TABLE IF EXISTS `room309C`;',
            '''
        CREATE TABLE IF NOT EXISTS `room309C` (
          `id` INTEGER PRIMARY KEY NOT NULL,
          `operate` varchar(20) NOT NULL,
          `user` int(5) DEFAULT NULL,
          `date` timestamp NOT NULL,
          `timeLen` double NOT NULL ,
          `currentTemp` double DEFAULT NULL,
          `finalTemp` double DEFAULT NULL,
          `wind` int(5) DEFAULT NULL,
          `singleElec`double DEFAULT NULL,
          `totalElec`double DEFAULT NULL,
          `perMoney` double DEFAULT NULL,
          `singleMoney`double DEFAULT NULL,
          `totalMoney` double DEFAULT NULL
        );''',
        'DROP TABLE IF EXISTS `room309D`;',
            '''
        CREATE TABLE IF NOT EXISTS `room309D` (
          `id` INTEGER PRIMARY KEY NOT NULL,
          `operate` varchar(20) NOT NULL,
          `user` int(5) DEFAULT NULL,
          `date` timestamp NOT NULL,
          `timeLen` double NOT NULL ,
          `currentTemp` double DEFAULT NULL,
          `finalTemp` double DEFAULT NULL,
          `wind` int(5) DEFAULT NULL,
          `singleElec`double DEFAULT NULL,
          `totalElec`double DEFAULT NULL,
          `perMoney` double DEFAULT NULL,
          `singleMoney`double DEFAULT NULL,
          `totalMoney` double DEFAULT NULL
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

    def getUser(self,objRoom):
        #objRoom="room"+objRoom
        select = [
            'Select  count(*) from {tableName} where operate=="firstopen" ;'.format(tableName=objRoom),
            ]
        user=0
        for sqlQuery in select:
            cursor = self.conn.cursor()
            cursor.execute(sqlQuery)
            for row in cursor:
                user=row[0]
            cursor.close()
            self.conn.commit()
        return user

    def getId(self,objRoom):
        #objRoom="room"+objRoom
        select = [
            'Select  count(*) from {tableName} ;'.format(tableName=objRoom),
            #房间使用空调的次数（一次开关）
        ]
        id=0
        for sqlQuery in select:
            cursor = self.conn.cursor()
            cursor.execute(sqlQuery)
            for row in cursor:
                id=row[0]
            cursor.close()
            self.conn.commit()
        return id+1

    def getLastTotalElec(self,user,objRoom):
        #objRoom="room"+objRoom
        select = [
            'Select  max(totalElec) from {tableName} where user == "{user}" ;'.format(tableName=objRoom,user=user),
            #房间使用空调的次数（一次开关）
        ]
        elec=0
        for sqlQuery in select:
            cursor = self.conn.cursor()
            cursor.execute(sqlQuery)
            for row in cursor:
                if row[0]==None:
                    elec=0
                else:
                    elec=row[0]
                #print elec
            cursor.close()
            self.conn.commit()
        float(elec)
        return elec

    def getLastTotalMoney(self,user,objRoom):
        #objRoom="room"+objRoom
        select = [
            'Select  max(totalMoney) from {tableName} where user=="{user}";'.format(tableName=objRoom,user=user),
            #房间使用空调的次数（一次开关）
        ]
        money=0
        for sqlQuery in select:
            cursor = self.conn.cursor()
            cursor.execute(sqlQuery)
            for row in cursor:
                if row[0]==None:
                    money=0
                else:
                    money=row[0]
            cursor.close()
            self.conn.commit()
        float (money)
        return money

    #插入的函数还没调用
    def insert_operate(self,objAir,op,timeLen):
        objRoom="room"+objAir.room
        '''
        if not isinstance(objAir,AirService):
            print 'not a airObj!'
            return
        '''
        user=database.getUser(objRoom)
        id=database.getId(objRoom)
        singleElec=objAir.totalElec-database.getLastTotalElec(user,objRoom)
        singleMoney=objAir.totalMoney-database.getLastTotalMoney(user,objRoom)
        insert=[
            "INSERT INTO `{tableName}` (`id`, `operate`, `user`, `date`,`timeLen`, `currentTemp`, `finalTemp`, `wind`, `singleElec`,`totalElec`,`perMoney`,`singleMoney`, `totalMoney`) VALUES ('{id}', 'firstopen', '{user}', '{date} ',0 , '{currentTemp}', '{finalTemp}', '{wind}', 0, 0,'{perMoney}',0,0);".format(
            tableName=objRoom,id=id, user=user+1,date= time.strftime("%Y-%m-%d", time.localtime(objAir.lastTime))  ,currentTemp=objAir.currentTemp, finalTemp=objAir.finalTemp, wind=objAir.wind,perMoney=objAir.perMoney) ,
            "INSERT INTO `{tableName}` (`id`, `operate`, `user`, `date`,`timeLen`, `currentTemp`, `finalTemp`, `wind`, `singleElec`,`totalElec`,`perMoney`,`singleMoney`, `totalMoney`) VALUES ('{id}', 'open', '{user}', '{date} ',0, '{currentTemp}', '{finalTemp}', '{wind}', 0, '{totalElec}', '{perMoney}', 0, '{totalMoney}');".format(
            tableName=objRoom,id=id, user=user,date= time.strftime("%Y-%m-%d", time.localtime(objAir.lastTime))  ,currentTemp=objAir.currentTemp, finalTemp=objAir.finalTemp, wind=objAir.wind,
            totalElec=objAir.totalElec,perMoney=objAir.perMoney,totalMoney=objAir.totalMoney) ,
             "INSERT INTO `{tableName}` (`id`, `operate`, `user`, `date`,`timeLen`, `currentTemp`, `finalTemp`, `wind`, `singleElec`,`totalElec`,`perMoney`,`singleMoney`, `totalMoney`) VALUES ('{id}', 'close', '{user}', '{date} ',0, '{currentTemp}', '{finalTemp}', '{wind}', 0, '{totalElec}', '{perMoney}',0, '{totalMoney}');".format(
            tableName=objRoom,id=id, user=user,date= time.strftime("%Y-%m-%d", time.localtime(objAir.lastTime))  ,currentTemp=objAir.currentTemp, finalTemp=objAir.finalTemp, wind=objAir.wind,
            totalElec=objAir.totalElec,perMoney=objAir.perMoney,totalMoney=objAir.totalMoney) ,
            "INSERT INTO `{tableName}` (`id`, `operate`, `user`, `date`,`timeLen`, `currentTemp`, `finalTemp`, `wind`, `singleElec`,`totalElec`,`perMoney`,`singleMoney`, `totalMoney`) VALUES ('{id}', 'serve', '{user}', '{date} ','{timeLen}', '{currentTemp}', '{finalTemp}', '{wind}', '{singleElec}', '{totalElec}', '{perMoney}', '{singleMoney}', '{totalMoney}');".format(
            tableName=objRoom,id=id, user=user,date= time.strftime("%Y-%m-%d", time.localtime(objAir.lastTime)) ,timeLen=timeLen,currentTemp=objAir.currentTemp, finalTemp=objAir.finalTemp, wind=objAir.wind,
            singleElec=singleElec,totalElec=objAir.totalElec,perMoney=objAir.perMoney,singleMoney=singleMoney,totalMoney=objAir.totalMoney ) ,
        ]

        cursor = self.conn.cursor()
        if op=="firstopen":
            cursor.execute(insert[0])
        elif op=="open":
            cursor.execute(insert[1])
        elif op=="close":
            cursor.execute(insert[2])
        elif op=="serve":
            cursor.execute(insert[3])
        cursor.close()
        self.conn.commit()

    #报表 房间objRoom所在日期objDate的type类型报表 objDate有类型要求！！
    def report(self,t,objRoom,type):
        objRoom="room"+objRoom
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
            'Select  count(operate) from {tableName} where strftime("{pattern}",date)="{queryDate}" and (operate=="open" or operate=="firstopen");'.format(tableName=objRoom,queryDate=objDate,pattern=pattern),
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

            'Select count(User) from ( select count(*)User from {tableName} where strftime("{pattern}",date)="{queryDate}" group by user);'.format(tableName=objRoom,queryDate=objDate,pattern=pattern),
            #详单数

            'Select sum(totalMoney) from {tableName} where strftime("{pattern}",date)="{queryDate}" and operate=="close"  group by user;'.format(tableName=objRoom,queryDate=objDate,pattern=pattern)
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
        #print len(list)
        return list

    #详单 用户user的所在房间objRoom的objDate那天的详单 以及总费用
    def detailed_bill(self,objRoom):
        objRoom="room"+objRoom
        user=database.getUser(objRoom)
        select = [
            'Select * from {tableName} where user="{user}";'.format(tableName=objRoom,user=user),
            #详单
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

    def getTotalMoney(self,objRoom):
        objRoom="room"+objRoom
        user=database.getUser(objRoom)
        print "user",user
        select = 'Select max(totalMoney)money from {tableName} where user="{user}" and operate=="close";'.format(tableName=objRoom,user=user)
            #总钱数
        cursor = self.conn.cursor()
        cursor.execute(select)
        for row in cursor:
            money = row
        cursor.close()
        self.conn.commit()
        print money[0]
        return money[0]

database = Database()
database.init()

if __name__ == '__main__':
    read_setting()
    air = AirService()
    air.__init__("307C",15,25,2)
    #print air
    database = Database()
    database.init()
    air.totalElec=30
    air.totalMoney=110
    #执行动作时插入空调
    database.insert_operate(air,"firstopen",0)
    database.insert_operate(air,"serve",30)
    database.insert_operate(air,"serve",20)
    database.insert_operate(air,"close",0)
    air.wind=1.5
    air.perMoney=3
    database.insert_operate(air,"open",0)
    database.insert_operate(air,"serve",20)
    air.totalMoney=300
    database.insert_operate(air,"close",0)
    air.room="307D"
    database.insert_operate(air,"open",0)
    database.insert_operate(air,"close",0)
    #database.test_unit()
    #room在实例里修改 时间和类型在前端给出

    t = (2018, 6, 15, 17, 3, 38, 1, 48, 0)
    t = time.mktime(t)
    print"日报表"
    database.report(time.gmtime(t),"307C",0)
    print"周报表"
    database.report(time.gmtime(t),"307C",1)
    print"月报表"
    database.report(time.gmtime(t),"307C",2)

    print "detailed_bill"
    database.detailed_bill("307C")
    database.getTotalMoney("307C")
