from selenium import webdriver
import json
import time


option = webdriver.ChromeOptions()
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0"
option.add_argument("User-Agent="+ua)

url = "https://www.youdao.com/"
url2 = "https://www.baidu.com/"
web = webdriver.Chrome(options=option)

web.get(url)

print("输出获取到的所有cookie："+str(web.get_cookies()))

time.sleep(2)
x = {'name': 'jack',"age":18}
# for y in x:
web.add_cookie({'name':'name','value':'jack'})

print("获取添加后的所有cookie："+str(web.get_cookies()))

print("获取单个cookie，name的值为："+str(web.get_cookie('name')))
#此处获取单个的cookie输出的值为：{'domain': 'www.youdao.com', 'httpOnly': False, 'name': 'name', 'path': '/', 'secure': True, 'value': 'jack'}



web.delete_cookie('age')
print("删除单个cookie："+str(web.get_cookies()))

# print("删除所有cookie：")

web.delete_all_cookies()

print("输出所有cookie："+str(web.get_cookies()))