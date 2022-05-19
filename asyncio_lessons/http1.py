import socket
import random
import sys
import time
import selectors  # из всех зоопарков сокетов разных ОС в один апи

# написать handle_exception на async/await


async def handle_connection(conn, addr):
    print("Connected by", addr)

    with conn:
        while True:
            data = await conn.recv(1024)
            if not data:
                break

            n = int(data.decode())
            res = f"{n * 2}\n".encode()
            await conn.send(res)
    print("Disconnected by", addr)


def doubler_server(port=8080):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", port))
        s.setblocking(False)  # делает этот сокет неблокирующем
        s.listen(5)
        sel = selectors.DefaultSelector()
        sel.register(s, selectors.EVENT_READ)
        while True:
            for key, mask in sel.select():
                # key namedtuple что произошло
                # key.fileobj
                # key.events
                # key.data
                if key.fileobj is s:
                    conn, addr = s.accept()
                    print("Connected by", addr)
                    conn.setblocking(False)
                    sel.register(conn, selectors.EVENT_READ, ('read', None))
                else:
                    conn = key.fileobj
                    op, arg = key.data
                    sel.unregister(conn)
                    if op == "read":
                        data = conn.recv(1024)
                        if not data:
                            conn.close()
                        n = int(data.decode())
                        res = f"{n * 2}\n".encode()
                        sel.register(conn, selectors.EVENT_WRITE, ('write', res))
                    elif op == "write":
                        conn.send(arg)
                        sel.register(conn, selectors.EVENT_READ, ("read", None))
                    else:
                        assert False, (op, arg)


def doubler_client():
    with socket.create_connection(("127.0.0.1", 8080)) as s:
        f = s.makefile(mode="rw", buffering=1, newline="\n")
        while True:
            n = random.randrange(10)
            f.write(f"{n}\n")
            print(n, f.readline().strip())
            time.sleep(random.random() * 2)


if __name__ == '__main__':
    if sys.argv[1] == "server":
        doubler_server()
    else:
        assert sys.argv[1] == "client"
        doubler_client()
