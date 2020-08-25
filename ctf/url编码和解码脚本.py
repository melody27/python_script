import sys


class url(object):                  # 基类

    def __init__(self,string:str):

        self.string = string

class encode(url):                  # 编码字类

    def get_result(self):
        answer = ''
        for x in range(len(self.string)):
            zc = self.string[x:(x+1)]
            c = ord(zc)
            c = '%'+hex(c)[2:]
            answer = answer+c

        return answer

class decode(url):                  # 解码子类

    def get_result(self):
        
        list1 = self.string.split('%')[1:]
        # print(list1)
        answer = ''
        for x in range(len(list1)):
            x = list1[x]
            x = int(x,16)
            # print(x)
            x = chr(x)
            # print(x)
            answer = answer+x
        
        return answer


class url_factory(object):          # 工厂类

    def __init__(self,string,opreation):
        self.string = string
        self.opreation = opreation

    def factory_jisuan(self):

        url_opreation = None

        if self.opreation == 1:
            url_opreation = encode(self.string)
        elif self.opreation == 2:
            url_opreation = decode(self.string)

        return url_opreation

if __name__ == "__main__":

    print('''
        
    ███▄ ▄███▓▓█████  ██▓     ▒█████  ▓█████▄▓██   ██▓
    ▓██▒▀█▀ ██▒▓█   ▀ ▓██▒    ▒██▒  ██▒▒██▀ ██▌▒██  ██▒
    ▓██    ▓██░▒███   ▒██░    ▒██░  ██▒░██   █▌ ▒██ ██░
    ▒██    ▒██ ▒▓█  ▄ ▒██░    ▒██   ██░░▓█▄   ▌ ░ ▐██▓░
    ▒██▒   ░██▒░▒████▒░██████▒░ ████▓▒░░▒████▓  ░ ██▒▓░
    ░ ▒░   ░  ░░░ ▒░ ░░ ▒░▓  ░░ ▒░▒░▒░  ▒▒▓  ▒   ██▒▒▒ 
    ░  ░      ░ ░ ░  ░░ ░ ▒  ░  ░ ▒ ▒░  ░ ▒  ▒ ▓██ ░▒░ 
    ░      ░      ░     ░ ░   ░ ░ ░ ▒   ░ ░  ░ ▒ ▒ ░░  
        ░      ░  ░    ░  ░    ░ ░     ░    ░ ░     
                                        ░      ░ ░     

    
    ''')

while True:

    opreation = int(input("url解码或编码脚本：1：编码。2：解码。3：退出"))
    if opreation == 3:
        exit()
    elif opreation != 1 and opreation != 2:
        exit()
    string_1 = str(input("输入你要进行编码/解码的字符串"))



    result = url_factory(string_1,opreation)
    print(result.factory_jisuan().get_result())
    