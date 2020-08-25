import gevent.monkey            # 必须在程序的最前面导入gevent的monkey包。否则会出现，超出最大递归数的报错
gevent.monkey.patch_all()
import gevent
import gevent
import socket
from urllib import parse
import urllib3
from threading import Thread
import time
import sys

# 不知怎么的，此脚本很慢。实际的话，需要进行优化

BASICCHECKSTRING = "Georg says, 'All seems fine'"
READBUFSIZE = 1024
VER = '\x05'
METHOD = '\x00'
# READ_TIMES = 0        # 统计响应次数和请求次数
# WRITE_TIMES = 0


# this is a demo for reGeory client 
# 如果变量为byted类型的话，那么使用迭代的方式来取的话，会自动的转化为十进制。
# x = b'\x34\x35\x36'
# print(x[2])       # 此处自动的输出54


class Session(Thread):

    def __init__(self,Psocket,connect_string):
        Thread.__init__(self)
        self.Psocket = Psocket
        self.connect_string = connect_string
        o = parse.urlparse(connect_string)
        try:
            self.http_port = o.port
        except Exception as identifier:
            if o.scheme == "https":
                self.http_port = 443
            elif o.scheme == "http":
                self.http_port = 80
        self.http_host = o.netloc
        self.http_path = o.path

        if o.scheme == "https":
            self.http_scheme = urllib3.HTTPSConnectionPool
        elif o.scheme == "http":
            self.http_scheme = urllib3.HTTPConnectionPool
        


    def run(self):
        
        if self.handleSocks(self.Psocket):
            print("握手成功")
            # r = gevent.spawn(self.reader)        # 先拉取数据
            # gevent.joinall([gevent.spawn(self.reader)])

            # w = gevent.spawn(self.writer)        # 此处将多线程修改为协程
            gevent.joinall([gevent.spawn(self.reader),gevent.spawn(self.writer)])       # 将原本的多线程修改为协程
            r.join()
            w.join()


    def reader(self):
        # global READ_TIMES
        conn = urllib3.PoolManager()
        while True:
            try:
                if not self.Psocket:exit("连接中断，退出")
                headers = {
                    "X-CMD":"READ",
                    "Cookie":self.cookie,
                    "Connection":"Keep-Alive"
                }
                response = conn.urlopen("POST",self.connect_string,headers=headers,body="")
                if response.status == 200:
                    if response.getheader("x-status") == "OK":
                        data = response.data
                        if data is None:
                            pass
                        
                    else:
                        exit("reader的x-status状态不为ok，退出")
                else:
                    exit("reader的响应状态码不为200，退出")        
                if len(data) == 0:
                    time.sleep(0.1)
                    continue
                self.Psocket.sendall(data)
                # READ_TIMES += 1       
                # print("响应次数为：",READ_TIMES)
            except Exception as identifier:
                print("读取出错")


    def writer(self):
        # global WRITE_TIMES
        print("进入写数据的函数中")
        global READBUFSIZE
        conn = urllib3.PoolManager()
        while True:
            data = self.Psocket.recv(READBUFSIZE)
            if not data:
                print("写入结束")
                break
            # WRITE_TIMES += 1
            # print("写入次数为",WRITE_TIMES)
            headers = {"X-CMD":"FORWARD","Cookie":self.cookie,"Content-type":"application/octet-stream","Connection":"Keep-Alive"}
            response = conn.urlopen("POST",self.connect_string,headers=headers,body=data)
            # print("正在写入数据中：",data)
            if response.status == 200:
                status = response.getheader("x-status")
                if status == "OK":
                    if response.getheader("set-sookie") is not None:
                        self.cookie = response.getheader("set-cookie")
                else:
                    print("服务端开起来貌似已经关闭")
            else:
                print("发送数据失败，目标无响应")
        

        # 握手并且在服务端建立session
    def setupSession(self,target,target_port):
        headers = {"X-CMD":"CONNECT","X-TARGET":target,"X-PORT":str(target_port)}
        self.target = target
        self.target_port = target_port
        cookie = None
        conn = self.http_scheme(host=self.http_host,port=self.http_port)

        response = conn.urlopen("POST",self.connect_string, headers=headers)
        print(response.status)
        if response.status == 200:
            cookie = response.getheader("set-cookie")
            print("保存的cookie为：",(cookie))
            if response.getheader("X-ERROR"):
                print("状态为;",response.getheader("X-ERROR"))
            print("请求头为：",headers)
        conn.close()
        return cookie

    def closeSession(self):
        headers = {"X-CMD":"DISCONNECT","Cookie":self.cookie}
        conn = self.http_scheme(host=self.http_host,port=self.http_port)
        r = conn.urlopen("POST",self.connect_string,headers=headers)
        if r.status == 200:
            print("已经杀死链接")
        conn.close()



    def socks_5(self,ss):
        print("开启socks连接,默认不支持密码验证(ps.客户端密码验证没有意义)")
        handle_data_1 = ss.recv(1024)     # 接受剩余的字节
        ss.sendall(b'\x05\x00')         # 响应客户端使用免验证登录
        handle_data_2 = ss.recv(1024)
        print(handle_data_2)
        if handle_data_2[0] != 5:exit('协议错误退出')
        if handle_data_2[1] != 1:print("不支持的方式,bind or udp，socks不支持. 退出")
        if handle_data_2[3] == 1:                       # 解析IP,           此处handle_data_2[3] 实际上为客户端确定的ipv4,域名，ipv6支持
            ip = ".".join( str(ord(x)) for x in handle_data_2[4:8].decode('latin1'))
            target = ip
            port = handle_data_2[-2] *256 + handle_data_2[-1]       # 优化一下
            target_port = port 
            print("目标IP为：",ip)
            print("目标端口为",port)

                    # 简单测试ip连接是否能够成功
            # ss.sendall(b'\x05\x00\x00\x01'+ handle_data_2[4:])                  # 后面的数据实际上就是相当于复制请求中的域名和port而已，所以此处直接复制即可
            # print("发送的数据为      ：",b'\x05\x00\x00\x01'+ handle_data_2[4:]) 
            # print("真实的data为:",ss.recv(1024))
        elif handle_data_2[3] == 3:                     # 解析域名
            host_name = handle_data_2[5:handle_data_2[4]+5].decode('utf-8')
            target = host_name
            port = handle_data_2[-2] *256 + handle_data_2[-1]       # 优化一下
            target_port = port
            print("目标域名为：",host_name)
            print("目标端口为：",port)  

                    # 简单测试hostname连接是否能够成功
            # ss.sendall(b'\x05\x00\x00\x03'+ handle_data_2[4:])                   # 后面的数据实际上就是相当于复制请求中的域名和port而已，所以此处直接复制即可
            # print("发送的数据为：",b'\x05\x00\x00\x03'+ handle_data_2[4:])         
            # print("真实的data为:",ss.recv(1024))

        elif handle_data_2[3] == 4:                     # 解析IPV6, 暂不提供支持
            IPV6 = handle_data_2[4:20]
            result_list = []
            for i in range(len(IPV6) // 2):
                result_list.append(unichr(ord(IPV6[2 * i]) * 256 + ord(IPV6[2 * i + 1])))
            result = ":".join(result_list)
        
        self.cookie = self.setupSession(target,target_port)
        if not self.cookie:exit('目标不可用，退出')
        ss.sendall(b'\x05\x00\x00'+handle_data_2[3:])           # php服务端连接成功，向客户端发送连接成功的socks响应。接下来应该进入成功的请求
        return True
        



    def socks_4(self,ss):

        status = ss.recv(1)
        if status != b"\x01":exit("协议不是连接，所以退出")
        
        socks_port = ss.recv(2)
        raw_host = ss.recv(4)
        port = socks_port[0]*256 + socks_port[1]

        if raw_host[:3] != b"\x00\x00\x00":     # this is scoks4 just for ip
            print("raw_host is ",raw_host)
            host_ip = ".".join([ str(ip) for ip in raw_host])        # this is host ip          bytes类型来作为可迭代对象的haunted，会直接将其转化为十进制
            # print("host is ",host)                                              # like 114.55.106.242
                                                                               # this is ip to str
            # print("server_ip is",server_ip)                                     # like r7jò
                                                        # utf-8无法将ascii大于126的字符转化为bytes类型.例如chr(242).encode('utf-8')
                                                                # 需要修改为chr(242).encode('latin1')
            # 抛出剩下的连接内容，准备进入响应阶段
            ss.recv(1024)
            target = host_ip

        elif raw_host[:3] == b"\x00\x00\x00":     # this for socks4a just for hostname
            true_host = ss.recv(1024)

            host = true_host[1:-1].decode('utf-8')
            host_ip = socket.gethostbyname(host)

            # here should be setup the sessions
            print("host_ip is ",host_ip)
            target = host
        self.cookie = self.setupSession(target,port)
        if not self.cookie:exit("目标不可连接")
        ss.sendall((chr(0)+chr(90)+chr(int(port) // 256)+chr(int(port) % 256)+"".join([ chr(int(x)) for x in host_ip.split('.')])).encode('latin1'))
        print("that send is",(chr(0)+chr(90)+chr(int(port) // 256)+chr(int(port) % 256)+"".join([ chr(int(x)) for x in host_ip.split('.')])).encode('latin1'))
        # print("socks4a握手成功后的请求为：\n",ss.recv(1024))

        return True

    def handleSocks(self,ss):
        socks_version = ss.recv(1)
        # print(socks_version)      # 此处判断版本
        if socks_version == b"\x04":
            return self.socks_4(ss)
        elif socks_version == b"\x05":
            return self.socks_5(ss)







def askGeorg(ConnectString):
    connect_string = ConnectString
    o = parse.urlparse(connect_string)

    http_host = o.netloc
    http_path = o.path
    try:
        http_port = o.port
    except Exception as identifier:
        pass

        # start the connect
    if o.scheme == "http":
        httpConnect = urllib3.HTTPConnectionPool
    elif o.scheme == "https":
        httpConnect = urllib3.HTTPSConnectionPool
    conn = httpConnect(host = http_host,port = http_port)
    response = conn.request("GET",http_path)
    print(response.status)
    if response.status == 200:
        if response.data.strip().decode("utf-8") == BASICCHECKSTRING:
            return True
    conn.close()
    return False

if __name__ == "__main__":

    try:
        if not askGeorg("http://192.168.2.82/connect.php"):exit("目标不可用")
    except Exception as identifier:
        exit("the target page is not available")
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('127.0.0.1',9998))

    s.listen(4)
    while True:
        ss,addr = s.accept()
        print("远程地址为：",addr)
        # askGeorg('http://192.168.2.82/connect.php')
        
        # the target is 
        
        try:
            if not askGeorg("http://192.168.2.82/connect.php"):exit("目标不可用")
        except Exception as identifier:
            exit("the target page is not available")
        
        Session(ss,"http://192.168.2.82/connect.php").start()
    s.close()
        


