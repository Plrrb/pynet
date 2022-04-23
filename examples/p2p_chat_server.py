from socket import create_server, gethostbyname, gethostname
from sys import argv

from pynet import Client


class Chat(Client):
    def __init__(self, sock):
        self.socket = sock
        self.msg = ""

    def on_send(self):
        if self.msg == "EXIT":
            self.stop()

        temp = self.msg
        self.msg = ""
        return temp

    def on_recv(self, data):
        if data != "":
            print(data)
        elif data == "EXIT":
            self.stop()

    def send_msg(self, msg):
        self.msg = msg

    def run(self):
        while self.running:
            i = input()
            self.send_msg(i)
        self.exit()


def main():
    print(f"IP: {gethostbyname(gethostname())}, Port: {argv[1]}")

    address = "", int(argv[1])
    s = create_server(address)
    s.listen()
    sock, address = s.accept()

    c = Chat(sock)

    c.start()
    print("you are now chatting, type 'EXIT' to disconnect")

    c.run()


if __name__ == "__main__":
    main()
