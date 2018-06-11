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
        );''',]
        for sqlQuery in create_table:
            cursor = self.conn.cursor()
            cursor.execute(sqlQuery)
            cursor.close()
            self.conn.commit()

    def test_unit(self):
        insert_table=[
            "INSERT INTO `room307C` (`id`, `operate`, `user`, `ip`, `date`,`timeLen`, `currentTemp`, `finalTemp`, `wind`, `totalMoney`, `perMoney`) VALUES (NULL, 'open', 'client', '127.0.0.1', '2018-04-25 00:00:00','0', '25.0', '28.0', '2', '15.2', '0.3');",
            "INSERT INTO `room307C` (`id`, `operate`, `user`, `ip`, `date`,`timeLen`, `currentTemp`, `finalTemp`, `wind`, `totalMoney`, `perMoney`) VALUES (NULL, 'serve', 'client', '127.0.0.1', '2018-04-25 00:00:00','30','25.0', '28.0', '2', '15.2', '0.3');",
            "INSERT INTO `room307C` (`id`, `operate`, `user`, `ip`, `date`,`timeLen`, `currentTemp`, `finalTemp`, `wind`, `totalMoney`, `perMoney`) VALUES (NULL, 'serve', 'client', '127.0.0.1', '2018-04-25 00:00:00','15', '25.0', '28.0', '2', '15.2', '0.3');",
            "INSERT INTO `room307D` (`id`, `operate`, `user`, `ip`, `date`,`timeLen`, `currentTemp`, `finalTemp`, `wind`, `totalMoney`, `perMoney`) VALUES (NULL, 'close', 'client', '127.0.0.1', '2018-04-25 00:00:00','0', '25.0', '28.0', '2', '15.2', '0.3');"]

        for sqlQuery in insert_table:
            cursor = self.conn.cursor()
            cursor.execute(sqlQuery)
            cursor.close()
            self.conn.commit()


    def insert_operate(self,  objAir, user,op):
        if not isinstance(objAir, AirService):
            print 'not a airObj!'
            return
        insert=[
            "INSERT INTO `{tableName}` (`id`, `operate`, `user`, `ip`, `date`,`timeLen`, `currentTemp`, `finalTemp`, `wind`, `totalMoney`, `perMoney`) VALUES (NULL, '\"open\"', '{user}', '{ip}', '{date}',0 , '{currentTemp}', '{finalTemp}', '{wind}', 0, 0);".format(
            tableName=objAir.room, user=user, ip='127.0.0.1', date=int(time.time()),#时间有问题！！！！！！
            currentTemp=objAir.currentTemp, finalTemp=objAir.finalTemp, wind=objAir.wind) ,
             "INSERT INTO `{tableName}` (`id`, `operate`, `user`, `ip`, `date`,`timeLen`, `currentTemp`, `finalTemp`, `wind`, `totalMoney`, `perMoney`) VALUES (NULL, '\"close\"', '{user}', '{ip}', '{date}','{timeLen}', '{currentTemp}', '{finalTemp}', '{wind}', '{totalMoney}', '{perMoney}');".format(
            tableName=objAir.room, user=user, ip='127.0.0.1', date=int(time.time()),timeLen=objAir.lastTime,#时间有问题！！！！！！
            currentTemp=objAir.currentTemp, finalTemp=objAir.finalTemp, wind=objAir.wind, totalMoney=objAir.totalMoney,perMoney=objAir.perMoney) ,
            "INSERT INTO `{tableName}` (`id`, `operate`, `user`, `ip`, `date`,`timeLen`, `currentTemp`, `finalTemp`, `wind`, `totalMoney`, `perMoney`) VALUES (NULL, '\"serve\"', '{user}', '{ip}', '{date}','{timeLen}', '{currentTemp}', '{finalTemp}', '{wind}', '{totalMoney}', '{perMoney}');".format(
            tableName=objAir.room, user=user, ip='127.0.0.1', date=int(time.time()),timeLen=objAir.lastTime,#时间有问题！！！！！！
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


    def report(self,objDate,objRoom):
        select = [
            'Select  count(operate) from {tableName} where date="{queryDate}" and operate=="open";'.format(tableName=objRoom,queryDate=objDate),
            #房间使用空调的次数（一次开关）

            '''
            Select  finalTemp  from {tableName} where date="{queryDate}" and sum(time)>= (
            Select  sum(time)  from {tableName} where date="{queryDate}" and group by finalTemp)group by finalTemp;
            '''.format(tableName=objRoom,queryDate=objDate),#最常用目标温度（该房间使用时间最长的目标温度）

            '''
          Select  wind  from {tableName} where date="{queryDate}" and sum(time)>= (
          Select  sum(time)  from {tableName} where date="{queryDate}" and group by wind)group by wind
          ;'''.format(tableName=objRoom,queryDate=objDate),#最常用风速（时间最长的风速）

            'Select  count(*) from {tableName} where date="{queryDate}" and operate=="serve" ;'.format(tableName=objRoom,queryDate=objDate),
            #达到目标温度次数---------没有考虑调度算法！！！！！！！

            'Select  count(operate) from {tableName} where date="{queryDate}" and operate=="serve" ;'.format(tableName=objRoom,queryDate=objDate),
            #被调次数---------没有考虑调度算法！！！！！！！

            'Select  count(*) from {tableName} where date="{queryDate}" group by user;'.format(tableName=objRoom,queryDate=objDate),
            #详单数

            'Select sum(totalMoney) from {tableName} where date="{queryDate}" and operate=="serve"  group user;'.format(tableName=objRoom,queryDate=objDate)
            #总费用
            ]
        print(objRoom),
        for sqlQuery in select:
            cursor = self.conn.cursor()
            cursor.execute(sqlQuery)
            for row in cursor:
                print(row[0]),
            print ("\n")
            cursor.close()
            self.conn.commit()





    def select_operate(self, date,type, objroom):
        #print type(objAir)
        '''
        if not isinstance(objAir, AirService):
            print 'not a airObj!'
            return
        '''
        date = time.gmtime(date)
        if type == 0:
            # 日报表
            #time.strftime("%Y-%m-%d",date)
            #sqlQuery = "SELECT * FROM `operate` "
            if objroom.strip()=='':
                sqlQuery = "SELECT * FROM `operate` WHERE strftime('\"%Y-%m-%d\"',time)=='\"{date}\"' ORDER BY TIME".format(
                    date= time.strftime("%Y-%m-%d", date)
                )
            else:
                sqlQuery = "SELECT * FROM `operate` WHERE room=='\"{objroom}\"' AND strftime('\"%Y-%m-%d\"',time)=='\"{date}\"' ORDER BY TIME".format(
                    date= time.strftime("%Y-%m-%d", date), objroom=objroom
                )
            #sqlQuery = "SELECT * FROM `operate` WHERE '\"2018-04-25\"'=='\"{date}\"' ORDER BY TIME".format(
             #   date=date
            #)
            print (sqlQuery)
            print("{date}日报表\n".format(date=date))
        elif type == 1:
            # 周报表
            if objroom.strip()=='':
                sqlQuery = "SELECT * FROM `operate` WHERE strftime('%Y-%W','TIME')=={date} ORDER BY TIME".format(
                    date=time.strftime("%Y-%W",date)
                )
            else:
                sqlQuery = "SELECT * FROM `operate` WHERE  room=='\"{objroom}\"' AND strftime('%Y-%W','TIME')=={date} ORDER BY TIME".format(
                    date=time.strftime("%Y-%W",date),objroom=objroom
                )
            print("{date}周报表\n".format(date=date))
        elif type == 2:
            # 月报表
            if objroom.strip()=='':
                sqlQuery = "SELECT * FROM `operate` WHERE strftime('%Y-%m','TIME')=={date} ORDER BY TIME".format(
                    date=time.strftime("%Y-%m",date)
                )
            else:
                sqlQuery = "SELECT * FROM `operate` WHERE room=='\"{objroom}\"' AND strftime('%Y-%m','TIME')=={date} ORDER BY TIME".format(
                    date=time.strftime("%Y-%m",date),objroom=objroom
                )
            print("{date}月报表\n".format(date=date))

        cursor = self.conn.cursor()
        cursor.execute(sqlQuery)

        print('%5s' % 'Room'),
        print('%10s' % 'Operate'),
        print('%8s' % 'User'),
        print('%15s' % 'IP'),
        print('%15s' % 'Time'),
        print('%15s' % 'InitTemperature'),
        print('%15s' % 'FinalTemperature'),
        print('%5s' % 'Wind'),
        print('%15s' % 'PerMoney'),
        print('%15s' % 'TotalMoney')

        for row in cursor:
            # print "id_operate_room_user_ip_time_currentTemp_finalTemp_wind_totalMoney_perMonet"
            print('%5s' % row[2]),
            print('%10s' % row[1]),
            print('%8s' % row[3]),
            print('%15s' % row[4]),
            print('%15s' % row[5]),
            print('%15s' % row[6]),
            print('%15s' % row[7]),
            print('%5s' % row[8]),
            print('%15s' % row[10]),
            print('%15s' % row[9])

        cursor.close()
        self.conn.commit()



if __name__ == '__main__':
    air = AirService()
    air.init()
    print air
    database = Database()
    database.init()
    #执行动作时插入空调
    database.insert_operate(AirService,"room523","open")
    #database.test_unit()
    #room在实例里修改 时间和类型在前端给出

    t = '2018-06-11'
    timeArray = time.strptime(t, "%Y-%m-%d")
    timeStamp = int(time.mktime(timeArray))

    database.report("2018-06-11","room307C")
    #database.select_operate(timeStamp,0 , '501')
