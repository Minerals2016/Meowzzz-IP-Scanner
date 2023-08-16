import os
import socket
from colorama import Fore, Style


def main(IP, subnetClass):
    def ipCount(IP, selector_A, selector_B, selector_C):
        targetIPs = []
        splitIP = IP.split(".")
        hostCount = 0

        for i in range(0, selector_A):
            splitIP[1] = str(i)

            for l in range(0, selector_B):
                splitIP[2] = str(l)

                for y in range(0, selector_C):
                    splitIP[3] = str(y)
                    hostCount += 1
                    IP2 = ".".join(splitIP)
                    #print(str(hostCount) + ": " + str(IP2))
                    targetIPs.append(IP2)
        return targetIPs

    if len(IP.split(".")) != 4:
        raise Exception("IP length is incorrect. (Note: Meowzzz only supports IPv4)")

    elif subnetClass == 1:
        return ipCount(IP, 256, 256, 256)

    elif subnetClass == 2:
        return ipCount(IP, 1, 256, 256)

    elif subnetClass == 3:
        return ipCount(IP, 1, 1, 256)

    else:
        raise Exception("subnetClass must be a value between 1 and 3 (inclusive)")
