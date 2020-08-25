import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('192.168.2.55',9999))       #此脚本可用

print(s.recv(1024).decode('utf-8'))

while True:
    name = str(input('输入你要说的话'))
    s.send(name.encode('utf-8'))
    print(s.recv(1024).decode('utf-8'))

    if name == 'exit':
        break
s.close