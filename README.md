# Meowzzz Network Scanner
### *Currently in development...*
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

## Tech

Meowzzz currently uses:

- [Python] - sockets are used for development.
- [Windows CMD] - for ICMP pings
- [Alive Progress](https://github.com/rsalmei/alive-progress) - to show users scanner loading times


## References 
- [IP Scanner](https://www.makeuseof.com/python-ping-sweeper-how-build/)
- [Intro to Network Programming](https://www.studytonight.com/network-programming-in-python/introduction-to-network-programming)
