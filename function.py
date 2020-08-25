#这个地方反映出python的函数当有多个返回值的时候
def juedui(x,y):
	if(x>0):
		return x,y
	elif(x<=0):
		return -x,-y
x=int(input('请输入你需要的x值:'))
y=int(input('请输入你需要的y值:'))
z=juedui(x,y)
h,i=juedui(x,y)
y=1
print('这里风别输出x的值为%s y值为%s' %(h,i))
print('这里Z的值为:',z)
