from pickle import dumps, loads
from socket import create_connection

from .network import Network


class Client(Network):
    __slots__ = Network.__slots__

    def loop(self):
        self.running = True

        try:
            while self.running:
                self._send(self.on_send())

                self.on_recv(self._recv())
        except (ConnectionError, EOFError):
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
