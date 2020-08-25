from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
#设置chrome的option。请求参数:lang和User-Agent

option = Options()          #实例化设置类

option.add_argument('lang=zh_CN.UTF-8')         #为设置里添加lang

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0'
option.add_argument('User-Agent='+user_agent)       #为设置里添加user-agent

option.add_argument('--headless')           #设置为不可视化浏览器。


web = webdriver.Chrome(options=option)      #实例化浏览器对象。(加上设置)
web.maximize_window()

url = 'http://www.baidu.com'
web.get(url)

tt = web.find_element_by_css_selector('#kw')
# print("祝你生日快乐")
print(web.title)                #获取浏览的当前页面的title

print(web.page_source)          #获取浏览器当前页面的源码