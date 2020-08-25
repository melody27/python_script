if __name__=='__main__':
    page=int(input('输入你的数'))
    page_list=10
    zong=[]
    
    z=0
    
    i=0
    for x in range(10000):
        zong.append(x)
    while True:
        dangqian=[]
        for x in range(page_list):
            dangqian.append(zong[i])
            i+=1
            if zong[i]==page:
                z=zong[i]
        if z==page:
            for x in dangqian:
                print(x)
            break


