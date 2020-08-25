import pymysql

conn = pymysql.connect(
    host = '127.0.0.1',
    user = 'root',
    password = 'root',
    database = 'python_test'
)

cursor = conn.cursor()
a = 'aa\lsa'
b = 'bb'
c = 'cc'

# sql = f'insert into freebuff(id,title,time,content) values(2,{a},{b},{c})'
sql = f'insert into freebuff(title,time,content) values("{a}","{b}","{c}")'

# sql = 'select version()'

cursor.execute(sql)
data = cursor.fetchone()
print(data)
cursor.close()
conn.close()