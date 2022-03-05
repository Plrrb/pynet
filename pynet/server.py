from socket import create_server

from pynet.client import Client
from .network import Network


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
        def __init__(self, sock, server_send, server_recv):
            self.socket = sock

            self.server_send = server_send
            self.server_recv = server_recv

        def on_send(self):
            return self.server_send()

        def on_recv(self, data):
            self.server_recv(data)
