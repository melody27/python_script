#    练习题1
# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# i=[]  
# for a in [1,2,3,4]:
#     for b in [1,2,3,4]:
#         if not b==a:
#             for c in [1,2,3,4]:
#                 if not c==a and c!=b:
#                     print(a*100+b*10+c)
#                     c=a*100+b*10+c
#                     i.append(c)
# print(len(i))

# i = int(input('净利润:'))     题目2讲的比较有意思
# arr = [1000000,600000,400000,200000,100000,0]
# rat = [0.01,0.015,0.03,0.05,0.075,0.1]
# r = 0
# for idx in range(0,6):
#     if i>arr[idx]:
#         r+=(i-arr[idx])*rat[idx]
#         print((i-arr[idx])*rat[idx])
#         i=arr[idx]
# print(r)



# for x in range(85):  习题3
#     for z in range(85):
#         if (x*x-z*z)==168:
#             print(x,z)
#             print(x*x-268)


#题目：输入某年某月某日，判断这一天是这一年的第几天？
# nian=int(input('年'))
# yue=int(input('月'))
# ri=int(input('日'))
# di={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
# if nian%4==0:
#     di[2]=29
# tian=0
# for x in range(1,yue):
#     tian=tian+di[x]
# tian=ri+tian
# print('这是%s天'%tian)


#输入三个整数x,y,z，请把这三个数由小到大输出。sort()函数比较奇怪
# a=int(input('第一个数'))
# b=int(input('第二个数'))
# c=int(input('第三个数'))
# di=[]
# for x in a,b,c:
#     di.append(x)
# di.sort()
# print(di)

#斐波那契数列。
# i=int(input('输出'))
# # a,b=0,1
# def fub(n):
#     a,b=0,1
#     for x in range(n):
#         print(b)
#         a,b=b,b+a

# print(fub(i))


#将一个列表的数据复制到另一个列表中。
# a=[1,2,3,4,5,6]
# b=a[:]
# print(b)

# i=1
# j=1
# for x in range(1,10):
#     print
#     for z in range(1,10):
#         print('%s*%s=%s'%(x,z,x*z))



#暂停一秒输出，并格式化当前时间。
# import time
# def ff(ss):
#     for x in range(ss):
#         print(x)
#         print(time.strftime("%y-%m-%D-%H:%M:%S",time.localtime()))
#         time.sleep(1)
# ff(int(input('输入')))



#判断101-200之间有多少个素数，并输出所有素数。
# for x in range(101,201):
#     if x%2!=0 and x%3!=0:
#         if x%5!=0 and x%7!=0:
#             print(x)


#求水仙花数
# for x in range(1,10):
#     for z in range(0,10):
#         for y in range(0,10):
#             j=100*x+z*10+y
#             i=x*x*x+y*y*y+z*z*z
#             if i == j:
#                 print(j)



# def jiji(t):              该题为分解因数
#     d=[]
#     u=t
#     while u!=1:
#         for x in [2,3,5,7]:
#             if u%x==0:
#                 print('11')
#                 u=u/x
#                 d.append(x)
#             if x==u:
#                 break
#         if x%2!=0 and x%3!=0:
#             if x%5!=0 and x%7!=0:
#                 break
#     print(d)
# s=int(input('输入你想球的数'))
# jiji(s)


# s=int(input('输入成绩'))          利用条件运算符的嵌套来完成此题：
# if s>=90:                         学习成绩>=90分的同学用A表示，
#     print('a')                    60-89分之间的用B表示，60分以下的用C表示
# elif s>=60:
#     print('b')
# elif s<=60:
#     print('c')


# from datetime import datetime
# d=datetime.now()      输出指定格式的日期。
# print(d)


# i=input('输入你想甄别的字符')
# yingwen=0                     输入一行字符，分别统计出其中英文字母、空格、
# kongge=0                          数字和其它字符的个数。
# shuzi=0
# qita=0
# for x in i:
#     if x.isdigit():
#         shuzi+=1
#     elif x.isalpha():
#         yingwen+=1
#     elif x.isspace():
#         kongge+=1
#     else:
#         qita+=1
# print(yingwen,kongge,shuzi,qita)


# def jisuan(z,f):    18题求项数，
#     i=z#收集每个数
#     s=0#收集所有数
#     for x in range(f):
#         if x!=0:
#             i=i*10+z
#         s=s+i
#     return s
# z=int(input('输入你想要的数'))
# f=int(input('输入你想要得到的项数'))
# print(jisuan(z,f))

# def houlai():19题   求完数
#     list_2=[]
#     for x in range(2,1001):
#         list_1=[]
#         if x%2!=0 and x%3!=0:
#             if x%5!=0 and x%7!=0:
#                 continue
#         u=x
#         for y in range(1,u):
#             if u%y==0:
#                 list_1.append(y)
#         z=0
#         for i in list_1:
#             z=z+i
#         if z==x:
#             list_2.append(x)
#     print('1000以内的完数为',list_2)
# houlai()


# def ff():               19题  一个数如果恰好等于它的因子之和，这个数就称为"完数"。
#     ilist=[]                  例如6=1＋2＋3.编程找出1000以内的所有完数。
#     for j in range(2,1001):
#         u=[]
#         h=0
#         for x in range(1,j):
#             if j%x==0:
#                 u.append(x)
#         for s in u:
#             h=s+h
#         if h==j:
#             ilist.append(j)
#     print('1000以内的所有的完数为',ilist)
# print(ff())

# def ff():         20题  ：一球从100米高度自由落下，
#     fast=100              每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，
#     heightall=0           共经过多少米？第10次反弹多高？
#     height=0
#     for x in range(1,11):
#         if x==1:
#             heightall=heightall+fast
#         else:
#             fast=fast/2
#             heightall=heightall+2*fast
#     height=fast/2#这个地方之所以除以二是因为，fast是第十次下落的总高度，包括了上去和下来的

#     print('总高度为',heightall)
#     print('第十次的高度为',height)
# ff()


# def ff():         21题：猴子吃桃问题：猴子第一天摘下若干个桃子，
#     peach=1               当即吃了一半，还不瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
#     for x in range(9):    以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。
#         peach=(peach+1)*2     求第一天共摘了多少
#     print(peach)
# ff()



# 21题 两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。
#      已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，
#      请编程序找出三队赛手的名单。
# def ff():               
#     for x in ['y','x','z']:
#         print(x)
#         for j in ['y','x','z']:
#             if x!=j:
#                 for h in ['y','x','z']:
#                     if h!=x and h!=j :
#                         if x!='x' and h!= 'x' and h!='z':
#                             print('a-->%s,b-->%s,c-->%s'%(x,j,h))
# ff()

# 23题打印出:
#     *    
#    ***   
#   *****  
#  ******* 
#   *****  
#    ***   
#     *
# def ff():                     
#     l=7
#     i=1
#     z=5
#     for x in range(4):
#         left=' '*((7-i)//2)
#         xing='*'*i
#         right=' '*((7-i)//2)
#         print(left,xing,right)
#         i=i+2
#     for x in range(3):
#         lef=' '*((7-z)//2)
#         xing='*'*z
#         right=' '*((7-z)//2)
#         print(lef,xing,right)
#         z=z-2
# ff()


# def ff():           24题：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
#     x=2
#     y=1
#     z=0
#     for v in range(20):
#         z=z+x/y
#         x,y=x+y,x
#     print(z)
# ff()


# 25题：求1+2!+3!+...+20!的和。(这个是阶乘)
# def ff():
#     num=0
#     for x in range(1,20+1):
#         num2=1
#         for y in range(1,x+1):
#             num2=num2*y
#         num=num+num2
#     print(num)
# ff()

# 26题：利用递归方法求5!。
# def ff(n):
#     jj=n
#     if(n==1):
#         jj=1
#     else:
#         jj=ff(n-1)*jj
#     return jj
# print(ff(5))



# def ff(s,l):      27题   利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
#     if l==0:
#         return print(s)
#     print (s[l-1])
#     ff(s,l-1)
# jisuan=input('笨比')
# l=len(jisuan)
# ff(jisuan,l)


# 28题，有五个人，每个人依次比后面那个人大2岁，最后面那个人10岁，求最大的那个多大
# def ff(n):
#     if n==1:
#         return 10
#     return ff(n-1)+2
# print('最大的是',ff(5))
# 利用递归的方法，递归分为回推和递推两个阶段。
# 要想知道第五个人岁数，需知道第四人的岁数，依次类推，推到第一人（10岁），再往回推。



#29题
# 给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
# x=int(input('请输入一个数'))
# a=x/10000
# b=x%10000//1000
# c=x%1000//100
# d=x%100//10
# e=x%10
# if a!=0:
#     print('五位数',e,d,c,b,a)
# elif b!=0:
#     print('四位数',d,c,b,a)
# elif c!=0:
#     print('三位数',c,b,a)
# elif b!=0:
#     print('两位数',b,a)
# elif a!=0:
#     print('一位数',a)

# 学会分解出每一位数。




#方法二
# def ff(n,l):
#     if l==1:
#         print(n)
#         return
#     else:
#         print(n[-1])
#         ff(n[:-1],l-1)
# jisuan=input('请给一个不多于五位的正整数')
# l=len(jisuan)
# print('该正整数的长度为',l)
# ff(jisuan,l)

# 30题，一个5位数，判断它是不是回文数。即12321是回文数
# jisuan=input('判断是否为回文数')
# if jisuan==jisuan[::-1]:
#     print(jisuan,'这个数确实是回文数')
# else:
#     print(jisuan,'这个数不是回文数')


# 31题，请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
# jisuan=input('周几')
# if jisuan[0]=='m':
#     if jisuan[1]=='o':
#         print('今天是周一',jisuan)
# elif jisuan[0]=='t':
#     if jisuan[1]=='u':
#         print('今天是周2',jisuan)
#     elif jisuan[1]=='h':
#         print('今天是周4',jisuan)
# elif jisuan[0]=='w':
#     if jisuan[1]=='e':
#         print('今天是周3',jisuan)
# elif jisuan[0]=='f':
#     if jisuan[1]=='r':
#         print('今天是周五',jisuan)
# elif jisuan[0]=='s':
#     if jisuan[1]=='a':
#         print('今天是周6',jisuan)
#     elif jisuan[1]=='u':
#         print('今天是周天',jisuan)

# 32题
# 按相反的顺序输出列表的值。
# a=['one','two','three']
# print(a[::-1])


# 33题，
# 按逗号分隔列表。(主要是熟悉list转化为str,包括list内是int的情况)
# a=[1,2,3,4,5]
# ss=",".join('%s' %x for x in a)    即遍历list的元素，把他转化成字符串。这样就能成功输出1，2，3，4，5了。
# print(ss)
# print(type(ss))

# 34题
# 函数的调用
# def jiji():
#     print('卡哇伊')
# def jijis():
#     for x in range(100):
#         jiji()
# if __name__=='__main__':
#     jijis()

# 35题
# 文本颜色设置
# class bcolors:
#     HEADER = '\033[95m'
#     OKBLUE = '\033[94m'
#     OKGREEN = '\033[92m'
#     WARNING = '\033[93m'
#     FAIL = '\033[91m'
#     ENDC = '\033[0m'
#     BOLD = '\033[1m'
#     UNDERLINE = '\033[4m'
# print(bcolors.WARNING + "警告的颜色字体?" + bcolors.ENDC)

# 36题
# 求100之内的素数。
# def ff():
#     for x in range(1,101):
#         if x%2!=0 and x%3!=0 and x%5!=0 and x%7!=0:
#             print(x)
# ff()


# 37题
# 对10个数进行排序。(选择排序法，)
# def ff(l):
#     f=10
#     for x in range(f-1):
#         min=x
#         for d in range(x+1,f):
#             if l[min]>l[d]:
#                 min=d
#         l[x],l[min]=l[min],l[x]
#     for y in range(f):
#         print(l[y])
# list_1=[]
# for x in range(10):
#     list_1.append(int(input('输入你要比较的十个数')))
# print(list_1)
# ff(list_1)

# def ff(n):
#     print(sorted(n))

# list_1=[]
# for x in range(10):
#     list_1.append(int(input('输入你要比较的十个数')))
# ff(list_1)

# 38题
# 求一个3*3矩阵主对角线元素之和。
# def ff():
#     i=[]
#     sum=0
#     for x in range(3):
#         i.append([])
#         for y in range(3):
#             i[x].append(int(input('输入你想要得到的数')))
#         sum+=i[x][x]
#     print(sum)
# ff()

# 39题
# 有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
#冒泡排序
# def ff(n):
#     i=[22,33,11,445,334663,356]
#     i.append(n)
#     len_i=len(i)
#     for x in range(len_i-1):
#         for z in range(x+1,len_i):
#             if i[x]>i[z]:
#                 i[x],i[z]=i[z],i[x]
#     print(i)
# ff(int(input('输入你想计算的数字')))

# 39题
# 将一个数组逆序输出
# def ff(n):
#     len_n=len(n)
#     for i in range(len_n // 2):
#         print(len_n-i-1)
#         n[i],n[len_n - i - 1] = n[len_n- i - 1],n[i] 这里的len_n-1-i表示最后数组最后一位数
#     print(n)

# i=[]
# for x in range(5):
#     i.append(int(input('输入你想要计算的值')))
# ff(i)

# 40题
# 模仿静态变量的用法。
# def varfunction():
#     var=0
#     print(var)
#     var+=1
# if __name__=='__main__':
#     for x in range(3):
#         varfunction()
# class Student(object):
#     var=0
#     def varfunction(self):
#         self.var+=1
#         print(self.var)
# print('类的属性var的值为',Student.var)
# s=Student()
# for x in range(3):
#     s.varfunction()

# 42题
# 学习使用auto定义变量的用法。
# 程序分析：没有auto关键字，使用变量作用域来举例吧。
# num=4
# def jisuan(num):
#     num=1
#     print('函数里的num值为',num)
#     num+=1
# for x in range(3):
#     print('循环里的num值为',num)
#     num+=1
#     jisuan(num)

# 43题
# 模仿静态变量(static)另一案例。
# 程序分析：演示一个python作用域使用方法
# class Student(object):
#     name=11
#     def change(self):
#         self.name+=1
#         print('类的属性name的值为',self.name)
# if __name__=='__main__':
#     name=2
#     s=Student()
#     for x in range(3):
#         print('循环的name值为',name)
#         name+=1
#         s.change()


# 44题
# 两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵
# x= [[12,7,3],
#     [4 ,5,6],
#     [7 ,8,9]]
# y= [[5,8,1],
#     [6,7,3],
#     [4,5,9]]
# list_1=[]
# for i in range(3):
#     list_1.append([])
#     for c in range(3):
#         list_1[i].append(x[i][c]+y[i][c])
# print(list_1)


# 45题
# 统计 1 到 100 之和。
# sum=0
# for x in range(101):
#     sum+=x
#     print(x)
# print(sum)

# 46题
# 求输入数字的平方，如果平方运算后小于 50 则退出。
# def jisuan(n):
#     return n*n
# num_2=100
# print('输入你要计算的数的平方，如果平方值小于50，则推出')
# while num_2>50:
#     num_1=int(input('输入你要计算数字的平方'))
#     num_2=jisuan(num_1)
#     print('该数的平方为',num_2)

# 47题
# 两个变量值互换。
# num_1=input('输入第一个数')
# num_2=input('输入第二个数')
# num_3=num_1
# num_1=num_2
# num_2=num_3
# print(num_1)
# print(num_2)


# 48题
# 数字比较。
# def bijiao(n,i):
#     q1='<'
#     q2='>'
#     q4='='
#     q3=''
#     if n>i:
#         q3=q2
#     elif n==i:
#         q3=q4
#     elif n<i:
#         q3=q1
#     print('%s%s%s'%(n,q3,i))
# if __name__=='__main__':
#     num_1=int(input('比较的第一个数'))
#     num_2=int(input('比较的第二个数'))
#     bijiao(num_1,num_2)


# 49题
# 使用lambda来创建匿名函数。
# max=lambda x,y: (x>y)*x+(x<y)*y       这里的话当x大于y返回值就为true就会实行x，后面的false就不会执行
# min=lambda  x,y: (x<y)*x+(x>y)*y
# if __name__=='__main__':
#     a=10
#     b=421
#     print('大的值为',max(a,b))
#     print('小的值为',min(a,b))


# 50题
# 题目：输出一个随机数
# import random
# print(random.random())

# 51题
#按位与，按位或，按位异或，按位取反
# 对数据的每个二进制位取反,即把1变为0,把0变为1 。~x 类似于 -x-1
# if __name__ == '__main__':
#     a=151
#     b=211
#     c=a&b
#     print('按位与c的值为',c)
#     d=a|b
#     print(b)
#     e=a^b
#     print('按位异或e的值为',e)
#     f=~a
#     print('按位取反f的值为',f)对数据的每个二进制位取反,即把1变为0,把0变为1 。~x 类似于 -x-1



# 52题
# 取一个整数a从右端开始的4〜7位。
# (1)先使a右移4位。
# (2)设置一个低4位全为1,其余全为0的数。可用~(~0<<4)
# (3)将上面二者进行&运算。
# u=int(input('输入哟个你想要的数'))
# b=u>>4
# print(~0<<4)
# f=~(~0<<4)
# print(u,b&f)



# 55题
# 学习使用按位取反~。
# 取一个整数a从右端开始的3〜7位。
# i=int(input('输入你想求的该数'))
# b=i>>2
# f=~(~0<<5)
# c=b&f
# print('你想球的该数的是',c)

# 56题
# 计算字符串长度
# str_1=input('请计算str长度')
# print(len(str_1))

# 61题
# 使用生成器打印出杨辉三角
# def ff():
#     list_1=[1]
#     while len(list_1)<11:
#         yield list_1
#         list_1=[1]+[list_1[i]+list_1[i+1] for i in range(len(list_1)-1)]+[1]
# n=0
# o=[]
# for x in ff():
#     o.append(x)
#     n+=1
#     if n==10:
#         break
# for t in o:
#     print(t)

# 62题
# 查找字符串
# str_1=input('输入你要查找的字符串')
# str_2=input('输入被查找的字符串')
# print(str_2.find(str_1))这个地方返回的是被查找的字符串的下标

# 66题
# 输入3个数a,b,c，按大小顺序输出。　　　
# i=[]
# for x in range(3):
#     i.append(int(input('输入你要计算的比大小的三个数')))
# def ff(list_1):
#     l=len(list_1)
#     for x in range(len(list_1)):
#         for c in range(x,len(list_1)):
#             if list_1[x]>list_1[c]:
#                 list_1[x],list_1[c]=list_1[c],list_1[x]
#     print(list_1)
# ff(i)

# 67题
# 输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。
# def ff(list_1):
#     max=0
#     min=0
#     l=len(list_1)
#     for x in range(l):
#             if list_1[x]>list_1[max]:
#                 max=x
#             if list_1[x]<list_1[min]:
#                 min=x
#     list_1[max],list_1[0]=list_1[0],list_1[max]
#     list_1[min],list_1[len(list_1)-1]=list_1[len(list_1)-1],list_1[min]
# i=[7,1,3,455,8,896523784512,444,9]
# ff(i)
# print(i)




# 68题
# 有 n 个整数，使其前面各数顺序向后移 m 个位置，最后 m 个数变成最前面的 m 个数
# str_1=input('输入你想要得到的整数')
# num_1=int(input('输入你想要后移的个数'))
# list_1=list(str_1)
# list_2=[]
# daxiao=[]
# for x in range(num_1):
#     x+=1
#     list_2.append(list_1[-x])
# list_2.reverse()
# for x in range(len(list_1)):
#     daxiao.append(x)
# daxiao.reverse()
# for x in range(0,len(list_1)-num_1):
#     x=x+1
#     list_1[-x]=list_1[-x-num_1]
# for x in range(len(list_2)):
#     list_1[x]=list_2[x]
# print(list_1)



# 69题
# 有n个人围成一圈，顺序排号。
# 从第一个人开始报数（从1到3报数），
# 凡报到3的人退出圈子，问最后留下的是原来第几号的那位。
# n=int(input('总人数为多少'))
# list_1=[]
# for x in range(n):
#     list_1.append(x+1)
# i=0
# num_1=0
# k=0
# while k<n-1:
#     if list_1[i]!=0:
#         num_1+=1
#     if num_1==3:
#         num_1=0
#         list_1[i]=0
#         k+=1
#     i+=1
#     if i==n:
#         i=0
# i=0
# while list_1[i]==0:
#     i+=1
    
# print(list_1)
        

# 70题
# 写一个函数，求一个字符串的长度，在main函数中输入字符串，并输出其长度。
# def ff(str_1):
#     print(len(str_1))
# if __name__=='__main__':
#     str_1=input('输入一个字符串')
#     ff(str_1)

# 71题
# 编写input()和output()函数输入，输出5个学生的数据记录。
# n=3
# student_list=[]
# for x in range(3):
#     student_list.append(['','',[]])
# def input_student(student_list):
#     for i in range(n):
#         student_list[i][0]=input('输入学生的学号')
#         student_list[i][1]=input('输入学生的名字')
#         for z in range(3):
#             student_list[i][2].append(int())
# def output_student(student_list):
#     for i in range(n):
#         print('%-6s%-10s' % ( student_list[i][0],student_list[i][1] ))
#         for j in range(3):
#             print('%-8d' % student_list[i][2][j]) 
# if __name__=='__main__':
#     input_student(student_list)
#     print('---'*10)
#     output_student(student_list)



# 72题
# 创建一个链表
# if __name__=='__main__':
#     f=[]
#     for x in range(5):
#         str_1=int(input('输入你要创建的链表的元素'))
#         f.append(str_1)
#     print(f)


# 73题
# 反向输出一个链表。
# if __name__=='__main__':
#     f=[]
#     d=[]
#     for x in range(5):
#         str_1=int(input('输入你想要得到的数组元素'))
#         f.append(str_1)
#     for y in range(len(f)):
#         d.append(f[-y-1])
#     print(d)



# 74题
# 列表排序及连接。
# 程序分析：排序可使用 sort() 方法，连接可以使用 + 号或 extend() 方法。
# if __name__=='__main__':
#     a=[1,2,3,4,55,8]
#     b=[2,1,43,7,8,6]
#     a=sorted(a)
#     a[len(a):len(a)]=b
#     print(a)

# 76题
# 编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n
# def ou(n):
#     list_1=[]
#     sum_1=0
#     for x in range(1,n+1):
#         if x%2==0:
#             list_1.append(1/x)
#     for y in list_1:
#         sum_1+=y
#     print('当输入的数为偶时，其所得的值为',sum_1)


# def ji(n):
#     list_1=[]
#     sum_1=0
#     for x in range(1,n+1):
#         if x%2!=0:
#             list_1.append(1/x)
#     for x in list_1:
#         sum+=x
#     print('当输入的数为奇数时所得的值为',sum_1)
# if __name__=='__main__':
#     n=int(input('输入一个数'))
#     if n%2==0:
#         ou(n)
#     else:
#         ji(n)


# 77题
# 循环输出列表
# if __name__=='__main__':
#     i=['iuytre','jhgfd,','likujnhytfr','iouy','rtf']
#     for x in range(len(i)):
#         print(i[x])

# 78题
# 找到年龄最大的人，并输出。请找出程序中有什么问题。
# if __name__=='__main__':
#     i={'li':12,'jisuan':33,'rgf':99,'jack':123,'houlai':963}
#     j='li'
#     for key in i.keys():
#         if i[key]>i[j]:
#             j=key
#     print('最大的人为',j,i[j])

# 79题
# 字符串排序。
# if __name__=='__main__':
#     str_1=input('输入一行字符串')
#     str_2=input('输入一行字符串')
#     str_3=input('输入一行字符串')
#     if str_1>str_2:
#         str_1,str_2=str_2,str_1
#     if str_1>str_3:
#         str_1,str_3=str_3,str_1
#     if str_2>str_3:
#         str_2,str_3=str_3,str_2
#     print(str_1)
#     print(str_2)
#     print(str_3)



# 80题
# 海滩上有一堆桃子，五只猴子来分。第一只猴子把这堆桃子平均分为五份，
# 多了一个，这只猴子把多的一个扔入海中，拿走了一份。第二只猴子把剩下
# 的桃子又平均分成五份，又多了一个，它同样把多的一个扔入海中，拿走了
# 一份，第三、第四、第五只猴子都是这样做的，问海滩上原来最少有多少个
# 桃子？
# if __name__=='__main__':
#     i=6
#     z=0
#     p=0
#     for x in range(1,10000):
#         for l in range(5):
#             z=x*5/4+1
#             x=z
#         if (x-1)%5==0:
#             print(x)

# 81题
# 809*??=800*??+9*?? 其中??代表的两位数, 809*??为四位数，
# 8*??的结果为两位数，9*??的结果为3位数。求??代表的两位数，
# 及809*??后的结果。
# if __name__=='__main__':
#     for x in range(10,100):
#         if 809*x==800*x+9*x:
#             print('x的值为',x)
#             print('809*??的值为',809*x)

# 82题
# 八进制转换为十进制
# if __name__=='__main__':
#     i=[]
#     num_1=int(input('输入一个数'))
#     z=oct(num_1)
#     print('转化为八进制为',z)
#     print('转化为十进制为',int(z,8))
# 方法二
# num_1=input('输入你想要转换为十进制的八进制数')
# num_2=0
# for x in range(len(num_1)):
#     num_2=num_2*8+int(num_1[x])
# print(num_2)


# 83题
# if __name__=='__main__':
#     p=[]
#     for x in range(1000):
#         if int(str(x)[-1])<8:
#             if x%2!=0:
#                 p.append(x)
#     print(len(p))

# 84题
# 拼接字符串
# i='...'
# j=['dsa','dsa','ffds']
# print(i.join(j))

# 85题
# 输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。
# if __name__=='__main__':
#     num_1=int(input('输入一个奇数'))
#     for x in range(1,10):
#         ge=x*'9'
#         if int(ge)%num_1==0:
#             print(ge)
#             break

# 86题
# 两个字符串连接程序。
# if __name__=='__main__':
#     str_1=input('输入第一个字符串')
#     str_2=input('输入第二个字符串')
#     print(str_1+str_2)

# 87题
# 回答结果（结构体变量传递）。
# class Student(object):
#     name='jack'
#     age=20
# def ff(Student):
#     Student.name='jackal'
#     Student.age=998
# if __name__=='__main__':
#     a=Student()
#     print('方法前的name',a.name)
#     print('方法前的age',a.age)
#     ff(a)
#     print('方法后的name',a.name)
#     print('方法后的age',a.age)


# 88题
# 读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊。
# if __name__=='__main__':
#     for x in range(7):
#         i=int(input('输入一个数'))
#         print(i*'*')

# 89题
# 某个公司采用公用电话传递数据，数据是四位的整数，
# 在传递过程中是加密的，加密规则如下：每位数字都加上5,
# 然后用和除以10的余数代替该数字，再将第一位和第四位交换，
# 第二位和第三位交换。
# if __name__=='__main__':
#     num_1=int(input('输入一个数'))
#     str1=str(num_1)
#     str2=''
#     for x in str1:
#         x=int(x)+5
#         x=x%10
#         str2=str2+str(x)
#     str2=list(str2)
#     str2[0],str2[3]=str2[3],str2[0]
#     str2[1],str2[2]=str2[2],str2[1]
#     print(''.join(str2))



# 91题
# 时间函数举例1。
# from datetime import datetime
# print(datetime.now())

# 92题
# 时间函数举例
# import time
# def ff():
#     for x in range(50):
#         print(x)
#         time.sleep(0.5)
# if __name__=='__main__':
#     start=time.time()
#     ff()
#     end=time.time()
#     print(end-start)

# 93题
# Python time clock() 函数以浮点数计算的秒数返回当前的CPU时间。
# 用来衡量不同程序的耗时，比time.time()更有用。
# import time 
# def ff():
#     for x in range(10000):
#         print(x)
# if __name__=='__main__':
#     start=time.clock()
#     ff()
#     end=time.clock()
#     print(end-start)


# 94题
# 猜数游戏(最后打印出猜数时间)
# import random
# import time
# if __name__=='__main__':
#     random_1=random.randint(1,100)
#     start=time.clock()
#     while True:
#         i=int(input('猜一个数'))
#         if i>random_1:
#             print('大了')
#         elif i<random_1:
#             print('小了')
#         if i==random_1:
#             print('恭喜你猜对了')
#             print(random_1)
#             break
#     end=time.clock()
#     print('猜的时间为',end-start)


# from datetime import datetime
# for x in range(30):
#     print(datetime.now())

# 96题
# 使用count函数查找字符(count函数返回的是查找到的字符的个数))
# str_1=input('输入字符串')
# find_1=input('输入查找的字符')
# str_2=str_1.count(find_1,0,len(str_1))
# print(str_2)


# 97题
# 从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止。
# str_1=''
# with open('D:/python/test','a') as f:
#     while str_1!='#':
#         str_1=input('输入要写入的文件')
#         f.write(str_1)

# 98题
# 把小写字母转化为大写字母保存
# str_1=input('输入你要保存的小写字母')
# with open('d:/python/test2','w') as f:
#     f.write(str_1.upper())

# 99题
# 把两个文件的内容保存到另一个新的文件当中
# with open('d:/python/test','r') as f:
#     result_1=f.read()
# with open('d:/python/test2','r') as z:
#     result_2=z.read()
# with open('d:/python/test3','w') as f:
#     f.write(result_1+result_2)



# 100题
# 把list转化为dict使用zip函数封装用dict函数转化
# i=['jackal','mackal','lisa']
# n=[19,18,20]
# dict_1=dict(zip(i,n))
# print(dict_1)