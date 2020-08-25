import csv
#此处为写入csv文件

with open('测试python写入csv.csv','a',newline='') as csv_xie:  #此处不使用newline的话，那么csv写入的数据之间就会空出一行空白行
    csv = csv.writer(csv_xie)
    csv.writerow(['姓名','年龄','电话'])           #单行写入
    test = [
        ('小a','17','110'),
        ('小b','19','120')
    ]
    csv.writerows(test)                     #多行写入
