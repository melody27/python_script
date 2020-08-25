import requests
import bs4
# url='http://www.baidu.com'
# respone=requests.get(url)#这里请求百度首页

# print(respone.status_code)
# print(respone.content)

def request(url="", headers=""):
    print("url: " + url)
    print("headers: " + headers)

request(headers="headers")