#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import argparse
import urllib3
from threading import Thread
from urlparse import urlparse
from socket import *
from threading import Thread
from time import sleep

# Constants
SOCKTIMEOUT = 5
RESENDTIMEOUT = 300
VER = "\x05"
METHOD = "\x00"         # socks5的方法为无认证方式
SUCCESS = "\x00"
SOCKFAIL = "\x01"
NETWORKFAIL = "\x02"
HOSTFAIL = "\x04"
REFUSED = "\x05"
TTLEXPIRED = "\x06"
UNSUPPORTCMD = "\x07"
ADDRTYPEUNSPPORT = "\x08"
UNASSIGNED = "\x09"

BASICCHECKSTRING = "Georg says, 'All seems fine'"

# Globals
READBUFSIZE = 1024

# Logging
RESET_SEQ = "\033[0m"
COLOR_SEQ = "\033[1;%dm"
BOLD_SEQ = "\033[1m"

BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

LEVEL = {"INFO": logging.INFO, "DEBUG": logging.DEBUG, }

logLevel = "INFO"

COLORS = {
    'WARNING': YELLOW,
    'INFO': WHITE,
    'DEBUG': BLUE,
    'CRITICAL': YELLOW,
    'ERROR': RED,
    'RED': RED,
    'GREEN': GREEN,
    'YELLOW': YELLOW,
    'BLUE': BLUE,
    'MAGENTA': MAGENTA,
    'CYAN': CYAN,
    'WHITE': WHITE,
}


def formatter_message(message, use_color=True):
    if use_color:
        message = message.replace("$RESET", RESET_SEQ).replace("$BOLD", BOLD_SEQ)
    else:
        message = message.replace("$RESET", "").replace("$BOLD", "")
    return message


class ColoredFormatter(logging.Formatter):
    def __init__(self, msg, use_color=True):
        logging.Formatter.__init__(self, msg)
        self.use_color = use_color

    def format(self, record):
        levelname = record.levelname
        if self.use_color and levelname in COLORS:
            levelname_color = COLOR_SEQ % (30 + COLORS[levelname]) + levelname + RESET_SEQ
            record.levelname = levelname_color
        return logging.Formatter.format(self, record)


class ColoredLogger(logging.Logger):

    def __init__(self, name):
        FORMAT = "[$BOLD%(levelname)-18s$RESET]  %(message)s"
        COLOR_FORMAT = formatter_message(FORMAT, True)
        logging.Logger.__init__(self, name, logLevel)
        if (name == "transfer"):
            COLOR_FORMAT = "\x1b[80D\x1b[1A\x1b[K%s" % COLOR_FORMAT
        color_formatter = ColoredFormatter(COLOR_FORMAT)

        console = logging.StreamHandler()
        console.setFormatter(color_formatter)

        self.addHandler(console)
        return


logging.setLoggerClass(ColoredLogger)
log = logging.getLogger(__name__)
transferLog = logging.getLogger("transfer")


class SocksCmdNotImplemented(Exception):
    pass


class SocksProtocolNotImplemented(Exception):
    pass


class RemoteConnectionFailed(Exception):
    pass


class session(Thread):
    def __init__(self, pSocket, connectString):         # 进行初始化操作
        Thread.__init__(self)                   
        self.pSocket = pSocket                      # 定义要进行使用的socket对象
        self.connectString = connectString          # 获取到了目标url后，对url进行切分赋值。将url的每个部分分别赋值给self的属性
        o = urlparse(connectString)
        try:
            self.httpPort = o.port
        except:
            if o.scheme == "https":
                self.httpPort = 443
            else:
                self.httpPort = 80
        self.httpScheme = o.scheme
        self.httpHost = o.netloc.split(":")[0]      # 如果是有端口的情况的话，通过:来做切分，获取其左边部分
        self.httpPath = o.path
        self.cookie = None
        if o.scheme == "http":
            self.httpScheme = urllib3.HTTPConnectionPool        # 此处定义使用的协议，并将其赋值给self的httpScheme属性
        else:
            self.httpScheme = urllib3.HTTPSConnectionPool

    def parseSocks5(self, sock):
        log.debug("SocksVersion5 detected")
        nmethods, methods = (sock.recv(1), sock.recv(1))
        sock.sendall(VER + METHOD)
        ver = sock.recv(1)
        if ver == "\x02":  # this is a hack for proxychains     正常的话第一个字节应该是\x05
            ver, cmd, rsv, atyp = (sock.recv(1), sock.recv(1), sock.recv(1), sock.recv(1))
        else:
            cmd, rsv, atyp = (sock.recv(1), sock.recv(1), sock.recv(1))
        target = None
        targetPort = None
        if atyp == "\x01":  # IPv4
            # Reading 6 bytes for the IP and Port
            target = sock.recv(4)
            targetPort = sock.recv(2)
            target = "." .join([str(ord(i)) for i in target])
        elif atyp == "\x03":  # Hostname
            targetLen = ord(sock.recv(1))  # hostname length (1 byte)
            target = sock.recv(targetLen)
            targetPort = sock.recv(2)
            target = "".join([unichr(ord(i)) for i in target])
        elif atyp == "\x04":  # IPv6
            target = sock.recv(16)
            targetPort = sock.recv(2)
            tmp_addr = []
            for i in xrange(len(target) / 2):
                tmp_addr.append(unichr(ord(target[2 * i]) * 256 + ord(target[2 * i + 1])))
            target = ":".join(tmp_addr)
        targetPort = ord(targetPort[0]) * 256 + ord(targetPort[1])
        if cmd == "\x02":  # BIND
            raise SocksCmdNotImplemented("Socks5 - BIND not implemented")
        elif cmd == "\x03":  # UDP
            raise SocksCmdNotImplemented("Socks5 - UDP not implemented")
        elif cmd == "\x01":  # CONNECT
            serverIp = target
            try:
                serverIp = gethostbyname(target)
            except:
                log.error("oeps")
            serverIp = "".join([chr(int(i)) for i in serverIp.split(".")])
            self.cookie = self.setupRemoteSession(target, targetPort)
            if self.cookie:
                sock.sendall(VER + SUCCESS + "\x00" + "\x01" + serverIp + chr(targetPort / 256) + chr(targetPort % 256))
                return True
            else:
                sock.sendall(VER + REFUSED + "\x00" + "\x01" + serverIp + chr(targetPort / 256) + chr(targetPort % 256))
                raise RemoteConnectionFailed("[%s:%d] Remote failed" % (target, targetPort))

        raise SocksCmdNotImplemented("Socks5 - Unknown CMD")

    def parseSocks4(self, sock):                      
        log.debug("SocksVersion4 detected")
        cmd = sock.recv(1)
        if cmd == "\x01":  # Connect
            targetPort = sock.recv(2)               # 接受两个代表port的字节
            targetPort = ord(targetPort[0]) * 256 + ord(targetPort[1])
            target = sock.recv(4)                   # 获取代表IP的四个字节
            sock.recv(1)                            # 代表用户ID的一个字节
            target = ".".join([str(ord(i)) for i in target])    # 将字节转化为十进制的字符串
            serverIp = target                      
            try:
                serverIp = gethostbyname(target)    # 获取主机名字，如果传入的是IP的话，那么这一步就是多余的。
            except:                                     # 实际上如果是socks4a协议的话,此处可能会有问题
                log.error("oeps")
            serverIp = "".join([chr(int(i)) for i in serverIp.split(".")])  # 将获取到的真实主机名，转化拼接为字符串
            self.cookie = self.setupRemoteSession(target, targetPort)       # 建立真实的连接请求，并且返回其cookie,实际此处为域名
            if self.cookie:                         # 
                sock.sendall(chr(0) + chr(90) + chr(targetPort / 256) + chr(targetPort % 256)+ serverIp )   # 此处的chr(0)是因为\x00不可打印
                return True                                 # 向本地的客户端发送响应包，返回True连接建立成功
            else:
                sock.sendall("\x00" + "\x91" + serverIp + chr(targetPort / 256) + chr(targetPort % 256))
                raise RemoteConnectionFailed("Remote connection failed")
        else:
            raise SocksProtocolNotImplemented("Socks4 - Command [%d] Not implemented" % ord(cmd))

    def handleSocks(self, sock):
        # This is where we setup the socks connection
        ver = sock.recv(1)
        if ver == "\x05":                                   # 如果传递的第一个字节为\x05，那么说明使用的是socket5:b'\x05\x01\x00'
            return self.parseSocks5(sock)
        elif ver == "\x04":                                 # 如果传递的第一个字节为\x04，那么使用的socket4:b'\x04\x01\x00P\x00\x00\x00\x01\x00ww.baidu.com\x00'
            return self.parseSocks4(sock)

    def setupRemoteSession(self, target, port):
        headers = {"X-CMD": "CONNECT", "X-TARGET": target, "X-PORT": port}
        self.target = target
        self.port = port
        cookie = None
        conn = self.httpScheme(host=self.httpHost, port=self.httpPort)  # 此方法为初始化中定义的httpconnectpool对象，实际作用为打开urlopen，产生连接
        # response = conn.request("POST", self.httpPath, params, headers)
        response = conn.urlopen('POST', self.connectString + "?cmd=connect&target=%s&port=%d" % (target, port), headers=headers, body="")
        if response.status == 200:                      # 获取目标页面的http连接并且获取其状态码并进行判断，X-CMD字段值为CONNECT
            status = response.getheader("x-status")     # getheader方法作用为获取响应头的目标字段
            if status == "OK":
                cookie = response.getheader("set-cookie")   # 获取cookie,这个cookie是socks连接服务端自定义的socks协议代理的cookie，而不是百度的cookie
                log.info("[%s:%d] HTTP [200]: cookie [%s]" % (self.target, self.port, cookie))
            else:
                if response.getheader("X-ERROR") is not None:
                    log.error(response.getheader("X-ERROR"))
        else:
            log.error("[%s:%d] HTTP [%d]: [%s]" % (self.target, self.port, response.status, response.getheader("X-ERROR")))
            log.error("[%s:%d] RemoteError: %s" % (self.target, self.port, response.data))
        conn.close()
        return cookie               # 实际返回的是其服务端定义的cookie，实际为session。暂时未找到cookie的作用是什么

    def closeRemoteSession(self):           # 实际上的关闭连接。就相当于
        headers = {"X-CMD": "DISCONNECT", "Cookie": self.cookie}
        params = ""
        conn = self.httpScheme(host=self.httpHost, port=self.httpPort)
        response = conn.request("POST", self.httpPath + "?cmd=disconnect", params, headers)
        if response.status == 200:
            log.info("[%s:%d] Connection Terminated" % (self.target, self.port))
        conn.close()

    def reader(self):
        print("into the reader")
        conn = urllib3.PoolManager()
        while True:
            try:
                if not self.pSocket:            # reader 终止的条件为 pSocket已经停止
                    break
                data = ""                               # 此处的cookie实则为PHPSESSION
                headers = {"X-CMD": "READ", "Cookie": self.cookie, "Connection": "Keep-Alive"}
                response = conn.urlopen('POST', self.connectString + "?cmd=read", headers=headers, body="")
                data = None
                if response.status == 200:
                    status = response.getheader("x-status")
                    if status == "OK":
                        if response.getheader("set-cookie") is not None:
                            cookie = response.getheader("set-cookie")
                        data = response.data
                        # Yes I know this is horrible, but its a quick fix to issues with tomcat 5.x bugs that have been reported, will find a propper fix laters
                        try:
                            if response.getheader("server").find("Apache-Coyote/1.1") > 0:
                                data = data[:len(data) - 1]
                        except:
                            pass
                        if data is None:            # if the socket is not close so data shounld be "" instead of None
                            data = ""
                    else:
                        data = None
                        log.error("[%s:%d] HTTP [%d]: Status: [%s]: Message [%s] Shutting down" % (self.target, self.port, response.status, status, response.getheader("X-ERROR")))
                else:
                    log.error("[%s:%d] HTTP [%d]: Shutting down" % (self.target, self.port, response.status))
                if data is None:
                    # Remote socket closed          # if X-STATUS: is FAIL   so this socket will be close. else it's will be ok
                    break
                if len(data) == 0:                  # if the socket is not close. so that shoud be connect next for sleep(0.1)
                    sleep(0.1)
                    continue
                transferLog.info("[%s:%d] <<<< [%d]" % (self.target, self.port, len(data)))
                self.pSocket.send(data)
            except Exception, ex:
                raise ex
        print("getout the reader")
        self.closeRemoteSession()                    # when the data is sendall. so next will be close session  # 在手动结束前并不会结束此处
        log.debug("[%s:%d] Closing localsocket" % (self.target, self.port))
        try:
            self.pSocket.close()                    # close the socket. the pSocket is the socket object 
        except:
            log.debug("[%s:%d] Localsocket already closed" % (self.target, self.port))

    def writer(self):
        global READBUFSIZE
        conn = urllib3.PoolManager()
        while True:
            try:
                self.pSocket.settimeout(1)
                data = self.pSocket.recv(READBUFSIZE)
                if not data:                    # writer 终止的条件为：recv的data为空
                    break                           # 实际上哪怕客户端发送ss.sendall(''.encode('utf-8'))，服务端也并不会接收到null数据。也就是说此处的退出条件实际上是终止为止
                headers = {"X-CMD": "FORWARD", "Cookie": self.cookie, "Content-Type": "application/octet-stream", "Connection": "Keep-Alive"}
                response = conn.urlopen('POST', self.connectString + "?cmd=forward", headers=headers, body=data)
                if response.status == 200:
                    status = response.getheader("x-status")
                    if status == "OK":
                        if response.getheader("set-cookie") is not None:
                            self.cookie = response.getheader("set-cookie")
                    else:
                        log.error("[%s:%d] HTTP [%d]: Status: [%s]: Message [%s] Shutting down" % (self.target, self.port, response.status, status, response.getheader("x-error")))
                        break
                else:
                    log.error("[%s:%d] HTTP [%d]: Shutting down" % (self.target, self.port, response.status))
                    break
                transferLog.info("[%s:%d] >>>> [%d]" % (self.target, self.port, len(data)))
            except timeout:
                continue
            except Exception, ex:
                raise ex
                break
        self.closeRemoteSession()       # 此处貌似不退出的话，实际上并不会执行到此处
        log.debug("Closing localsocket")
        try:
            self.pSocket.close()
        except:
            log.debug("Localsocket already closed")

    def run(self):                                      
        try:                                    # session作为thread类的入口函数
            if self.handleSocks(self.pSocket):      # 测试连接状态，如果是socks4的话，那么会往代理服务器发送http包，测试连接状态。
                log.debug("Staring reader")             # 如果连接状态OK的话，那么会向客户端发送握手正确的socks响应包，然后此处会返回true
                r = Thread(target=self.reader, args=())     
                r.start()
                log.debug("Staring writer")
                w = Thread(target=self.writer, args=())
                w.start()
                r.join()
                w.join()
        except SocksCmdNotImplemented, si:
            log.error(si.message)
            self.pSocket.close()
        except SocksProtocolNotImplemented, spi:
            log.error(spi.message)
            self.pSocket.close()
        except Exception, e:
            log.error(e.message)
            self.closeRemoteSession()
            self.pSocket.close()


def askGeorg(connectString):					# 测试连接是否可用
    connectString = connectString               # 此处的测试连接不是限制代理的 只能是http协议。
    o = urlparse(connectString)                 # 而是测试目标代理是否可用，也就是确认服务端是否存在
    try:                                        # 此处会向目标代理的php页面发送请求，并且确认是否返回了  Georg says, 'All seems fine'
        httpPort = o.port
    except:
        if o.scheme == "https":
            httpPort = 443
        else:
            httpPort = 80
    httpScheme = o.scheme
    httpHost = o.netloc.split(":")[0]
    httpPath = o.path
    if o.scheme == "http":
        httpScheme = urllib3.HTTPConnectionPool
    else:
        httpScheme = urllib3.HTTPSConnectionPool

    conn = httpScheme(host=httpHost, port=httpPort)
    response = conn.request("GET", httpPath)
    if response.status == 200:
        if BASICCHECKSTRING == response.data.strip():
            log.info(BASICCHECKSTRING)
            return True
    conn.close()
    return False

if __name__ == '__main__':
    print """\033[1m
    \033[1;33m
                     _____
  _____   ______  __|___  |__  ______  _____  _____   ______
 |     | |   ___||   ___|    ||   ___|/     \|     | |   ___|
 |     \ |   ___||   |  |    ||   ___||     ||     \ |   |  |
 |__|\__\|______||______|  __||______|\_____/|__|\__\|______|
                    |_____|
                    ... every office needs a tool like Georg

  willem@sensepost.com / @_w_m__
  sam@sensepost.com / @trowalts
  etienne@sensepost.com / @kamp_staaldraad
  \033[0m
   """
    log.setLevel(logging.DEBUG)
    parser = argparse.ArgumentParser(description='Socks server for reGeorg HTTP(s) tunneller')
    parser.add_argument("-l", "--listen-on", metavar="", help="The default listening address", default="127.0.0.1")
    parser.add_argument("-p", "--listen-port", metavar="", help="The default listening port", type=int, default="8888")
    parser.add_argument("-r", "--read-buff", metavar="", help="Local read buffer, max data to be sent per POST", type=int, default="1024")
    parser.add_argument("-u", "--url", metavar="", required=True, help="The url containing the tunnel script")
    parser.add_argument("-v", "--verbose", metavar="", help="Verbose output[INFO|DEBUG]", default="INFO")
    args = parser.parse_args()
    if (args.verbose in LEVEL):
        log.setLevel(LEVEL[args.verbose])
        log.info("Log Level set to [%s]" % args.verbose)

    log.info("Starting socks server [%s:%d], tunnel at [%s]" % (args.listen_on, args.listen_port, args.url))
    log.info("Checking if Georg is ready")
    if not askGeorg(args.url):			# 测试目标连接是否可用
        log.info("Georg is not ready, please check url")
        exit()
    READBUFSIZE = args.read_buff
    servSock = socket(AF_INET, SOCK_STREAM)
    servSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) #SO_REUSEADDR 标志告诉内核将处于 TIME_WAIT 状态的本地套接字重新使用，而不必等到固有的超时到期。
    servSock.bind((args.listen_on, args.listen_port))
    servSock.listen(1000)                            # 指定连接的线程
    while True:
        try:
            sock, addr_info = servSock.accept()
            sock.settimeout(SOCKTIMEOUT)
            log.debug("Incomming connection")
            session(sock, args.url).start()         # 使用session类进行流量的转发。第一个参数为accept返回的sock对象，第二个参数为webshell所在的url
        except KeyboardInterrupt, ex:
            break
        except Exception, e:
            log.error(e)
    servSock.close()
