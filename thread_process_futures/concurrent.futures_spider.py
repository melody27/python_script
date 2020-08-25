import requests
from concurrent.futures import ThreadPoolExecutor,wait,ALL_COMPLETED,as_completed
import time
import os

headers = {
            "Host": "api.vc.bilibili.com",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0",
            "Accept-Language": "zh-CN,en-US;q=0.7,en;q=0.3",
            "Accept-Encoding": "gzip, deflate",
            "Referer": "https://h.bilibili.com/eden/picture_area",
            "Origin": "https://h.bilibili.com"
        }

path = '/tmp/test'


def get_response(times):
    img_and_title = {}
    url = 'https://api.vc.bilibili.com/link_draw/v2/Photo/list?category=cos&type=hot&page_num={}&page_size=20'.format(str(times))
    r = requests.get(url=url,headers=headers)
    r_dict = eval(r.text)
    for User_lists in r_dict['data']['items']:
        img_and_title[User_lists['user']['name']] = []
        for img_list in User_lists['item']['pictures']:
            img_and_title[User_lists['user']['name']].append(img_list['img_src'])
    # print(img_and_title)
    return img_and_title

def make_user_directory(user_dict:dict):
    img_dict = []
    # print('输入的dict is ：{}'.format(user_dict))
    # for keys,values in user_dict.items():
    #     print("key true is :{}".format(keys))
    for keys,values in user_dict.items():
        try:
            os.makedirs(path+'/'+keys)
            print("key is ：{}".format(keys))
            
        except FileExistsError as identifier:
            pass
    return user_dict
    


def write_to_file(path,img_url):
    r = requests.get(url=img_url)
    if r.status_code == 200:
        with open("/tmp/test/{}/{}".format(path,(str(time.time())+".jpg")),'wb') as f:
            f.write(r.content)
            print('{}写入完成'.format(img_url))
    else:
        print("下载失败：",r.text)
    pass




if __name__ == "__main__":

    # page_lenth定义爬取多少页  thread_lenth定义线程数
    page_lenth = 20
    thread_lenth = 200

    start_time = time.time()
    with ThreadPoolExecutor(max_workers=thread_lenth) as f:

        thread_pool = [ f.submit(get_response,x) for x in range(page_lenth)]
        for x in as_completed(thread_pool):
            img_lists = make_user_directory(x.result())     # 获取抓取接口获得的img字典


            img_pool = []
            for user_name,img_list in img_lists.items():
                for img_url in img_list:
                    img_pool.append(f.submit(write_to_file,user_name,img_url))
            for z in as_completed(img_pool):
                # print("/tmp/test/{}写入完成".format(z.result()))
                pass



    # wait(img_pool)
    print("耗时为：{}".format((time.time()-start_time)))

