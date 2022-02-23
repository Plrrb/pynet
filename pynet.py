import socket
from pickle import dumps, loads
from threading import Thread


class Client:
    __slots__ = "socket", "on_send", "on_recv", "running"

    def __init__(self, socket, on_send, on_recv):
        self.socket = socket

        self.on_send = on_send
        self.on_recv = on_recv

    def start(self):
        Thread(target=self.loop, daemon=True).start()

    def stop(self):
        self.running = False

    def exit(self):
        self.running = False
        self.socket.close()

    def loop(self):
        self.running = True

        try:
            while self.running:
                self._send(self.on_send())

                self.on_recv(self._recv())
        except ConnectionError:
            self.exit()

    @classmethod
    def from_address(cls, address, *args, **kwargs):
        sock = socket.create_connection(address)
        return cls(sock, *args, **kwargs)

    def _send(self, data):
        data = dumps(data)

        self.socket.send(data)

    def _recv(self):
        data = self.socket.recv(512)
        data = loads(data)

        return data


class Server:
    __slots__ = "socket", "running"

    def __init__(self, socket):
        self.socket = socket

    def start(self):
        Thread(target=self.listen, daemon=True).start()

    def stop(self):
        self.running = False

    def listen(self):
        self.running = True
        self.socket.listen()

        while self.running:
            sock, address = self.socket.accept()

            self.connect_socket(sock, address)

    def connect_socket(self, sock, _):
        self.ServerClient(sock, self.on_send, self.on_recv).start()

    def connect_address(self, address):
        self.ServerClient.from_address(address, self.on_send, self.on_recv).start()

    # to be overwritten
    def on_send(self):
        raise Exception("Server.on_send() wasn't overwritten")

    # to be overwritten
    def on_recv(self, _):
        raise Exception("Server.on_recv() wasn't overwritten")

    @classmethod
    def from_address(cls, address, *args, **kwargs):
        sock = socket.create_server(address)
        return cls(sock, *args, **kwargs)

    class ServerClient(Client):
        pass
