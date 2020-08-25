from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#百度的键盘快捷键操作

web = webdriver.Chrome()

url = 'http://www.baidu.com'
web.get(url)

kw = web.find_element_by_id('kw')

kw.send_keys('Python你好啊')
time.sleep(2)

kw.send_keys(Keys.BACK_SPACE)
time.sleep(2)

kw.send_keys(Keys.SPACE)
kw.send_keys("教程")
time.sleep(2)

kw.send_keys(Keys.CONTROL,'a')
time.sleep(2)

kw.send_keys(Keys.CONTROL,'x')
time.sleep(2)

kw.send_keys(Keys.CONTROL,'v')
time.sleep(2)

btn = web.find_element_by_css_selector('#su')
btn.send_keys(Keys.ENTER)