# encoding=utf8
import socket
import time

host = ''
port = 33333
buffsize = 1024
addr = (host, port)

updsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
updsocket.bind(addr)


while True:
    # 接收元组第一个为 字节内容，第二个元素为addr
    data, addr = updsocket.recvfrom(buffsize)
    print('receive from ',addr)
    # if not data:
    #     break
    print('[%s] %s'%(time.ctime(), data.decode()))

    new_data = '[%s ]'%time.ctime() + data.decode()
    # 返回数据给客户端
    updsocket.sendto(new_data.encode(), addr)

# 服务器一般不会close
# updsocket.close()
