from pickle import dumps, loads
from socket import create_connection, create_server
from threading import Thread


class Network:
    __slots__ = "socket", "on_send", "on_recv", "running"

    def __init__(self, sock, on_send, on_recv):
        self.socket = sock

        self.on_send = on_send
        self.on_recv = on_recv

    def start(self):
        Thread(target=self.loop, daemon=True).start()

    def stop(self):
        self.running = False

    def exit(self):
        self.running = False
        self.socket.close()


class Client(Network):
    __slots__ = Network.__slots__

    def loop(self):
        self.running = True

        try:
            while self.running:
                self._send(self.on_send())

                self.on_recv(self._recv())
        except ConnectionError:
            self.exit()

    def _send(self, data):
        data = dumps(data)

        self.socket.send(data)

    def _recv(self):
        data = self.socket.recv(512)
        data = loads(data)

        return data

    @classmethod
    def from_address(cls, address, *args, **kwargs):
        sock = create_connection(address)
        return cls(sock, *args, **kwargs)


class Server(Network):
    __slots__ = Network.__slots__

    def loop(self):
        self.running = True
        self.socket.listen()

        while self.running:
            sock, address = self.socket.accept()

            self.connect_socket(sock, address)

    def connect_socket(self, sock, _):
        self.ServerClient(sock, self.on_send, self.on_recv).start()

    def connect_address(self, address):
        self.ServerClient.from_address(address, self.on_send, self.on_recv).start()

    @classmethod
    def from_address(cls, address, *args, **kwargs):
        sock = create_server(address)
        return cls(sock, *args, **kwargs)

    class ServerClient(Client):
        pass
