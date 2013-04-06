#!/usr/bin/python

import socket

HOST = ''
PORT = 8083
BUFFER_SIZE = 1024
ADDRESS = (HOST, PORT)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(ADDRESS)
server_socket.listen(5)

try:
    while True:
        client_socket, address = server_socket.accept()
        data = client_socket.recv(BUFFER_SIZE)
        client_socket.send('%s' % data)
        client_socket.close()
except:
    server_socket.close()
