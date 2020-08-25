import requests
import pymysql
import time
from bs4 import BeautifulSoup
#这玩意可以用，把爬到的freebuff写入文件和数据库

url = 'https://www.freebuf.com/'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'refer':'www.baidu.com'
}

r = requests.get(url,headers=headers)
soup = BeautifulSoup(r.text,'html.parser')
kuang = soup.find_all('div',class_='news_inner news-list')

conn = pymysql.connect(
    host = '127.0.0.1',
    user = 'root',
    password = 'root',
    database = 'python_test'
)
cursor = conn.cursor()


with open('cest.html','w',encoding='utf-8') as f:
    for x in kuang:
            try:
                y = x.find('div',class_='news-info').dl.dt.a
            except :
                y = 'null'
            # print(y)
            # print(y.replace(' ','').replace('\n',''))
            f.writelines(str(y))
            f.writelines('<br>')
            print(y)
            try:
                z = x.find('div',class_='news-info').dl.dd.replace('img','kkp')
            except :
                z='null'
                
            # print(z)
            # print(z.replace(' ','').replace('\n',''))
            f.writelines(str(z))
            f.writelines('<br>')
            try:
                v = x.find('div',class_='news-info').find('dd',class_='text')
            except :
                v = 'null'
            # print(v.replace(' ','').replace('\n',''))
            f.writelines(str(v))
            f.writelines('<br><br>')

            sql = "insert into freebuff(title,time,content) values('%s','%s','%s')"%(y,z,v)
            print(sql)
            # sql = pymysql.escape_string(sql)  #此函数的作用为对特殊字符进行转义，这里暂时用不上
            cursor.execute(sql)

cursor.close()
conn.close()