# -*- coding:utf-8 -*-
import math, time

class Algo(object):

    def __init__(self):
        self.roomPriority = {'307C':2, '306C':2,'306D':2,'307D':2}

        self.serverList = []
        self.waitList = []
        self.roomStartTime = {}
        self.time = int(time.time())
        self.queueLength = 5
        self.queueTime = 6

    def req_server(self, roomid, priority):
        self.roomPriority[roomid] = priority
        #print '[queueueueueue]', roomid, '[request]'
        if time.time()-self.time >= self.queueTime:
            self.time = time.time()
            self.change_server()
        
        if roomid in self.serverList:
            print roomid, 'serving'
            return
        elif roomid in self.waitList:
            print roomid, 'waiting'
            return

        # self.serverList append
        if len(self.serverList) < self.queueLength:
            self.serverList.append(roomid)
            self.roomStartTime[roomid] = time.time()
            return
        else:
            # get min priority
            minPriority = 999
            minRoom = []
            for room in self.serverList:
                if self.roomPriority[room] < minPriority:
                    minPriority = self.roomPriority[room]
                    minRoom = [room]
                elif self.roomPriority[room] == minPriority:
                    minRoom.append(room)
                else:
                    pass

            # check if need switch
            if self.roomPriority[roomid] < minPriority:
                self.waitList.append(roomid)
                return

            # get oldest room
            if len(minRoom) > 1:
                minStartTime = 0xfffffffffff
                earlyRoom = ''
                for room in minRoom:
                    if self.roomStartTime[room] < minStartTime:
                        earlyRoom = room
                minRoom = [earlyRoom]

            print minRoom[0], 'pop'

            # switch
            self.serverList.remove(minRoom[0])
            if minRoom[0] not in self.waitList:
                self.waitList.append(minRoom[0])
            self.serverList.append(roomid)
            self.roomStartTime[roomid] = time.time()

    def remove_server(self, roomid):
        if roomid in self.serverList:
            self.serverList.remove(roomid)
        if roomid in self.waitList:
            self.waitList.remove(roomid)

        if len(self.serverList) < self.queueLength:
            #找优先级最高的
            maxPriority = -1
            maxRoom = []
            for room in self.waitList:
                if self.roomPriority[room] > maxPriority:
                    maxPriority = self.roomPriority[room]
                    maxRoom = [room]
                elif self.roomPriority[room] == maxPriority:
                    maxRoom.append(room)
                else:
                    pass

            if maxRoom == []:
                return

            maxRoom = maxRoom[0]
            self.serverList.append(maxRoom)
            self.waitList.remove(maxRoom)

    def change_server(self):
        print self.serverList, self.waitList, self.roomStartTime
        if len(self.serverList) < self.queueLength:
            return

        # get min priority in serverList
        minPriority = 999
        minRoom = []
        for room in self.serverList:
            if self.roomPriority[room] < minPriority:
                minPriority = self.roomPriority[room]
                minRoom = [room]
            elif self.roomPriority[room] == minPriority:
                minRoom.append(room)
            else:
                pass

        maxPriority = -1
        maxRoom = []
        for room in self.waitList:
            if self.roomPriority[room] > maxPriority:
                maxPriority = self.roomPriority[room]
                maxRoom = [room]
            elif self.roomPriority[room] == maxPriority:
                maxRoom.append(room)
            else:
                pass

        if minPriority > maxPriority:
            return

        turns = min(len(minRoom),len(maxRoom))
        for turn in range(turns):
            minStartTime = 0xffffffffffffff
            earlyRoom = ''
            for room in minRoom:
                if self.roomStartTime[room] < minStartTime:
                    minStartTime = self.roomStartTime[room]
                    earlyRoom = room
            minRoom.remove(earlyRoom)

            outRoom = earlyRoom
            inRoom = ''
            for room in self.waitList:
                if minPriority == self.roomPriority[room]:
                    inRoom = room
                    break
            maxRoom.remove(inRoom)
            if inRoom == '':
                return

            self.serverList.remove(outRoom)
            self.serverList.append(inRoom)
            self.roomStartTime[inRoom] = time.time()

            self.waitList.remove(inRoom)
            self.waitList.append(outRoom)


#    def remove_server(self, roomid):

