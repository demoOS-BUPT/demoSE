import math, time


class Algo(object):

	def __init__():
		self.roomPriority = {'503':1,'504':2,'505':2,'506':3}

		self.roomList = ['503', '504', '505', '506']

		self.serverList = []
		self.waitList = []
		self.roomStartTime = {}

		self.queueLength = 2

	def req_server(self, roomid):
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
			self.roomPriority[roomid] = time.time()

	def change_server(self):
		if len(self.serverList) < self.queueLength:
			return

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

		if len(minRoom) > 1:
			minStartTime = 0xfffffffffff
			earlyRoom = ''
			for room in minRoom:
				if self.roomStartTime[room] < minStartTime:
					earlyRoom = room
			minRoom = [earlyRoom]

		print minRoom[0], 'oldest' 

		outRoom = minRoom[0]

		inRoom = ''
		for room in self.waitList:
			if minPriority == self.roomPriority[room]:
				inRoom = room
				break

		if inRoom == '':
			return

		self.serverList.remove(outRoom)
		self.serverList.append(inRoom)
		self.roomStartTime[inRoom] = time.time()

		self.waitList.remove(inRoom)
		self.waitList.append(outRoom)
