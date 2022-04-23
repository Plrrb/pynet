from socket import create_server
from .network import Network
from .client import Client


class Server(Network):
    __slots__ = Network.__slots__

    def loop(self):
        super().loop()

        while self.running:
            sock, address = self.socket.accept()

            self.add_client(sock, address)

    def add_client(self, sock, _):
        c = Client(sock, self.on_send, self.on_recv)
        c.start()

    @classmethod
    def from_address(cls, address, *args, **kwargs):
        sock = create_server(address)
        return cls(sock, *args, **kwargs)
