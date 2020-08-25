from selenium import webdriver
# 自动执行提交学校瘟疫调查问卷



web = webdriver.Chrome()

url = "https://www.wjx.cn/m/55390531.aspx"

web.get(url)

web.find_element_by_id("q1").send_keys("张祥可")
web.find_element_by_css_selector("#q2 > option:nth-child(2)").click()
web.find_element_by_css_selector("#div3 > div.ui-controlgroup > div.ui-checkbox.huchi > div").click()
web.find_element_by_css_selector("#div4 > div.ui-controlgroup > div.ui-checkbox.huchi > div").click()
web.find_element_by_css_selector("#div5 > div.ui-controlgroup > div:nth-child(3) > div").click()
web.find_element_by_css_selector("#div6 > div.ui-controlgroup > div:nth-child(2) > div").click()
web.find_element_by_css_selector("#div7 > div.ui-controlgroup > div:nth-child(2) > div").click()
web.find_element_by_css_selector("#div8 > div.ui-controlgroup > div:nth-child(2) > div").click()

web .find_element_by_css_selector("#ctlNext").click()

