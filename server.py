#-*- coding:utf-8 -*-
import SocketServer


class HandleCheckin(SocketServer.StreamRequestHandler):
    # 3 Call this function when recv a connection from client
    def handle(self):
        # 4 Send the question
        req = self.request


        opStr = ''
        while 1:
            res = req.recv(1024).strip()
            opStr += res
            operate = opStr.split("_")

            if operate[0] == 'r' and len(operate) == 5:
                opStr = ''
                print operate
            if operate[0] == 'c' and len(operate) == 5:
                opStr = ''
                #close
            if operate[0] == 'close' and len(operate) == 2:
                opStr = ''
                #待机
            if operate[0] == 'wait' and len(operate) == 3:
                opStr = ''
                #啥是等待？
            time.sleep(0.1)



        req.sendall("The answer of life, universe and everything:\n")

        # 5 Receive the answer
        answer = req.recv(1024).strip()

        # 6 Check the answer
        if(answer == "42") :
            # 7 Send the Flag to Client
            req.sendall("=== Mission Complete ===\n")
            req.sendall(FLAG + "\n")
        else :
            return

class ThreadedServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

if __name__ == "__main__":
    # 1 Set Host and Port
    HOST, PORT = "127.0.0.1", int(2333)

    # 2 Start Server
    server = ThreadedServer((HOST, PORT), HandleCheckin)
    server.allow_reuse_address = True
    server.serve_forever()
