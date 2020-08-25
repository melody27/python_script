import socket

# socks5握手连接demo

'''
协议内容来自：
https://www.cnblogs.com/yinzhengjie/p/7357860.html
https://blog.csdn.net/yetugeng/article/details/89503557

'''


# 如果要启用密码支持的话，那么用户名为melody 密码为123456



socks = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socks.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
socks.bind(("127.0.0.1",9998))
socks.listen(10)
while True:
    ss,addr = socks.accept()
    while True:
        result = ss.recv(1024)
        if not result:                                                                      # 连接中断即退出
            exit("连接中断，退出")
        print("请求为:",result)
        if result[:1] == b'\x01' and (result[1] + result[2+result[1]] + 3) == len(result):      # 此处的特征为密码认证的密码
            print("表示密码长度的为",ord(result[1:2]))                                           # 




        if ord(result[1:2].decode('latin1')) == len(result[2:]) and result[:1] == b'\x05':      # 第一次握手确定连接方式
            ss.sendall((chr(5)+chr(2)).encode('latin1'))        # 此处确定验证方法,使用密码则为：chr(2)，免验证则为：chr(0)
            print("响应的数据为：",(chr(5)+chr(00)).encode('latin1'))
            print('\n\n\n')
            continue
        

        elif result[:1] == b'\x01' and (result[1] + result[2+result[1]] + 3) == len(result):        # 第二次握手验证密码登录的密码
            print(result[1])                                 # 认证包的第一个字节为\x01而不是\x05
            print("进入密码认证")
            username = result[2:2+result[1]].decode('utf-8')
            passwd = result[2+result[1]+1:].decode('utf-8')
            print("用户名为：",username,"\n密码为：",passwd)
            if username == 'melody' and passwd == '123456': # 密码正确的情况下
                ss.sendall(b'\x01\x00')
                print("密码认证正确")
                print('\n\n\n\n')
                continue
                

        elif result[:3] == b'\x05\x01\x00' and len(result) >= 10 :                      # 第三次握手确定
            print('\n这是第二次响应')
            print("VER目标版本号位置为：",result[:1])
            print("CMD表示请求状态的字节为：",result[1:2])
            print("RSV此为保留字",result[2:3])
            print("ATYP表示的描述远程地址的类型为:",result[3:4])
            if result[3:4] == b'\x01':                                                  # 解析IPV4
                print("DST.ADDR远程地址为",result[4:8])
            elif result[3:4] == b'\x03':                                                # 解析域名，暂不提供IPV6的解析。此脚本最后有，解析IPV6的参考
                raw_len_host = result[4:5]                                          
                len_host = ord(raw_len_host.decode('latin1'))           
                print("真实的host长度为",len_host)
                host = result[5:5+len_host]
                print("真实的host为",host)

            raw_port = result[-2:]
            port = raw_port[0]*256 + raw_port[1]
            print("port为",port)
            if result[3:4] == b'\x01':
                ss.sendall(b'\x05\x00\x00'+result[3:4]+result[4:8]+raw_port)
                print(" ip 第二次响应的数据为",b'\x05\x00\x00'+result[3:4]+result[4:8]+raw_port)
                print('\n\n\n')
                continue
            elif result[3:4] == b'\x03':
                ss.sendall(b'\x05\x00\x00'+result[3:4]+chr(len(host)).encode('latin1')+host+raw_port)
                print("域名第二次响应的数据为",b'\x05\x00\x00'+result[3:4]+chr(len(host)).encode('latin1')+host+raw_port)
                print('\n\n\n')
                continue
            print("响应为：",ss.recv(1024))
        # ss.sendall(str(input("输入你想要的响应")))


'''
elif handle_data_2[3] == 4:                     # 解析IPV6，不确定此脚本是否可用
    IPV6 = handle_data_2[4:20]
    result_list = []
    for i in range(len(IPV6) // 2):
        result_list.append(unichr(ord(IPV6[2 * i]) * 256 + ord(IPV6[2 * i + 1])))
    result = ":".join(result_list)
'''