import hashlib

m = hashlib.md5()

# m.update(b'123')

disits = '9123456780'

for a in disits:
    for b in disits:
        for c in disits:
            for d in disits:
                for e in disits:
                    for f in disits:
                        for g in disits:
                            b = str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g)
                            m.update(b.encode('utf8'))
                            md5 = m.hexdigest()
                            # md5 = '6d0bc155'
                            print(md5)
                            if md5[:6] == '6d0bc1':
                                print("成功")
                                print(b)
                                print("md5后的值为："+md5)
                                exit()



