import base64 
from urllib.parse import quote

def rc4_main(key,message):
    secret = rc4_sandbox(key)           # 进行第一次的混乱
    # print("混乱后的S盒为：",secret)

    cipher_text = rc4_encrypt(secret,message)



def rc4_sandbox(key):

    sand_boxs = [x for x in range(256)]         # 原始盒
    # print(sand_box)

    j = 0
    for i in range(256):                            # 实际上此处有一个T盒，T盒为一个长度256的list，其中每个值都只是一个字符。实际上就算取出key中的每个字符进行的填充。如果key长度不够的话，就反复循环填充直到长度为256为止
        j = ( j + sand_boxs[i] + ord(key[i % len(key)]) ) % 256     # j的值等于    上一次j的值    sand_boxs从0开始的索引值    T盒中从索引0开始的值 的ascii十进制值      (ps.使用上一次的j值和S盒，T盒进行混淆)
        sand_boxs[i],sand_boxs[j] = sand_boxs[j],sand_boxs[i]       # 进行S盒的混乱作业
    return sand_boxs                                                # 返回混乱后的S盒


def rc4_encrypt(key,message):

    results = []
    i = j =0
    for x in message:
        i = ( i + 1 ) % 256
        j = ( j + key[i] ) % 256

        key[i],key[j] = key[j],key[i]

        k = ( key[i] + key[j] ) % 256
        z = key[k]
        l = chr(ord(x) ^ z)
        results.append(l)

    result = "".join(results)
    print("得出的结果为：",quote(result))
    return result




if __name__ == "__main__":



    message = 'this is a message'
    rc4_main('secret',message)