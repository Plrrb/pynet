import time
from sys import argv

from pynet import Client, Server


class ChatServer(Server):
    __slots__ = Server.__slots__ + ("database",)

    def __init__(self, socket):
        self.socket = socket
        self.database = {}

    def on_send(self):
        return self.database

    def on_recv(self, data):
        self.database.update(data)

    class ServerClient(Client):
        def __init__(self, socket, server_send, server_recv):
            self.socket = socket
            self.server_send = server_send
            self.server_recv = server_recv

        def on_send(self):
            return self.server_send()

        def on_recv(self, data):
            self.server_recv(data)


def main():
    s = ChatServer.from_address(("", int(argv[1])))
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
