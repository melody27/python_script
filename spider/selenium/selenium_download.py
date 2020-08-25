from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
import time
#测试上传与下载


options = webdriver.ChromeOptions()

ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0"
options.add_argument("User-Agent="+ua)
prefs = {'download.default_directory':'d:\\python\pachong'}         #设置下载路径
options.add_experimental_option("prefs",prefs)                      #添加设置的下载路径

print("拉起服务器")
web = webdriver.Chrome()
time_start = time.time()

url = "http://pc.weixin.qq.com"
print("开始请求网站")
web.get(url)
time_end = time.time()
print("开启浏览器和请求网站之间的时间为",(time_end-time_start))
web.maximize_window()

down = web.find_element_by_css_selector("body > div.container > div.body > div.textarea > div > a")
down.click()

