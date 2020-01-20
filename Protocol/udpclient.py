# encoding=utf8
import socket

host = 'localhost'
port = 33333
addr = (host, port)
buffsize = 1024

udpsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    data = input('input data:')
    # 发送内容为空关闭套接字
    if not data:
        break
    # 把输入内容发送给服务器
    udpsocket.sendto(data.encode(),addr)

    # 接收服务器返回数据
    data = udpsocket.recvfrom(buffsize)
    print(data[0].decode())
udpsocket.close()