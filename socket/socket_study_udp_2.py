import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    name = str(input('输入你想说的话'))
    s.sendto(name.encode('utf-8'),('127.0.0.1',9999))
    
    huihua = []

    
    print(s.recv(1024).decode('utf-8'))
        
