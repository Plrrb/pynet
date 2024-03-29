from sys import argv

from pynet import Client


class ChatClient(Client):
    def __init__(self, socket, name):
        self.socket = socket
        self.name = name
        self.msg = ""
        self.old_database = {}

    def on_send(self):
        return {self.name: self.msg}

    def on_recv(self, database):
        for user in database:
            if user == self.name:
                continue

            if user in self.old_database and database[user] != self.old_database[user]:
                print(user, ":", database[user])

        self.old_database = database

    def send_msg(self, msg):
        self.msg = msg


def main():
    c = ChatClient.from_address((argv[1], argv[2]), input("name: "))

    c.start()

    try:
        while True:
            msg = input("")
            c.send_msg(msg)
    except KeyboardInterrupt:
        print("Exited")


if __name__ == "__main__":
    main()
