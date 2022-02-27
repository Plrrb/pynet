# Pynet

Pynet is a Python library for making Servers and Clients.

## Demo

The chat_server.py and chat_client.py is a simple terminal chat program.

Start the chat server like this put a port number where it says [port]:

```bash
python3 chat_server.py [port]
```

to start a client run this with the servers ip address, and the port you gave the server:

```bash
python3 chat_client.py [ip] [port]
```

## Usage/Examples

A simple client that sends "Hello World!" And prints what it receives:

```py
from sys import argv
from pynet import Client


def on_send():
    return "Hello World!"


def on_recv(data):
    print(data)


# This gets the IP and port from the terminal arguments and converts the port to an int
address = (argv[1], int(argv[2]))
client = Client.from_address(address, on_send, on_recv)

client.loop()
```

A server that takes clients data adds it to a database and send it to other clients:

```py
from sys import argv
from pynet import Server

database = {}

def on_send():
    return database

def on_recv(data):
    database.update(data)

address = "", int(argv[1])

s = Server.from_address(address, on_send, on_recv)
s.loop()
```

## Installation

Install with git:

```bash
git clone https://www.github.com/Plrrb/pynet.git
```
