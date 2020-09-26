# -*-coding:utf-8 -*-
import io
import sys
#改变标准输出的默认编码
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')


# 测试网上的免费IP是否可用
import requests
import base64
import os
from urllib import request,error

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
}

url = "http://www.baidu.com/"
def test_proxy(ip):

    proxies = {
        # "http":"125.108.122.154:9000"
        # "http":"219.239.142.253:3128"
        "http":"{}".format(ip)
    }

    url = "http://114.55.106.242:8080/index.php/"
    r = requests.get(url,proxies=proxies,timeout=5)
    print(r.text)




if __name__ == "__main__":
    # test_proxy("220.178.227.48","4268")
    # print(requests.get("http://www.baidu.com"))
    test_proxy("223.82.106.253:3128")