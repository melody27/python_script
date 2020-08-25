from test_11 import favicon


data = favicon('http://www.bilibili.com/favicon.ico')
data.get_hash()
print(data.hash)
