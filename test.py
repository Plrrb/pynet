from pynet import Server


class MyServer(Server):
    def __init__(self, sock):
        self.socket = sock
        self.msg = ""

    def on_send(self):
        temp = self.msg
        self.msg = ""
        return temp

    def on_recv(self, data):
        if data != "":
            print(data)

    def send_msg(self, msg):
        self.msg = msg


address = "", 5555
s = MyServer.from_address(address)
s.start()

try:
    while True:
        i = input()
        s.send_msg(i)
except KeyboardInterrupt:
    pass
