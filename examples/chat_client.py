from sys import argv

from pynet import Client


class ChatClient:
    def __init__(self, address, name):
        self.client = Client.from_address(address, self.on_send, self.on_recv)
        self.name = name
        self.msg = ""
        self.old_database = {}

    def start(self):
        self.client.start()

    def on_send(self):
        if self.msg == "EXIT":
            return None

        return {self.name: self.msg}

    def on_recv(self, database):
        if database is None:
            self.client.exit()
            return

        for user in database:
            if user == self.name:
                continue

            if user in self.old_database and database[user] != self.old_database[user]:
                print(user, ":", database[user])

        self.old_database = database

    def send_msg(self, msg):
        self.msg = msg


def main():
    c = ChatClient((argv[1], argv[2]), input("name: "))

    c.start()

    try:
        while True:
            msg = input("")
            c.send_msg(msg)
    except KeyboardInterrupt:
        print("Exited")


if __name__ == "__main__":
    main()
