import socket
import time

# Socket Init
HOST, PORT = "127.0.0.1", int(2333)

# Connect to Server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))


while 1:
	res = sock.recv(1024)
	opStr += res
	operate = opStr.split("_")

	if operate[0] == 'a' and len(operate) == 10:
		opStr = ''
		print operate
	if operate[0] == 'close' and len(operate) == 2:
		opStr = ''
		#close
	if operate[0] == 'sleep' and len(operate) == 2:
		opStr = ''
		#待机
	if operate[0] == 'wait' and len(operate) == 3:
		opStr = ''
		#啥是等待？

	# 3 Send the Answer to Server
	sendBuf = "aloha～"
	sock.send(sendBuf)
	print sendBuf

	time.sleep(0.1)
sock.close()
