import socket

# 需要注意的是，在服务端的socket.recv()函数中是阻塞的，所以不能够使用while循环来进行循环接受。需要注意的是：recv函数本身是阻塞的，不管其是否在客户端或服务端。
    # recv函数都会将其阻塞掉


ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ss.connect(('127.0.0.1',6379))
ss.send(b'PING')

while True:
    requests_content = str(input('input:'))
    ss.send(requests_content.encode('utf-8'))

    # 输出一下响应：
    print(ss.recv(1024))
    if requests_content == 'exit':
        ss.send(b'bye bye')
        ss.close()



ss.close()
