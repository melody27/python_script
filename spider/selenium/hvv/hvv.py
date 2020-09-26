from selenium import webdriver
import time
import hashlib
import re
from selenium.webdriver import ActionChains


# 此脚本为hw过程中的D-sensor监控脚本

def handle_message(web):
    # web.get("http://www.baidu.com")
    message_box = web.find_element_by_css_selector("body > div:nth-child(8) > div > span > div > div > div > div.ant-notification-notice-description > div.f1tslxfd").text()
    attack_message = exteact_message(message_box)
    attack_ip = attack_message['attack_ip']

    # 此处应该点击弹出框的关闭选项

def exteact_message(data):
    result = {}
    message = data
    ip_list = re.findall(r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}',message)
    honeypot_name = re.findall(r'ag_\w+',message)[0]
    attack_message = re.findall(r"(?<=上的).+",message)[0]
    attack_ip = ''
    honeypot_ip = ''
    for x in ip_list:
        if x.startswith("172.18") or x.startswith("10.79"):
            honeypot_ip = x
        else:
            attack_ip = x
    result['honeypot_name'] = honeypot_name
    result['attack_message'] = attack_message
    result['attack_ip'] = attack_ip
    result['honeypot_ip'] = honeypot_ip
    
    return attack_ip



# 此函数可以用来设置时间，限制。设置警报页面的时间限制
def monitor_date(web):  # 根据时间选择

    web.get("https://10.79.21.110/alarm-center")
    time.sleep(3)
    time.sleep(2)
    web.find_element_by_css_selector("#main-wrapper > main > div > div > div > div > div:nth-child(1) > div > div:nth-child(2) > button").click()
    time.sleep(2)
    web.find_element_by_css_selector('body > div:nth-child(7) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-body > div > div > button').click()
    time.sleep(2)
    xuanxiang = web.find_element_by_css_selector('body > div:nth-child(7) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-body > div > div.f1luoau5 > div:nth-child(1) > div > div > div > div')
 

    action = ActionChains(web)
    action.move_to_element(xuanxiang).click()
    time.sleep(1)
    action.move_to_element_with_offset(xuanxiang,40,162).click().perform()
    # action.perform()
    web.find_element_by_css_selector("body > div:nth-child(7) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-body > div > div.f1luoau5 > div.fiw0lep > div > div > span > span > input:nth-child(1)").click()
    time.sleep(2)
    web.find_element_by_css_selector("div > div > div > div > div > div.ant-calendar-date-panel > div.ant-calendar-range-part.ant-calendar-range-left > div:nth-child(2) > div.ant-calendar-body > table > tbody > tr.ant-calendar-current-week > td:nth-child(6)").click()
    time.sleep(2)
    web.find_element_by_css_selector("body > div:nth-child(8) > div > div > div > div > div.ant-calendar-date-panel > div.ant-calendar-range-part.ant-calendar-range-left > div:nth-child(2) > div.ant-calendar-body > table > tbody > tr:nth-child(5) > td.ant-calendar-cell.ant-calendar-in-range-cell.ant-calendar-last-day-of-month").click()

    time.sleep(2)
    web.find_element_by_css_selector("body > div:nth-child(8) > div > div > div > div > div.ant-calendar-footer.ant-calendar-range-bottom.ant-calendar-footer-show-ok > div > a.ant-calendar-ok-btn").click()
    web.find_element_by_css_selector("body > div:nth-child(7) > div > div.ant-modal-wrap.ant-modal-centered > div > div.ant-modal-content > div.ant-modal-footer > button.ant-btn.fzr3hld.f1iny9pd").click()
    time.sleep(3)
    


# 过滤攻击流量页面的数据
def filter_data(web):
    result = {}
    place = web.find_element_by_css_selector("#main-wrapper > main > div > div > div > div > div:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div > span:nth-child(2)").text
    attack_time = web.find_element_by_css_selector("#main-wrapper > main > div > div > div > div > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div > span:nth-child(2)").text
    honeypot_id = web.find_element_by_css_selector("#main-wrapper > main > div > div > div > div > div:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div > span:nth-child(2) > a").text
    honeypot_name = web.find_element_by_css_selector("#main-wrapper > main > div > div > div > div > div:nth-child(2) > div:nth-child(4) > div:nth-child(2) > div > span:nth-child(2)").text
    result['place'] = place
    result['attack_time'] = attack_time
    result['honeypot_id'] = honeypot_id
    result['honeypot_name'] = honeypot_name
    return result



# 每一个tr的classname为ant-table-row ant-table-row-level-0
# 第一个的css选择器为：#main-wrapper > main > div > div > div > div > div.fadfao3 > div > div > div > div > div > div > table > tbody > tr:nth-child(1) > td:nth-child(8) > button:nth-child(1)





url = "https://10.79.21.110/alarm-center"

web = webdriver.Chrome()
web.get(url)

if (web.find_element_by_css_selector("#details-button").is_displayed()):
    web.find_element_by_css_selector("#details-button").click()
    time.sleep(1)
    web.find_element_by_css_selector("#proceed-link").click()

if (web.find_element_by_css_selector("#root > div > div > div.ant-spin-nested-loading > div > div.ant-tabs.ant-tabs-top.f1e7n2px.ant-tabs-line > div.ant-tabs-bar.ant-tabs-top-bar > div > div > div > div > div:nth-child(1) > div.ant-tabs-tab-active.ant-tabs-tab").is_displayed()):
    print("进入",web.find_element_by_css_selector("#root > div > div > div.ant-spin-nested-loading > div > div.ant-tabs.ant-tabs-top.f1e7n2px.ant-tabs-line > div.ant-tabs-bar.ant-tabs-top-bar > div > div > div > div > div:nth-child(1) > div.ant-tabs-tab-active.ant-tabs-tab").text)
    user = str(input("输入你的登录用户名"))
    passwd = str(input("输入你登录的用户名"))
    web.find_element_by_css_selector("#root > div > div > div.ant-spin-nested-loading > div > div.ant-tabs.ant-tabs-top.f1e7n2px.ant-tabs-line > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > form > div:nth-child(1) > div > div > span > input").send_keys(user)
    web.find_element_by_css_selector("#root > div > div > div.ant-spin-nested-loading > div > div.ant-tabs.ant-tabs-top.f1e7n2px.ant-tabs-line > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > form > div:nth-child(2) > div > div > span > span > input").send_keys(passwd)
    web.find_element_by_css_selector("#root > div > div > div.ant-spin-nested-loading > div > div.ant-tabs.ant-tabs-top.f1e7n2px.ant-tabs-line > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > form > button").click()
    print("登录成功")
    time.sleep(2)
    web.get('https://10.79.21.110/alarm-center')


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

monitor_date(web)
web.get(url)
time.sleep(5)
web.find_element_by_css_selector("#main-wrapper > main > div > div > div > div > div.fadfao3 > div > div > div > div > div > div > table > tbody > tr:nth-child(1) > td:nth-child(8) > button:nth-child(1)").click()

time.sleep(15)
print("准备开始抓取")
try:
    assert 1 != 1,'pa'
    web.find_element_by_css_selector("#main-wrapper > main > div > div > div > div > div > div > div > div.fadfao3 > div > div > div > div > div > div > table > tbody > tr")
except Exception as identifier:
    web.find_element_by_css_selector('#main-wrapper > main > div > div > div > div > div > div > div > div:nth-child(1) > div.f1kcmsuh > div:nth-child(2) > span:nth-child(1) > label').click()
    # web.find_element_by_css_selector("#main-wrapper > main > div > div > div > div > div > div > div > div.fadfao3 > div > div > div > div > div > div > table > tbody > tr").is_displayed()

# times = web.find_element_by_xpath('//*[@id="main-wrapper"]/main/div/div/div/div/div/div/div/div[2]/div/div/div/ul/li[1]').text()
# web.find_element_by_css_selector('#main-wrapper > main > div > div > div > div > div > div > div > div:nth-child(1) > div.f1kcmsuh > div:nth-child(2) > span:nth-child(1) > label > span.ant-checkbox.ant-checkbox-checked > input').click()
time.sleep(3)
# if times != "共 1 条":
#     pass      # 暂时由于

# 此页面为  攻击IP的攻击次数页面
web.find_element_by_css_selector("#main-wrapper > main > div > div > div > div > div > div > div > div.fadfao3 > div > div > div > div > div > div > table > tbody > tr > td:nth-child(8) > button").click()
attack_data = filter_data(web)
print(attack_data)

while True:
    try:

        monitor_date(web)
        Conditions = expected_conditions.visibility_of_any_elements_located((By.XPATH,"/html/body/div[2]/div/span/div"))
        WebDriverWait(driver=web,timeout=60,poll_frequency=0.5).until(Conditions)
        handle_message(web)

        # 点击警报首页中的第一条
        web.find_element_by_css_selector("#main-wrapper > main > div > div > div > div > div.fadfao3 > div > div > div > div > div > div > table > tbody > tr:nth-child(1) > td:nth-child(8) > button:nth-child(1)").click()
        times = web.find_element_by_css_selector("#main-wrapper > main > div > div > div > div > div > div > div > div.fadfao3 > div > div > div > ul > li.ant-pagination-total-text").text()
        # if times != "共 1 条":
        #     pass      # 暂时由于

        # 此页面为  攻击IP的攻击次数页面
        web.find_element_by_css_selector("#main-wrapper > main > div > div > div > div > div > div > div > div.fadfao3 > div > div > div > div > div > div > table > tbody > tr > td:nth-child(8) > button").click()
        attack_data = filter_data(web)
        print(attack_data)


    except Exception as f:
        print("正在监控……")








# if (web.find_element_by_css_selector("body > div:nth-child(8) > div > span > div").)

# time.sleep(30)