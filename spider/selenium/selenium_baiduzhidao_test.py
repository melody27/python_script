from selenium import webdriver

url = "https://zhidao.baidu.com/question/2273207753519280428.html?fr=qlquick&is_force_answer=0&entry=list_default_level1"

web = webdriver.Chrome()

web.get(url)

# an = web.find_elements_by_css_selector('#qb-content')
# web.switch_to.frame(2)
# web.switch_to.frame(0)
aa = web.find_element_by_xpath('//*[@class="answer-text mb-10 line"]')
print(aa)