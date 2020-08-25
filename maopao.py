from functools import reduce

z=0
d=[]
while z!=999:
    z=int(input('请输入要冒泡排序的数'))
    d.append(z)
def maopao(x,y):
    if x>y:
        z=x
        x=y
        y=z
e=reduce(maopao,d)
print(e)