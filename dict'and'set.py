#这个地方使用dict，注意写dict的格式'one':18。输出或者用的时候要注意jay['one']的格式(ps。里面要有单引号因为是字符串)
jay={'one':18,'two':17,'three':16}
print(jay['one'])
jay['four']=1    	#这里是把数据放入dict的方法，还是要注意里面加上单引号''
print(jay['two'])
print(jay)
#print(jay['tom']) 这里是示意当dict中要求输出不存在的key对应的key值时，会报错


jay['five']=33#这个地方是直接通过key（five）添加一个数据（33）
jay['five']=44#这个地方是像表达通过重新给value的方法把上次的值(33)给冲掉
print(jay['five'])

print('if' in jay)#这个地方的输出值为false，通过in这个方法来确认是否key(if)在dict(jay)中

print('这里的示意是dict的get方法返回值的问题：%s'%(jay.get('tom',-1)))
			#上面一行这个地方如果不加-1的话就会直接%S占位符出现的就是none后面这个表达式的值为none