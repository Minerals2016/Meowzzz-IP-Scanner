# This script sets up a TCP client
import socket


def main():
    so = socket.socket()
    host = socket.gethostname()
    port = 9999

    print("Client side messaging...")

    def message():
        messageText = str(input("Enter your message here (type \"exit\" to exit)-> "))
        if (messageText == "exit"):
            so.close()
        else:
            so.connect((host, port))
            so.sendall(messageText)
            data = so.recv(1024)
            print(data)
            message()
    message()
#    so.close()
