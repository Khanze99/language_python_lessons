import socket


class IOTask:
    def __init__(self):
        self._running = False

    def run(self, sock):
        sock.settimeout(5)
        while self._running:
            try:
                data = sock.recv(8192)
                break
            except socket.timeout:
                continue
