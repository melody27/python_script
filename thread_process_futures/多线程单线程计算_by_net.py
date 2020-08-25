#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by vellhe 2017/7/1

from multiprocessing.pool import ThreadPool
from multiprocessing.dummy import Pool as DummyPool
from multiprocessing import Pool as ProcessPool

import time

max_range = 10000000

# 网上认的测试代码

def run(i):
    i = i * i
    # return i # return和不return对进程池运行速度会有比较大影响，不return效率更高


def thread_pool(num):
    p = ThreadPool(num)
    start_time = time.time()
    ret = p.map(run, range(max_range))
    p.close()
    p.join()
    print("thread_pool  %d, costTime: %fs ret.size: %d" % (num, (time.time() - start_time), len(ret)))


def dummy_pool(num):
    p = DummyPool(num)
    start_time = time.time()
    ret = p.map(run, range(max_range))
    p.close()
    p.join()
    print("dummy_pool   %d, costTime: %fs ret.size: %d" % (num, (time.time() - start_time), len(ret)))


def process_pool(num):
    p = ProcessPool(num)
    start_time = time.time()
    ret = p.map(run, range(max_range))
    p.close()
    p.join()
    print("process_pool %d, costTime: %fs ret.size: %d" % (num, (time.time() - start_time), len(ret)))


if __name__ == "__main__":
    for i in range(1, 9):
        thread_pool(i)
        dummy_pool(i)
        process_pool(i)
        print("=====")


# 纯运算情况下单线程比多线程更快
# 多线程在IO操作较多情况下才能很好的发挥作用，但效率还是低于多进程
# 单进程运行比单线程慢，但当多进程数够多情况下会超越单线程的速度
# 多进程比单进程运行快
# 对于多进程而言，有return会比没有return慢很多很多，对于多线程却只会慢一点点
# 【疑惑】不管开多少个进程或者线程，各个核占用情况几乎是均匀的，猜测是系统底层有优化
