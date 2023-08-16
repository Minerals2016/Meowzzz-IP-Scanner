#
# import socket
#
# clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# clientsocket.connect(("www.niicomii.tech", 80))
# socket.gethostbyname(socket.gethostname())
import time

from progress.bar import Bar
from alive_progress import alive_bar

def main():
    def compute():
        with alive_bar(30, force_tty=True) as bar:  # your expected total
            for i in range(30):  # the original loop
                time.sleep(0.01)
                print("uwu")  # your actual processing here
                bar()  # call `bar()` at the end

    compute()