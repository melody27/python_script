from selenium import webdriver
import time
#对窗口进行操作，新建，切换

url = 'http://www.baidu.com/'

web = webdriver.Chrome()                #实例化浏览器

web.get(url)
print("初次请求的百度的title："+web.title)
print("初次请求的百度的url"+web.current_url)


open_new_lab = 'window.open("http://www.bilibili.com/");'
web.execute_script(open_new_lab)            #通过execute_script函数执行js脚本。新建窗口
time.sleep(2)
print("--------第二次请求---------")
print("新建了窗口后的title："+web.title)
print("新建了窗口后的url"+web.current_url)


all_windows = web.window_handles            #获取所有的窗口
while True:
    web.switch_to.window(all_windows[0])        #切换到第一个窗口
    print("---------------切换窗口后的------------------")
    print("切换窗口后新的url："+web.current_url)
    time.sleep(2)
    web.switch_to.window(all_windows[1])        #切换到第二个窗口
    print("第二次切换了窗口后的url："+web.current_url)