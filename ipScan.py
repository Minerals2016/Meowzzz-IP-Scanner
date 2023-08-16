# Reference from https://www.makeuseof.com/python-ping-sweeper-how-build/
# Utilized this package: https://github.com/rsalmei/alive-progress

import os
import socket
from colorama import Fore, Style
from alive_progress import alive_bar

from SocketPractice import ipCount


def main():
    hostIP = str(socket.gethostbyname(socket.gethostname()))

    def networkID(subnetClass):
        result = ""
        octetCount = 0
        for i in range(len(hostIP)):
            if hostIP[i] == ".":
                octetCount += 1
            if octetCount < subnetClass:
                result += hostIP[i]
            if octetCount == subnetClass:
                result += "."
                break
        return result

    hostIP_A = str(networkID(1) + "0.0.0")
    hostIP_B = str(networkID(2) + "0.0")
    hostIP_C = str(networkID(3) + "0")

    # get the list of hosts to scan
    targetList = ipCount.main(hostIP_C, 3)

    def scanIP(IP):
        response = os.system("ping -n 1 -w 1 " + IP + " >nul")

        if response == 0:
            print(Fore.GREEN + "- " + IP + " is up -" + Style.RESET_ALL)
        # else:
        #     print(Fore.RED + "- " + IP + " is down -" + Style.RESET_ALL)

    # ICMP scan IPs
    totalScanned = 0
    with alive_bar(len(targetList)-1, force_tty=True) as bar:
        for i in range(len(targetList)):
            scanIP(targetList[i])
            totalScanned += 1
            bar()
    print("Scanned ===> " + str(totalScanned - 1) + " host(s)")
