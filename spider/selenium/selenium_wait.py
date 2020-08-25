from selenium import webdriver
#显示等待，与隐性等待
    
    
    #显性等待可以手动设置等待条件。而隐形等待只是简单的规定设定时间内网页加载完毕。隐性等待，设置后整个webdriver周期都有用

url = 'http://www.baidu.com/'

web = webdriver.Chrome()
web.implicitly_wait(30)             #设置隐性等待
web.get(url)

kw = web.find_elements_by_id('kw')
kw.send_keys("python")



#设置显性等待
from selenium.webdriver.support.wait import WebDriverWait           #导入显性等待的类
from selenium.webdriver.common.by import By                         #导入快速选择的元素定位方式的类
from selenium.webdriver.support import expected_conditions          #导入显性等待所需要的预期条件的类

Conditions = expected_conditions.visibility_of_element_located((By.ID,"kw"))        #设置显性等待

WebDriverWait(driver=web,timeout=10,poll_frequency=0.5).until(Conditions)
print("执行成功")



