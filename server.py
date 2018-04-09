import SocketServer

FLAG = "Aloha, this is SocketServer"

class HandleCheckin(SocketServer.StreamRequestHandler):
    # 3 Call this function when recv a connection from client
    def handle(self):
        # 4 Send the question
        req = self.request
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
