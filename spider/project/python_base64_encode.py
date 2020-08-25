import base64

with open('D:\python\python项目目录\\10_million_password_list_top_100.txt','r+') as f:
    list = []
    for x in f.readlines():
        x = 'admin:%s'%(x)
        print(x)
        list.append(x)
    for y in list:
        y = y.encode('utf-8')
        new_y = base64.b64encode(y)
        f.writelines(new_y)

