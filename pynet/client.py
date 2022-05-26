from pickle import dumps, loads
from socket import create_connection
from .network import __Network__


class Client(__Network__):
    __slots__ = __Network__.__slots__

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

        self.sock.send(data)

    def _recv(self):
        data = self.sock.recv(512)
        data = loads(data)

        return data

    @classmethod
    def from_address(cls, address: tuple[str, int], *args, **kwargs):
        sock = create_connection(address)
        return cls(sock, *args, **kwargs)
