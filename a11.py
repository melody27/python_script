import random

def jisuan(times):
    print("开始")
    result = []
    num = 0
    for x in range(times):
        result.append(random.randrange(0,11))
    for x in result:
        num += x
    print(num/times)

if __name__ == "__main__":
    jisuan(1000)