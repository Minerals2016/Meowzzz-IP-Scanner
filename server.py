# This script sets up a TCP server

import socket


def main():
    so = socket.socket() # create so - a socket object
    host = socket.gethostname()
    hostIP = socket.gethostbyname(socket.gethostname())
    port = 9998

    so.bind((host, port))

    print("Host:", hostIP, " \nWaiting for connection...")
    so.listen(5)
    conn, addr = so.accept()
    print("Connected by ", addr)
    while(True):
        conn.send("Connection request accepted!! Meow Meow~")
        data = conn.recv(1024)
        d = data.split("|")
        conn.sendall(d)
        conn.close()
