import requests
# import pytesseract            暂时没有模块，先注释掉
from PIL import Image
import re
from bs4 import BeautifulSoup


s = requests.session()
url1 = 'http://lab1.xseclab.com/vcode7_f7947d56f22133dbc85dda4f28530268/index.php#'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

r1 = s.get(url1,headers=headers)
r1.encoding = 'utf-8'
print(r1.text)

url2 = 'http://lab1.xseclab.com/vcode7_f7947d56f22133dbc85dda4f28530268/mobi_vcode.php'
r2 = s.get(url2,headers=headers)
r2.encoding = 'utf-8'
print(r2.status_code)


soup = BeautifulSoup(r1.text,'html.parser')
# print('接下来是soup')
# print(soup.text)
tu = soup.img['src']
print('图片链接为')
print(tu)
with open('D:/python/python项目目录/spider/img/','wb') as f :

    f.writelines('1')