import gevent.monkey            # 必须在程序的最前面导入gevent的monkey包。否则会出现，超出最大递归数的报错
gevent.monkey.patch_all()
import gevent
import gevent
import socket
from urllib import parse
import urllib3
from threading import Thread
import logging
import time
import sys
import logging

# this is reGeorg Python'client listent to 127.0.0.1:80
# this is available

# constants
BASICCHECKSTRING = "Georg says, 'All seems fine'"
READBUFSIZE = 1024
VER = '\x05'
METHOD = '\x00'

# READ_TIMES = 0        # 统计响应次数和请求次数
# WRITE_TIMES = 0

# logging
LOGSTART = '\x1b[{}m'
LOGEND = '\x1b[0m'
LOG_MELODY = '\x1b[5m'

BLACK, RED, GREEN, YELLOW, BLUE, PERPLE, LITTILE_BLUE, WRITE = range(30,38)
LOGLEVEL = "INFO"

COLOR_LIST = {
    'CRITICAL':RED,
    'ERROR':YELLOW,
    'WARNING':LITTILE_BLUE,
    'INFO':PERPLE,
    "DEBUG":GREEN

}


class FormatLogger(logging.Formatter):
    def __init__(self, msg, use_color=True):
        logging.Formatter.__init__(self, msg)
        self.use_color = use_color

    def format(self, record):
        level_name = record.levelname


        if self.use_color and level_name in COLOR_LIST:
            result = LOGSTART.format(COLOR_LIST[level_name]) + level_name + LOGEND

        if record.name == 'melody':
            result = LOG_MELODY + LOGSTART.format(COLOR_LIST['CRITICAL']) + level_name + LOGEND

        record.levelname = result
        return logging.Formatter.format(self, record)

class MainLogger(logging.Logger):
    
    def __init__(self,name):
        logging.Logger.__init__(self, name, LOGLEVEL)
        format_msg = "[%(levelname)s]  %(message)s"

        msg_format = FormatLogger(format_msg)
        console = logging.StreamHandler()
        console.setFormatter(msg_format)

        self.addHandler(console)
        return

logging.setLoggerClass(MainLogger)

log = logging.getLogger('log')
melody = logging.getLogger('melody')









class SocksProtocolNotImplemented(Exception):
    pass



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
            log.info('[ {}:{} ] shake hands is OK  '.format(self.target,self.target_port))
            # r = gevent.spawn(self.reader)        # 先拉取数据
            # gevent.joinall([gevent.spawn(self.reader)])

            # w = gevent.spawn(self.writer)        # 此处将多线程修改为协程
            gevent.joinall([gevent.spawn(self.reader),gevent.spawn(self.writer)])       # 将原本的多线程修改为协程
            # r.join()
            # w.join()
            
            log.warning('\x1b[42m[ Client Over ]\x1b[0m {}:{} '.format(self.target,self.target_port))

    def reader(self):
        # global READ_TIMES
        conn = urllib3.PoolManager()
        while True:
            try:
                if not self.Psocket: raise SocksProtocolNotImplemented('连接结束，退出')
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
                        log.error('[ {}:{} ] server:{} '.format(self.target,self.target_port,response.getheader('x-error')))
                        break
                        raise SocksProtocolNotImplemented("服务端已经关闭连接，退出")
                        
                else:
                    raise SocksProtocolNotImplemented("服务端状态异常，响应状态码不为200，退出")   
                    break    
                if len(data) == 0:
                    time.sleep(0.1)
                    continue
                else:
                    melody.critical(' [ {}:{}] recv \x1b[5m\x1b[33m<<<\x1b[0m {}'.format(self.target,self.target_port,len(data)))
                self.Psocket.sendall(data)
                # READ_TIMES += 1       
                # print("响应次数为：",READ_TIMES)
            except Exception as identifier:
                print(identifier)


    def writer(self):
        # global WRITE_TIMES
        log.error('[ {}:{} ] sending data ... ... '.format(self.target,self.target_port))
        global READBUFSIZE
        conn = urllib3.PoolManager()
        while True:
            data = self.Psocket.recv(READBUFSIZE)
            if not data:
                log.critical('[ {}:{} ] no data need to send to target '.format(self.target,self.target_port))
                break
            # WRITE_TIMES += 1
            # print("写入次数为",WRITE_TIMES)
            headers = {"X-CMD":"FORWARD","Cookie":self.cookie,"Content-type":"application/octet-stream","Connection":"Keep-Alive"}
            response = conn.urlopen("POST",self.connect_string,headers=headers,body=data)
            melody.critical(' [ {}:{}] send \x1b[5m\x1b[33m>>>\x1b[0m {}'.format(self.target,self.target_port,len(data)))
            # print("正在写入数据中：",data)
            if response.status == 200:
                status = response.getheader("x-status")
                if status == "OK":
                    if response.getheader("set-sookie") is not None:
                        self.cookie = response.getheader("set-cookie")
                else:
                    log.error('[ {}:{} ] server:{} '.format(self.target,self.target_port,response.getheader('x-error')))
                    break
            else:
                log.error('[ {}:{} ] remote server status_code is not 200 '.format(self.target,self.target_port))
                break
        self.closeSession()
        try:
            self.Psocket.close()
        except:
            log.error('[ {}:{} ] the socket is error  '.format(self.target,self.target_port))
        

        # 握手并且在服务端建立session
    def setupSession(self,target,target_port):
        headers = {"X-CMD":"CONNECT","X-TARGET":target,"X-PORT":str(target_port)}
        self.target = target
        self.target_port = target_port
        cookie = None
        conn = self.http_scheme(host=self.http_host,port=self.http_port)

        response = conn.urlopen("POST",self.connect_string, headers=headers)
        log.error('[ {}:{} ] setuping the remote sessions ... ...  '.format(self.target,self.target_port))
        if response.status == 200:
            cookie = response.getheader("set-cookie")
            log.error('[ {}:{} ] the cookie is   '.format(self.target,self.target_port,cookie))
            if response.getheader("X-ERROR"):
                log.error('[ {}:{} ] remote server is send X-ERROR like:{} '.format(self.target,self.target_port,response.getheaders("X-ERROR")))
            log.error('[ {}:{} ] the setupsession() send request headers is {}  '.format(self.target,self.target_port,headers))
        else:
            raise SocksProtocolNotImplemented('与目标服务器建立连接失败')
        conn.close()
        return cookie

    def closeSession(self):
        headers = {"X-CMD":"DISCONNECT","Cookie":self.cookie}
        conn = self.http_scheme(host=self.http_host,port=self.http_port)
        r = conn.urlopen("POST",self.connect_string,headers=headers)
        if r.status == 200:
            log.critical('[ {}:{} ] send the closeSession '.format(self.target,self.target_port))
        conn.close()



    def socks_5(self,ss):
        log.info('start the socks5 shake hands')
        handle_data_1 = ss.recv(1024)     # 接受剩余的字节
        ss.sendall(b'\x05\x00')         # 响应客户端使用免验证登录
        handle_data_2 = ss.recv(1024)
        log.critical('recv the socks5 shake handls data like {}'.format(handle_data_2))
        if handle_data_2[0] != 5:exit('协议错误退出')
        if handle_data_2[1] != 1:print("不支持的方式,bind or udp，socks不支持. 退出")
        if handle_data_2[3] == 1:                       # 解析IP,           此处handle_data_2[3] 实际上为客户端确定的ipv4,域名，ipv6支持
            ip = ".".join( str(ord(x)) for x in handle_data_2[4:8].decode('latin1'))
            target = ip
            port = handle_data_2[-2] *256 + handle_data_2[-1]       # 优化一下
            target_port = port 
            
            log.error('the target is {}:{}'.format(ip,port))
                    # 简单测试ip连接是否能够成功
            # ss.sendall(b'\x05\x00\x00\x01'+ handle_data_2[4:])                  # 后面的数据实际上就是相当于复制请求中的域名和port而已，所以此处直接复制即可
            # print("发送的数据为      ：",b'\x05\x00\x00\x01'+ handle_data_2[4:]) 
            # print("真实的data为:",ss.recv(1024))
        elif handle_data_2[3] == 3:                     # 解析域名
            host_name = handle_data_2[5:handle_data_2[4]+5].decode('utf-8')
            target = host_name
            port = handle_data_2[-2] *256 + handle_data_2[-1]       # 优化一下
            target_port = port
            log.error('the target is {}:{}'.format(host_name,port))
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
        if not self.cookie:
            ss.sendall(b'\x05\x01\x00'+handle_data_2[3:])
            raise SocksProtocolNotImplemented('连接不可用，退出')
        else:
            ss.sendall(b'\x05\x00\x00'+handle_data_2[3:])           # php服务端连接成功，向客户端发送连接成功的socks响应。接下来应该进入成功的请求
            return True
        return False
        



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
        else :
            raise SocksProtocolNotImplemented('connect is abnormal')







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
    log.info('target is available')
    if response.status == 200:
        if response.data.strip().decode("utf-8") == BASICCHECKSTRING:
            return True
    conn.close()
    return False

if __name__ == "__main__":


    # server_url = 'http://192.168.2.82/connect.php'
    server_url = 'http://192.168.2.82/testconnect.php'

    try:
        if not askGeorg(server_url):exit("目标不可用")
    except Exception as identifier:
        exit("the target page is not available")
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('127.0.0.1',9998))

    s.listen(4)
    while True:
        ss,addr = s.accept()
        log.info('\n\n\n\x1b[42m[ New Client ]\x1b[0m from {}'.format(str(addr[0])+':'+str(addr[1])))
        
        try:
            if not askGeorg(server_url):exit("目标不可用")
        except Exception as identifier:
            exit("the target page is not available")
        
        Session(ss,server_url).start()
    s.close()
        


