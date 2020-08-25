
#对字符串的ascii码,进行加1的加密解密脚本。

def kkp(ss):

    y = ''
    for x in range(len(ss)):
        c = ss[x:(x+1)]
        print("c的值等于",)
        z = ord(c)+1
        c = chr(z)
        y = y+c

    return y

def fankkp(ss):
    y = ''

    for x in range(len(ss)):
        c = ss[x:(x+1)]
        z = ord(c)-1
        c = chr(z)
        y = y+c
    
    return y


action = input("输入你要进行解码的字符串。1：测试。2：编码。3：解码")

if action == '1':
    ff = kkp(input("输入测试字符串"))
    print("进行编码：",ff)

    print("进行解码:",fankkp(ff))

elif action == '2':
    ff = kkp(input("输入编码字符串"))
    print("编码结果为：",ff)

elif action == '3':
    ff = fankkp(input("输入解码字符串"))
    print("解码结果为：",ff)

