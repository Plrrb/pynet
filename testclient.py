from sys import argv
from pynet import Client


class MyClient(Client):
    def __init__(self, sock):
        self.socket = sock

    def on_send(self):
        return {"text2": input("send: ")}

    def on_recv(self, data):
        print(data)


c = MyClient.from_address((argv[1], int(argv[2])))
c.loop()
