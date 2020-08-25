import math

def jisuan(a,b,c):
	z=b*b-4*a*c
	if(z<0):
		return '原方程无解'
	if(z==0):
		#这个时候原方程有两个相同的解
		d=-b/(2*c)
		return d
	if(z>0):
		d=((-b)+((b*b-4*a*c))**0.5)/(2*a)
		f=((-b)-((b*b-4*a*c))**0.5)/(2*a)
		return d,f
a=float(input('输入你想要的a值'))
b=float(input('输入你想要的b值'))
c=float(input('输入你想要的c值'))
print(jisuan(a,b,c))
