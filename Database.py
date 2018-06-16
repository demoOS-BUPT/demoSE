# -*- coding:utf-8 -*-
import sqlite3
import time
import SocketServer
from AirClient import *
from AirService import *


class Database(object):
    def __init__(self):
        self.conn = sqlite3.connect('db/air'+str(time.time())+'.db')

    def init(self):
        create_table = [
            'DROP TABLE IF EXISTS `operate`;',
            '''
        CREATE TABLE IF NOT EXISTS `operate` (
          `id` INTEGER PRIMARY KEY NOT NULL,
          `operate` varchar(20) NOT NULL,
          `room` int(5) DEFAULT NULL,
          `user` varchar(20) NOT NULL,
          `ip` varchar(20) NOT NULL,
          `time` timestamp NOT NULL,
          `currentTemp` double DEFAULT NULL,
          `finalTemp` double DEFAULT NULL,
          `wind` int(5) DEFAULT NULL,
          `totalMoney` double DEFAULT NULL,
          `perMoney` double DEFAULT NULL
        );''', ]
        for sqlQuery in create_table:
            cursor = self.conn.cursor()
            cursor.execute(sqlQuery)
            cursor.close()
            self.conn.commit()

    def test_unit(self):
        sqlQuery = "INSERT INTO `operate` (`id`, `operate`, `room`, `user`, `ip`, `time`, `currentTemp`, `finalTemp`, `wind`, `totalMoney`, `perMoney`) VALUES (NULL, 'open', '501', 'client', '127.0.0.1', '2018-04-25 00:00:00', '25.0', '28.0', '2', '15.2', '0.3');"
        cursor = self.conn.cursor()
        cursor.execute(sqlQuery)
        cursor.close()
        self.conn.commit()

    def insert_operate(self, action, objAir, user):
        if not isinstance(objAir, AirService):
            print 'not a airObj!'
            return
        sqlQuery = "INSERT INTO `operate` (`id`, `operate`, `room`, `user`, `ip`, `time`, `currentTemp`, `finalTemp`, `wind`, `totalMoney`, `perMoney`) '\
        'VALUES (NULL, '{action}', '{room}', '{user}', '{ip}', '{time}', '{currentTemp}', '{finalTemp}', '{wind}', '{totalMoney}', '{perMoney}');".format(
            action=action, room=objAir.room, user=user, ip='127.0.0.1', time=int(time.time()),
            currentTemp=objAir.currentTemp, finalTemp=objAir.finalTemp, wind=objAir.wind, totalMoney=objAir.totalMoney,
            perMoney=objAir.totalMoney
        )
        cursor = self.conn.cursor()
        cursor.execute(sqlQuery)
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
    #air = AirService()
    #air.init()
    #print air
    database = Database()
    database.init()
    #执行动作时插入空调
    #database.insert_operate("first_start",AirService,"room523")
    database.test_unit()
    #room在实例里修改 时间和类型在前端给出

    t = '2018/04/25'
    timeArray = time.strptime(t, "%Y/%m/%d")
    timeStamp = int(time.mktime(timeArray))

    database.select_operate(timeStamp,0 , '501')
