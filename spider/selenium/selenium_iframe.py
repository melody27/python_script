from selenium import webdriver
#切换iframe


        #通过百度知道来实验。百度知道嵌套了不少的iframe


url = 'https://zhidao.baidu.com/question/431404227562114812.html?fr=qlquick&is_force_answer=0&entry=list_default_level1'

option = webdriver.ChromeOptions()

ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0"

option.add_argument("User-Agent="+ua)

web = webdriver.Chrome(options=option)

web.get(url)

# web.switch_to.frame(0)
# element = web.find_element_by_tag_name('iframe')
web.switch_to.frame('ueditor_0')
content = web.find_element_by_css_selector('body > p')
content.send_keys("输入陈公公")

web.switch_to.default_content()
web.find_element_by_css_selector('#answer-editor > div.addons.line > a').click()