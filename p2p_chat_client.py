from sys import argv

from p2p_chat_server import Chat


def main():
    address = argv[1], argv[2]
    c = Chat.from_address(address)
    c.start()
    print("you are now chatting, type 'EXIT' to disconnect")
    c.run()


if __name__ == "__main__":
    main()
