serverAddress = ("0.0.0.0", 9339)

import socket
from Heart.Connection import Connection
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, True)
server.bind(serverAddress)
print(f"Heart beats on {serverAddress[0]}:{serverAddress[1]}")
while True:
    server.listen()
    socket, address = server.accept()
    print(f"New player: {address[0]}:{address[1]}")
    Connection(socket, address).start()