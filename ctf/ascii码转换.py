import sys

def zhuan1(ss):
    tt = ''
    for x in ss:
        x = str(ord(x))
        tt = tt+x
    return tt

def jie1(ss):
    tt = ''
    ss = chr(ss)
    return ss


if __name__ == "__main__":
    yt = ''
    zt = ''
    while True:
        try:
            action = int(input("输出你想进行的操作。1：转码。2：解码。0：退出"))
        except Exception as identifier:
            pass
        if action == 1:
            try:
                y = str(input("输入你要转换的字符串"))
                zt = zhuan1(y)
                print('转码后得到的为：'+zt)
            except Exception as identifier:
                pass
        elif action == 2:
            try:
                
                print("你上次转换出的数为："+yt)
                y = int(input("输入你要转换的十进制数"))
                yt = yt+jie1(y)
                print("转换得到的数为："+yt)
            except Exception as identifier:
                pass
        elif action == 0:
            sys.exit()
