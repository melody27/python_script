import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind(('0.0.0.0',9999))

print('开始监听9999端口的udp')


while True:
    
    data,addr = s.recvfrom(1024)
    print(addr)
    print('正在接收来自%s的信息'%(addr[0]))
    s.sendto(('你好啊%s'%(data.decode('utf-8'))).encode('utf-8'),addr)
    print('已经回话')
