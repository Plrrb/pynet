from pynet import Server, Client


class Device:
    def __init__(self, position, name):
        self.position = position
        self.other_drones = None
        self.name = name

    def get_data(self):
        return self.position

    def recv_data(self, data):
        self.other_drones = data["drones"]

        if data["msg"] == "ACT":
            print(self.name, "was activated")


class Controller:
    def __init__(self):
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)

    def get_data(self):
        return {
            "drones": tuple(d.get_data() for d in self.devices),
            "msg": "None",
        }

    def recv_data(self, data):
        print(data)


con = Controller()

s = Server.from_address(("127.0.0.1", 5555), con.get_data, con.recv_data)
s.start()
clients = []

for i in range(3):
    d = Device((i, 0), i)
    c = Client.from_address(("127.0.0.1", 5555), d.get_data, d.recv_data)

    con.add_device(d)
    clients.append(c)


{c.start() for c in clients}

while True:
    pass
