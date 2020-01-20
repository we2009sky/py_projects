# encoding=utf8
import socket
import time

host = ''
port = 22222
buffsize = 1024
addr = (host, port)

tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsocket.bind(addr)
tcpsocket.listen(10)

while True:
    print('Waiting for connection...')
    sub_sock, addr = tcpsocket.accept()
    print('Connected from ', addr)

    while True:
        data = sub_sock.recv(buffsize)
        if not data:
            break

        new_data = '[%s] '%(time.ctime()) + data.decode()
        sub_sock.send(new_data.encode())
        # sub_sock.send('[{}] {}'.format(time.ctime().encode(), data))

    sub_sock.close()


