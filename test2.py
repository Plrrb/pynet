from sys import argv
from pynet import Client


class MyClient(Client):
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


address = argv[1], int(argv[2])
c = MyClient.from_address(address)

c.start()
try:
    while True:
        i = input()
        c.send_msg(i)
except KeyboardInterrupt:
    pass
