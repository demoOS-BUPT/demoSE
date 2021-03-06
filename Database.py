#-*- coding:utf-8 -*-
import sqlite3

class Database(object):

    def __init__(self):
        self.conn = sqlite3.connect('air.db')
    
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
        );''',]
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
    
     
    def insert_operate(self, action, objAirm, user):
        if !isinstance(objAir, Air):
            print 'not a airObj!'
            return
        sqlQuery = "INSERT INTO `operate` (`id`, `operate`, `room`, `user`, `ip`, `time`, `currentTemp`, `finalTemp`, `wind`, `totalMoney`, `perMoney`) '\
        'VALUES (NULL, '{action}', '{room}', '{user}', '{ip}', '{time}', '{currentTemp}', '{finalTemp}', '{wind}', '{totalMoney}', '{perMoney}');".format(
          action=action, room=objAir.room, user=user, ip='127.0.0.1', time=int(time.time()), currentTemp=objAir.currentTemp, finalTemp=objAir.finalTemp, wind=objAir.wind, totalMoney=objAir.totalMoney, perMoney=objAir.totalMoney
          )
        cursor = self.conn.cursor()
        cursor.execute(sqlQuery)
        cursor.close()
        self.conn.commit()
        
    def select_operate(self, room):
        pass
        
if __name__ == '__main__':
    database = Database()
    database.init()
    database.test_unit()