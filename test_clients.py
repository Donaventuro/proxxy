import socket
import threading
import time
from random import randint

MAX_CONNECTIONS = 20
address_to_server = ('localhost', 9000)

clients = [socket.socket(socket.AF_INET, socket.SOCK_STREAM) for i in range(MAX_CONNECTIONS)]
for client in clients:

    threading.Thread(target=client.connect, args=(address_to_server,)).start()
    # client.connect(address_to_server)
    #
    # threading.Thread(target=).start
    #

for i in range(MAX_CONNECTIONS):
    clients[i].send(bytes("hello from client number " + str(i), encoding='UTF-8'))

for client in clients:
    data = client.recv(1024)
    print(str(data))