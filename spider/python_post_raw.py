import requests

# python实现post数据包。也可以使用dict而不是string的方式来进行传递数据。也可以使用打开文件的方式，也可以使用json的方式
# 稍微需要注意的是请求头中的"Content-Type"值


url = 'http://192.168.2.138/index.php'

headers = {
    "Content-Type": "multipart/form-data; boundary=---------------------------160527832215434079761148429759",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36", 
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",  
    "Connection": "close"
    }

data = """-----------------------------160527832215434079761148429759
Content-Disposition: form-data; name="file1"; filename="phpinfo.ph1p"
Content-Type: application/x-php

<?php 
	phpinfo();
?>

-----------------------------160527832215434079761148429759--
"""

r = requests.post(url=url,headers=headers,data=data)

print(r.text)