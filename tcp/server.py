import socket

sock = socket.socket()
sock.bind(('localhost', 80, ))
sock.listen()