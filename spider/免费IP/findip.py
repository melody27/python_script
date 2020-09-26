# -*-coding:utf-8 -*-
import io
import sys
#改变标准输出的默认编码
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

from bs4 import BeautifulSoup


# 爬取网上的免费IP，  后续通过testip.py脚本进行测试IP是否可用

import requests
import re
import time


# 获取免费IP
url = "https://www.kuaidaili.com/free/intr/{}/"
target_url = "http://www.melodyspace.cn"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",

}
    
def spider_the_ip(pages):
    for x in range(1,pages):
        
        time.sleep(2)
        print("第{}页".format(str(x)))
        x = str(x)
        r = requests.get(url=url.format(x),headers=headers)
        html_content = BeautifulSoup(r.text,"html.parser")
        # print(r.text,url.format(x))
        with open("D:\\cpan\\桌面\\test\\hwtest\\ip\\iptxt.txt",'a+',encoding="utf-8") as f:
            for yy in range(1,16):
                raw_ip = html_content.select('#list > table > tbody > tr:nth-child({}) > td:nth-child(1)'.format(str(yy)))[0]
                raw_port = html_content.select('#list > table > tbody > tr:nth-child({}) > td:nth-child(2)'.format(str(yy)))[0]
                print("raw_ip:{}  raw_port:{}".format(raw_ip,raw_port))
                ip = re.findall(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}",str(raw_ip))
                port = re.findall(r"[0-9]{2,5}",str(raw_port))
                print(ip)
                print("{}:{}".format(ip[0],port[0]))
                f.write("{}:{}\r".format(ip[0],port[0]))

if __name__ == "__main__":
    spider_the_ip(999)