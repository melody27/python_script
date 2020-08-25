name=0
a=[1,2,3,4,5,6,7,8,9,10]
for x in a:
	name+=x
print(name)
c=0
for x in (1,2):
	c+=name
print(c)


#使用for X in循环计算0到100的和
p=0
for x in range(101):
	p+=x
print('0到100的值为''%d' %(p)) #我发现这里不能像java里面直接写+p(ps.这里的p是变量)


#以下是while循环
u=0
y=100
while y>0:
	u+=y
	y-=2
print('while循环的u值为'+str(u))


#请利用循环依次对list中的每个名字打印出Hello, xxx!：
L = ['Bart', 'Lisa', 'Adam']

for x in L:
    print(x)
	
	
p=len(L)
i=0
while i<p:
   print('使用while循环得到的：%s'%(L[i]))
   i+=1
 
 #使用break来结束打断循环
zzi=0
while zzi<100:
	zzi+=1
	if (zzi>10):
		break
	print('break结束的值为'+str(zzi))

#使用continue来跳过本次循环
uzi=0
while uzi<100:
	uzi+=1
	if(uzi%2==1):	#这个地方我有一个错误我写成了uzi%2=1,这样是错的。"="是赋值运算,"=="才是比较运算
		continue
	print('continue结束挑选得到的偶数为'+str(uzi))