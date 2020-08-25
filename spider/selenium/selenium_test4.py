from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

#哔哩哔哩的登录操作(未完成)
web = webdriver.Chrome()

url = "https://passport.bilibili.com/login"

web.get(url)

web.find_element_by_css_selector("#login-username").send_keys("18980455753")        #输入账号
web.find_element_by_css_selector("#login-passwd").send_keys("zxc1154717286")        #输入密码
if web.find_element_by_css_selector("#geetest-wrap > div > div.remember > div > label > label > input[type=checkbox]").is_selected():       #切换为不记住我
    web.find_element_by_css_selector("#geetest-wrap > div > div.remember > div > label > label").click()


login = web.find_element_by_css_selector("#geetest-wrap > div > div.btn-box > a.btn.btn-login")

ActionChains(web).click(login).perform()

time.sleep(3)

#拖动滑条

huatiao = web.find_element_by_css_selector("body > div.geetest_panel.geetest_wind > div.geetest_panel_box.geetest_no_logo.geetest_panelshowslide > div.geetest_panel_next > div > div.geetest_wrap > div.geetest_slider.geetest_ready > div.geetest_slider_button")

huantu = web.find_element_by_css_selector("body > div.geetest_panel.geetest_wind > div.geetest_panel_box.geetest_no_logo.geetest_panelshowslide > div.geetest_panel_next > div > div.geetest_panel > div > a.geetest_refresh_1")

chongshi = web.find_element_by_css_selector("body > div.geetest_panel.geetest_wind > div.geetest_panel_box.geetest_no_logo > div.geetest_panel_error > div.geetest_panel_error_content")

cuowu = web.find_element_by_css_selector("body > div.geetest_panel.geetest_wind > div.geetest_panel_box.geetest_no_logo > div.geetest_panel_error")
# ActionChains(web).drag_and_drop_byoffset(huatiao,100,0).perform()

while True:
    for x in range(5):

        if huatiao.is_displayed:
            ActionChains(web).drag_and_drop_by_offset(huatiao,86,0).perform()
            time.sleep(8)

            ActionChains(web).click(huantu).perform()
            time.sleep(2)
            print("开始换图")
    # cuowu.is_displayed:
    ActionChains(web).click(chongshi).perform()
    print("开始重置")
    time.sleep(2)




