from socket import create_connection, create_server, socket

from .client import Client
from .network import __Network__


class Server(__Network__):
    __slots__ = __Network__.__slots__

    def loop(self):
        self.running = True

        while self.running:
            sock, address = self.sock.accept()

            self.add_client(sock, address)

    def add_client(self, sock: socket, address: tuple[str, int]):
        Client(sock, self.on_send, self.on_recv).start()

    def connect_to(self, address: tuple[str, int]):
        sock = create_connection(address)
        self.add_client(sock, address)

    @classmethod
    def from_address(cls, address: tuple[str, int], *args, **kwargs):
        sock = create_server(address)
        return cls(sock, *args, **kwargs)
