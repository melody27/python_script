def kebian(*nums):
	i=0
	for x in nums:
		i=i+x
	return i
t=[]
u=0
while(u!=999):
	u=int(input('请输入你需要加的数(ps.按999结束)'))
	if(u==999):
		break
	t.append(u)
#shu=[1,2,3,4,5,6]
print(kebian(*t))