import socket
import threading
import time
from random import randint

MAX_CONNECTIONS = 20
address_to_server = ('localhost', 9000)

clients = [socket.socket(socket.AF_INET, socket.SOCK_STREAM) for i in range(MAX_CONNECTIONS)]
for client in clients:

    threading.Thread(target=client.connect, args=(address_to_server,)).start()

for client in clients:
    data = client.recv(1024)
    print(str(data))