# Meowzzz Network Scanner
### *Currently in development...*

![Logo](https://cdn.discordapp.com/attachments/1129900240745533571/1146111968437084220/image.png)

Meowzzz is a compact Python program that scans and sweeps local IP addresses 
and determine open TCP/UDP ports using ICMP packets. It currently supports:


## Basic Features

- Guided user input
- Automated ICMP only ping requests
- Support for local networks (private LANS)
- Designed for Windows (can be modified for Linux)

## Proposed Features
- Router location
- Support for classless subnets (CIDR)
- Identifying port services 
- Implementing parallelism (to improve scanning time)

## Commands
| Command | Result |
| ------ | ------ |
| ScanIPs | scans all IPs in a local network (private addresses) |
| scanPort | scans a port number (port by port) |
| ScanIPA (proposed) | scans local network and all IP address ports (with default ports) |

## Current Command Flowchart *(In progress..)*
![Command flowchart](https://cdn.discordapp.com/attachments/1129900240745533571/1146108703964135505/image.png)


## Tech

Meowzzz currently uses:

- [Python] - sockets are used for development.
- [Windows CMD] - for ICMP pings
- [Alive Progress](https://github.com/rsalmei/alive-progress) - to show users scanner loading times


## References 
- [IP Scanner](https://www.makeuseof.com/python-ping-sweeper-how-build/)
- [Intro to Network Programming](https://www.studytonight.com/network-programming-in-python/introduction-to-network-programming)




