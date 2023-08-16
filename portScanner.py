# script to scann all port numbers within a given network
import socket


def main():
    # try:
    #     ip = int(input("Select an IPv4 host name between 0.0.0.0 - 255.255.255.255:\n"))
    # except(ValueError):
    #     ip = socket.gethostbyname(str(input("Type a host name (www.hostname.net): \n")))

    temp_ip = input("Select an IPv4 address or host name to scan: \t")
    if temp_ip.isalpha():
        ip = socket.gethostbyname(temp_ip)
        print(ip)
    else:
        ip = temp_ip

    while True:
        port = int(input("Enter the port number to be scanned: (type 0 to exit)\n"))
        if port == 0:
            break
        else:
            try:
                so = socket.socket()
                res = so.connect((ip, port))
                print("Port ", port, "is open")
                so.close()
            except():
                print("Port ", port, "is closed")
    print("Scanning complete!! Nya!~")

