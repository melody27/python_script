import requests

# 测试php客户端的reGeorg脚本。此脚本会使php服务端产生session  （ps. sessions中是有数据的）

url = 'http://192.168.2.82/connect.php'

target = '114.55.106.241'
target_port = '80'

r_s = requests.session()

headers = {
    'X-CMD':'CONNECT',
    'X-TARGET':'{}'.format(target),
    'X-PORT':'{}'.format(target_port)
}

r = r_s.post(url=url,headers=headers)


headers = {
    'Content-Type':'application/octet-stream',
    'Connection':'Keep-Alive',
    'X-CMD':'FORWARD',
    'X-TARGET':'{}'.format(target),
    'X-PORT':'{}'.format(target_port)
}

url = "http://192.168.2.82/connect.php"
out = "GET / HTTP/1.1\r\n"
out += "Host: 114.55.106.241\r\n"
out += "Connection: Close\r\n\r\n"
data = out

r = r_s.post(url=url,headers=headers,data=data)