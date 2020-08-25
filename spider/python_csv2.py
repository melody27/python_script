import csv
#此处为读取csv文件

with open('测试python写入csv.csv','r') as f:
    
    read = csv.reader(f)

    for x in read:
        print(x[0])
        if 'a' in x[0]:
            print('你好啊,我是小a')

