from threading import Thread


class Network:
    __slots__ = "socket", "on_send", "on_recv", "running"

    def __init__(self, sock, on_send, on_recv):
        self.on_recv = on_recv
        self.on_send = on_send
        self.running = False
        self.socket = sock

    def start(self):
        Thread(target=self.loop, daemon=True).start()

    def loop(self):
        if self.running:
            return

        self.running = True

    def stop(self):
        self.running = False

    def exit(self):
        self.running = False
        self.socket.close()
        self.on_recv(None)
