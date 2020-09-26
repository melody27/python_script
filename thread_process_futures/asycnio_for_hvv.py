import time 
import asyncio
from aiohttp import ClientSession
import re
import json
import queue
import os

# 此脚本为asycnio的样本，推荐使用此模块，此模块比gevent好用太多了。晓航师傅也推荐使用此模块

tasks = []
# true_result_path = 'result_id_all.txt'
true_result = 'result_id_2.txt'
# false_result_path = 'result_not_id_all.txt'
false_result = 'result_not_id_2.txt'

url = 'https://console.oray.com/passport/send-code'

true_result_list = []
false_result_list = []


async def jisuan(user_id, Semaphore, sess):
    data = {
        'account':'{}'.format(user_id)
    }

    async with Semaphore:
        
        async with sess.post(url=url,data=data,verify_ssl=False) as response:
            response = await response.text()

            if re.search(r'\\u8bf7\\u9009\\u62e9\\u9a8c\\u8bc1\\u65b9\\u5f0f',response):
                json_data = json.loads(response.encode('utf-8').decode('unicode_escape'))
                write_to_file(false_result,user_id,json_data['message'])
                # false_result_list.append([user_id,json_data['message']])
                return 
            try:
                json_data = json.loads(response.encode('utf-8').decode('unicode_escape'))
            except JSONDecodeError as identifier:
                print(response.encode('utf-8').decode('unicode_escape'))
            
            write_to_file(true_result,user_id,json_data['message'])
            # true_result_list.append([user_id,json_data['message']])


# def write_to_file(file_path,result_list):     # 数组方式存放数据
    # with open(file_path,'a+',encoding='utf-8') as f:
    #     for x in result_list:
    #         f.write(x[0]+"\t:\t"+x[1]+'\n')

def write_to_file(file_path,user_id,message):     # 数组方式存放数据
    open(file_path,'a+',encoding='utf-8').write(user_id+message+"\n")
        





async def run(target_file_url):

    raw_id = open(target_file_url,'r+',encoding='utf-8').readlines()

    semaphore = asyncio.Semaphore(500)
    print('开始')
    async with ClientSession() as sess:

        last = [ jisuan(x.strip(),semaphore,sess) for x in raw_id]
        await asyncio.wait(last)



if __name__ == "__main__":


    # 进行读取目录下文件的操作
    # file_url = '/root/workpsace/id_d/id_id/'
    # file_list = [ file_url+x for x in os.listdir(file_url)]
    # file_list.remove(file_url+'id_generate_all.txt')
    # for target_file_url in file_list:
    #     try:
    #         loop = asyncio.get_event_loop()
            
    #         loop.run_until_complete(run(target_file_url))
    #     except Exception as identifier:
    #         write_to_file('error_2.txt','root','this is error log')



    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(target_file_url='id_2_center.txt'))
    # write_to_file(false_result_path,false_result_list)
    # write_to_file(true_result_path,true_result_list)





