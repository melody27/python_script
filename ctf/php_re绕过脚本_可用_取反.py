import re


# php_re绕过脚本_可用_取反绕过 


len_1 = 0xff
start_str = input("输入")

print(len(start_str))
result = ''

for x in start_str:
    
    # print('开始')
    
    last = 0
    zi_len = ord(x)
    last = 255-zi_len
    result += hex(last)
    # print(result)

print(" The Result is :\n")
print(result.replace('0x','%'))