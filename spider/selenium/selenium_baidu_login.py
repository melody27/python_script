from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time
import re



def detail(link):
    web.switch_to.window(winds[1])
    web.get(link)
    web.refresh
    question_title = web.find_element_by_css_selector('#wgt-ask > h1 > span')
    print(question_title.text)

    return question_title.text


def search(kw):
    web.switch_to.window(winds[2])
    url = 'https://zhidao.baidu.com/search?lm=0&rn=10&pn=0&fr=search&ie=gbk&word=%s'%(kw)
    web.get(url)
    web.refresh()
    try:
        question_details = web.find_element_by_css_selector('#wgt-list > dl:nth-child(1) > dt > a')
        question_details_link = question_details.get_attribute('href')
    except BaseException as identifier:
        pass
    

    
    return question_details_link



def answer_detail(ss):

    web.switch_to.window(winds[3])
    web.get(ss)
    time.sleep(2)
    answer = web.find_element_by_xpath('//*[@class="answer-text mb-10 line"]').text
    return answer






if __name__ == "__main__":
    url = 'https://www.baidu.com'


    # 进行实例化webdriver的设置
    option = webdriver.ChromeOptions()
    ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0"
    option.add_argument("User-agent="+ua)
    web = webdriver.Chrome(options=option)
    web.implicitly_wait(30)

    #请求百度首页并点击登录
    web.get(url)
    login = web.find_element_by_css_selector('#u1 > a.lb')
    print("准备开始"+login.text)
    login.click()

    #设置弹框中的qq登录的显性等待，等待结束后点击qq登录
    condition = expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,"#pass_phoenix_btn > ul > li.bd-acc-qzone > a"))
    WebDriverWait(driver=web,timeout=20,poll_frequency=0.5).until(condition)
    web.find_element_by_css_selector("#pass_phoenix_btn > ul > li.bd-acc-qzone > a").click()

    #切换到QQ安全登录的窗口
    time.sleep(5)
    winds = web.window_handles
    web.switch_to.window(winds[1])
    ccy = web.current_window_handle

    #进入QQ安全登录的iframe
    the_frame = web.find_element_by_css_selector("#ptlogin_iframe")
    web.switch_to.frame(the_frame)

    #显性等待qq登录的图片，等待结束后点击图片登录
    condition2 = expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,"#qlogin_list > a.face"))
    WebDriverWait(driver=web,timeout=20,poll_frequency=0.5).until(condition2)
    time.sleep(2)
    web.find_element_by_css_selector("#qlogin_list > a.face").click()

    #登录后立即切换到主窗口
    web.switch_to.window(winds[0])
    condition3 = expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,"#s_username_top > span"))
    WebDriverWait(driver=web,timeout=20,poll_frequency=0.5).until(condition3)
    time.sleep(2)

    #登录过程完成后直接到百度知道的界面
    url = "https://zhidao.baidu.com/list"
    web.get(url)

    web.refresh()
    questions = web.find_elements_by_class_name('title-link')

    script = 'window.open("http://www.baidu.com")'
    web.execute_script(script)
    script = 'window.open("http://www.baidu.com")'
    web.execute_script(script)
    script = 'window.open("http://www.baidu.com")'
    web.execute_script(script)
    winds = web.window_handles
    gg = []
    pp_answer = ''
    for y in questions:
        gg.append(y.get_attribute('href'))
    for x in gg:
        questions_title = detail(x)
        try:
            answer_question = search(questions_title)
        except BaseException as identifier:
            continue


        try:
            pp_answer = answer_detail(answer_question)
        except BaseException as identifier:
            continue

        web.switch_to.window(winds[1])
        web.find_element_by_css_selector('#answer-bar').click()
        web.switch_to.frame('ueditor_0')
        web.find_element_by_css_selector('body > p').send_keys(pp_answer)
        web.switch_to.default_content()
        web.find_element_by_css_selector('#answer-editor > div.addons.line > a').click()
#body > div.tags-box > div.tags-content > div.tags-bottom > div.tags-sub