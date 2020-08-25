import socket
import time

#不可用，不知道为什么。也没显示远程连接被关闭

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    name = str(input('输入你想说的话'))
    s.sendto(name.encode('utf-8'),('114.55.106.242',9999))
    
    huihua = []

    print('已经发送')

    try:
        print(s.recv(1024).decode('utf-8'))
    except BaseException as identifier:
        pass
    print('已经回复')
