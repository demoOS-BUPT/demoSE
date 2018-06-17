# -*- coding: UTF-8 -*-
# Ui Init
from PyQt4 import QtCore, QtGui

from report import *
import sys;
sys.path.append("./ui/")
from Dformui import *


class DformUI(QtGui.QDialog):
    def __init__(self,room,parent=None):
        super(DformUI,self).__init__(parent)
        self.Dform = Ui_MainWindow()
        self.Dform.setupUi(self)
        self.room = room
        self.showTab()
        self.Dform.gobackBtn.clicked.connect(self.bye)

    def bye(self):
        self.close()

    def showTab(self):

        list = database.detailed_bill(self.room)
        row = 0
        column = 0
        wind = [0,u'低风',u'中风',u'高风']

        air_closed_flag = 0

        self.Dform.listWidget.clear()
        last_wind = wind[0]
        last_temp = 0
        status = {}
        for items in list:
            #['id',u'操作','user',u'日期', u'时长', u'室温', u'目标温度', u'风速', u'单次服务用电',u'总耗电量',u'耗费/单位时间',u'单次服务金额',u'总金额'])
            status['op'] = items[1]
            status['date'] = items[3]
            status['timelen'] = items[4]
            status['roomtemp'] = items[5]
            status['targettemp'] = items[6]
            status['wind'] = wind[items[7]]
            status['singleelec'] = items[8]
            status['totalelec'] = items[9]
            status['permoney'] = items[10]
            status['singlemoney'] = items[11]
            status['totalmoney'] = items[12]

            if items[1] == "firstopen":
                showBuf = u'{date} 空调初次启动服务,室温{roomtemp}℃，目标温度{targettemp} ℃,风速{wind}。'
                air_closed_flag = 0
            elif items[1] == "serve":
                air_closed_flag = 0
                if last_wind != status['wind']:
                    showBuf = u'{date} 室温{roomtemp}℃，目标温度{targettemp} ℃,风速由'+last_wind+ u'改为{wind},总耗电量{totalelec}度,共耗费￥{totalmoney}。'
                elif last_temp != status['targettemp']:
                    showBuf = u'{date} 室温{roomtemp}℃，目标温度由'+str(last_temp)+u'改为{targettemp} ℃,风速{wind}，总耗电量{totalelec}度,共耗费￥{totalmoney}。'
                elif status['roomtemp'] >= status['targettemp']:
                    showBuf = u'{date} 室温{roomtemp}℃到达目标温度，开始休眠，停止计费，总耗电量{totalelec}度,共耗费￥{totalmoney}。'
                else:
                    showBuf = u'{date} 室温{roomtemp}℃，目标温度{targettemp} ℃,风速{wind}'
            elif items[1] == "open":
                air_closed_flag = 0
                showBuf = u'{date} 空调再次开机，室温{roomtemp}℃，目标温度{targettemp} ℃,风速{wind}，总耗电量{totalelec}度,共耗费￥{totalmoney}。'
            elif items[1] == "close":
                if air_closed_flag == 0: ######没关空调
                    showBuf = u'{date} 空调服务关闭，房间温度{roomtemp}℃,总耗电量{totalelec}度,共耗费￥{totalmoney}。'
                    air_closed_flag = 1
                else:
                    showBuf = u'{date} 退房了。'
                    air_closed_flag = 0
            else:
                print items[1]
            showBuf = showBuf.format(**status)
            self.Dform.listWidget.addItem(showBuf)
            last_wind = status['wind']
            last_temp = status['targettemp']


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dform = DformUI("307C")
    Dform.show()
    sys.exit(app.exec_())
