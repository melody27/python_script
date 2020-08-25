from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
#文件上传，（未完成）

web = webdriver.Chrome()

url = "http://chuantu.biz/"
options = webdriver.ChromeOptions()

ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0"
options.add_argument("User-Agent="+ua)


web.get(url)

# web.find_element_by_css_selector("body > div > div.welcome > div > div.next").click()

#移动鼠标触发ajax
# aa = web.find_element_by_css_selector("body > div > div.cow-transfer-entry > div > div.add-files-area > div.add-files.button > span:nth-child(3)")
# ActionChains(web).move_to_element(aa).perform()
# web.find_element_by_css_selector("body > div > div.cow-transfer-entry > div > div.add-files-area > div.add-folder.button > img").click()
time.sleep(2)

web.find_element_by_css_selector("#latest-post > form > input[type=file]:nth-child(2)").send_keys("D:\\test.txt")
# web.find_element_by_css_selector("body > div > input:nth-child(5)").send_keys("D:\cpan\桌面\ssr\templates\cgi-style.css")
# web.find_element_by_css_selector("body > div > input:nth-child(6)").send_keys("D:\cpan\桌面\ssr\templates\cgi-style.css")


