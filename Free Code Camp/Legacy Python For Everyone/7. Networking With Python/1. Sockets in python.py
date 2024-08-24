"""
Python has built-in support for TCP Sockets
https://docs.python.org/3/library/socket.html
"""

import socket
# creates a socket but does not associate it
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#                host           port
mysock.connect(('data.pr4e.org', 80))

