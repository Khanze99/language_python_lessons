import socket
import argparse
import enum
import time


parser = argparse.ArgumentParser(description='Process socket')
parser.add_argument('-t', default=0, type=int)


class TypeStart(enum.Enum):
    SERVER = 0
    CLIENT = 1


def server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 8000))
    sock.setblocking(False)
    sock.listen(5)
    while True:
        try:
            conn, addr = sock.accept()
            handle_connection(conn, addr)
            break
        except BlockingIOError:
            print('Err')
            time.sleep(2)


def client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 8000))


def handle_connection(conn, addr):
    print(conn, addr)


if __name__ == '__main__':
    arg = parser.parse_args()
    _type = TypeStart(arg.t)

    if _type is TypeStart.SERVER:
        server()
    elif _type is TypeStart.CLIENT:
        client()




