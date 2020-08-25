# 生成器 （by周杰）
import time

def f():
    for i in range(10):
        print("yield 上面")
        yield i
        print("yield 下面")
        time.sleep(0.5)


x = f()

print(next(x))
print("*" * 10)
print(next(x))
print("*" * 10)
print(next(x))