import threading
import requests
import re
def spider(page):
    dizhi='https://v.paixin.com/mediapack/4/%s' % page
    headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}
    r=requests.get(dizhi,headers=headers)
    r.encoding='utf-8'
    print(r.text)
    imgdizhi=re.findall('^http:\/\/.+jpg',r.text)#http://d302.paixin.com/thumbs/3813349/184883396/staff_1024.jpg?imageView2/2/w/700/h/700
    print(imgdizhi)
spider(2)