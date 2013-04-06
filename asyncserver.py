#!/usr/bin/python

import errno
import socket
import functools

from tornado import ioloop

HOST = ''
PORT = 8085
BUFFER_SIZE = 1024
ADDRESS = (HOST, PORT)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.setblocking(0)
server_socket.bind(ADDRESS)
server_socket.listen(5)


def server(server_socket, fd, events):
    try:
        client_socket, address = server_socket.accept()
    except socket.error, e:
        if e.args[0] not in (errno.EWOULDBLOCK, errno.EAGAIN):
            raise
        return
    data = client_socket.recv(BUFFER_SIZE)
    client_socket.setblocking(0)
    client_socket.send('%s' % data)
    client_socket.close()
    return

io_loop = ioloop.IOLoop.instance()
callback = functools.partial(server, server_socket)
io_loop.add_handler(server_socket.fileno(), callback, io_loop.READ)
io_loop.start()
