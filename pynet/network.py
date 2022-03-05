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
