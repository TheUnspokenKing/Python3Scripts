#!/usr/bin/python3
import socket,sys

host = sys.argv[1]

print(host,"--->",socket.gethostname(host))