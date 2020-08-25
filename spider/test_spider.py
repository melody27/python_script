import requests
from bs4 import BeautifulSoup

def spider():
    
    url = "https://movie.douban.com/subject/27119724/?tag=%E7%83%AD%E9%97%A8&from=gaia"

    headers = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0"
    }

    r = requests.get(url,headers=headers)
    bs4(r)

def bs4(content):
    bs = BeautifulSoup(content.content,"html.parser")

    title = bs.find('span',property="v:itemreviewed").text
    fenshu = bs.find('strong',property='v:average').text
    contentd = bs.find('span',property="v:summary").text        #此处的property为对应的标签的property属性
    taolun = bs.findAll('div',class_="short-content")
    
    with open("joker.txt","a",encoding="utf-8") as f:
        f.write(title+"    "+ fenshu+"\n")
        f.write(contentd+"\n")
        for x in taolun :
            z = x.text.replace(' ',"").replace("(展开)","").replace('\n\n\n\n\n',"")
            print(z)
            f.write(z)

    print("结束")


spider()