s=input('请输入你的s值')
def trim(s):
    i=[]
    for x in s:
            i.append(s[x])
    return i
print(trim(s))