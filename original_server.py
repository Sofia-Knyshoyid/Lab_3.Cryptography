import socket
import threading
import hashlib
from encrypt_alg import gener_keys_get_message, encrypt_message, decrypt_message

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
            # self.broadcast(f'new person has joined: {username}') # prints out the message to all users
            self.username_lookup[c] = username
            self.clients.append(c)

            # send public key to the client 
            

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
            raw_received = c.recv(1024).decode()
            received = raw_received.split(' ')
            msg, edited, e, n, d, receiver, username, hash_val = received[0], int(received[1]), int(received[2]),\
                int(received[3]), int(received[4]), received[5], received[6], received[7]
            # get the message.encode, edited, e, n, d
            msg_decoded = decrypt_message(msg, d, n, edited)
            if receiver == 'AllUsers':
                print(f'_________server received a message from {username}!________')
                
                got_message = msg_decoded
                # print(got_message, '  serv got message')
                got_message = got_message.encode('utf-8')
                sha3_512 = hashlib.sha3_512(got_message)
                sha3_512_hex_digest = sha3_512.hexdigest()
                # print(sha3_512_hex_digest, 'serv hexidigest')
                # print('Printing hexadecimal output')
                # print(sha3_512_hex_digest)
                print(f'...Checking the message integrity: {str(sha3_512_hex_digest) == hash_val}')


                print(msg_decoded)
            else:
                print(f'_________server received a private for {receiver}!_________')
                for client in self.clients:
                    if client != c and self.username_lookup[client] == receiver:
                        print('...server identified the receiver, redirecting message')
                        client.send(raw_received.encode())
            

            # for client in self.clients:
            #     if client != c:
            #         client.send(msg_decoded)

if __name__ == "__main__":
    s = Server(9005)
    try:
        s.start()
    finally:
        s.s.close()
