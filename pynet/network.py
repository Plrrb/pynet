from socket import socket
from threading import Thread


class __Network__:
    __slots__ = "sock", "on_send", "on_recv", "running"

    def __init__(self, sock: socket, on_send, on_recv):
        self.running = False
        self.on_recv = on_recv
        self.on_send = on_send
        self.sock = sock

    def start(self):
        if self.running:
            return
        else:
            self.running = True
            Thread(target=self.loop, daemon=True).start()

    def stop(self):
        self.running = False

    def exit(self):
        self.running = False
        self.sock.close()
