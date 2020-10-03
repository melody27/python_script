import logging
logging.getLogger("scapy").setLevel(logging.CRITICAL)


# 官网的日志demo，实际上应该使用的是logging模块。
# 上面的代码中，实际上只设置了日志级别。并没有具体的输出日志。