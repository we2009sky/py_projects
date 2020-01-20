# encoding=utf8
import socket

host = 'localhost'
port = 22222
buffsize = 1024
addr = (host, port)

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.connect(addr)

while True:
    data = input('input data: ')
    if not data:
        break
    tcpsock.send(data.encode())
    data = tcpsock.recv(buffsize)
    print(data.decode())
tcpsock.close()