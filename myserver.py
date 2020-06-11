import socket
import threading
from select import select
import sys
import argparse


def createParser():
    """ Принимаем аргумент из cli"""
    parser = argparse.ArgumentParser()
    parser.add_argument('--host')
    return parser


parser = createParser()
destination_host = parser.parse_args(sys.argv[1:]).host.replace('http://', '').replace('https://', '')

# Указываем адрес сервера назначения и прокси-сервера
destination_to = (destination_host, 80)
proxxy_to = ['127.0.0.1', 9000]


class Server:
    # input_list копит сокеты, управление которыми берет на себя select
    input_list = []
    # channel копит сопоставление конечных хостов (клиент - сервер назначения)
    channel = {}

    def __init__(self, host, port):
        """Инициализирует прокси-сервер"""
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((host, port))
        self.server.listen(200)

    def main(self):
        # Первым в список добавляется серверный сокет самого прокси-сервера
        self.input_list.append(self.server)

        while True:
            # Если текущий сокет из списка inputready, возвращенного select,
            # не предполагает новое соединение, значит, мы имеем дело с входящими данными
            # от сервера назначения или клиента
            inputready, outputready, exceptready = select(self.input_list, [], [])

            for self.s in inputready:
                # Если первый элемент списка - сокет сервера,
                # Асинхронно вызываем метод on_accept
                if self.s == self.server:
                    threading.Thread(target=self.on_accept(), ).start()
                    break

                # в противном случае пакет необходимо переслать в соответствующее место назначения.
                self.data = self.s.recv(4096)
                self.on_recv()

    def on_accept(self):
        # Метод устанавливает новое соединение с сервером назначения,
        # а также принимает подключение текущего клиента.
        destination = Destination().start(destination_to[0], destination_to[1])
        clientsock, clientaddr = self.server.accept()

        if destination:

            print("Client {}:{} connected".format(clientaddr[0], clientaddr[1]))

            # Оба сокета добавляются в список input_list
            self.input_list.append(clientsock)
            self.input_list.append(destination)

            # Оба сокета также сохраняются в словаре channel
            self.channel[clientsock] = destination
            self.channel[destination] = clientsock

        else:

            print("Can't connect to {}:{}".format(destination_to[0], destination_to[1]))
            print("Closing connection to client {}:{}".format(clientaddr[0], clientaddr[1]))
            clientsock.close()

    def on_recv(self):
        # Редиректим данные по месту назначения
        self.channel[self.s].send(self.data)


class Destination:
    """Инициализируем соединение между прокси и сервером назначения"""
    def __init__(self):
        self.destination = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self, host, port):
        try:
            self.destination.connect((host, port))
            return self.destination

        except Exception:
            return False


if __name__ == '__main__':

    server = Server(proxxy_to[0], proxxy_to[1])

    try:
        print('Proxxy server is available at {}:{}. Press ctrl+c to stop'.format(proxxy_to[0], proxxy_to[1]))
        server.main()

    except KeyboardInterrupt:
        print("Stopping proxxy")
