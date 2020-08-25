import socket
import threading
import time

def response(socks,addr):
    print("接受来自{}的连接".format(addr[0]))
    socks.send('i am melody'.encode('utf-8'))
    reuqests_response = []
    while True:
        # time.sleep(1)
        
        data = socks.recv(20*1024)          # 此处的recv是阻塞的，可以想象的是：此处的recv函数实际上会一直阻塞在此处
       
        if data:
            reuqests_response.append(data.decode('utf-8'))
            print(''.join(data.decode('utf-8')))

            socks.send(b"you are hack")
            
        else:
            print("关闭链接")
            # socks.close()
            exit()
    


    



if __name__ == "__main__":
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s. bind(('0.0.0.0',6379))

    s.listen(5)
    print("正在监听端口……")

    while True:
        socks,addr = s.accept()
        print("开始建立连接")
        a = threading.Thread(target=response,args=(socks,addr))
        a.start()
        a.join()




