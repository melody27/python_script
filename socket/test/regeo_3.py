import requests

url = "http://192.168.2.82/connect.php"
headers = {"X-CMD":"CONNECT","X-TARGET":'www.baidu.com',"X-PORT":'80'}
r = requests.post(url=url,headers=headers)
print(r.headers)