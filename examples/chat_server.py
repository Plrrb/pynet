import time
from sys import argv

from pynet import Server


class Chat:
    def __init__(self, address):
        self.database = {}
        self.server = Server.from_address(address, self.on_send, self.on_recv)

    def start(self):
        self.server.start()

    def on_send(self):
        return self.database

    def on_recv(self, data):
        self.database.update(data)


def main():
    s = Chat(("", int(argv[1])))
    s.start()


if __name__ == "__main__":
    import socket

    print("server local ip", socket.gethostbyname(socket.gethostname()))
    main()

    try:
        while True:
            time.sleep(100)
    except KeyboardInterrupt:
        print("Exited")
