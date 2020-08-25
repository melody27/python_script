import socket
import threading
                #此tcp连接脚本可用




def tcplink(s,addr):
    print('正在来自%s的连接'%''.join('%s'%id for id in addr))
    s.send('欢迎光临,我叫服务端'.encode('utf-8'))
    while True:
        data = s.recv(1024)
        if not data or data.decode('utf-8') == 'exit':
            # print(data.decode('utf-8'))
            s.send('那好啊,再见'.encode('utf-8'))
            break
        s.send(('你好啊%s'%(data.decode('utf-8'))).encode('utf-8'))
    
    s.close()
    print('聊天结束')


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('127.0.0.1',9999))

s.listen(5)
print('等到连接中……')

while True:
    sock,addr = s.accept()                  #此脚本，连接上了以后是从此处开始的。没连接上的话，就只会运行上面的
    print('整个脚本开始运行')
    
    t = threading.Thread(target=tcplink,args=(sock,addr))
    t.start()
    t.join()