#!/usr/bin/python

import thread
import socket

HOST = ''
PORT = 8084
BUFFER_SIZE = 1024
ADDRESS = (HOST, PORT)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(ADDRESS)
server_socket.listen(5)

try:
    while True:
        client_socket, address = server_socket.accept()

        def response(client_socket):
            data = client_socket.recv(BUFFER_SIZE)
            client_socket.send('%s' % data)
            client_socket.close()

        thread.start_new_thread(response, (client_socket,))

except:
    server_socket.close()
