import socket
import threading

class Server:

    def __init__(self, port: int):
        self.host = '127.010.0.0'
        self.port = port
        self.clients = []
        self.username_lookup = {}
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    def start(self):
        # self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind((self.host, self.port))
        self.s.listen(100)

        # generate keys ...

        while True:
            c, addr = self.s.accept() # waits for connect()
            username = c.recv(1024).decode() # waits for send()
            print(f"{username} tries to connect")
            self.broadcast(f'new person has joined: {username}') # prints out the message to all users
            self.username_lookup[c] = username
            self.clients.append(c)

            # send public key to the client 

            # ...

            # encrypt the secret with the clients public key

            # ...

            # send the encrypted secret to a client 

            # ...

            threading.Thread(target=self.handle_client,args=(c,addr,)).start()

    def broadcast(self, msg: str):
        for client in self.clients: 

            # encrypt the message

            # ...

            client.send(msg.encode())

    def handle_client(self, c: socket, addr): 
        while True:
            msg = c.recv(1024)

            for client in self.clients:
                if client != c:
                    client.send(msg)

if __name__ == "__main__":
    s = Server(9001)
    try:
        s.start()
    finally:
        s.s.close()