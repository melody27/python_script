import logging
import random



# python logging模块demo

LOGSTART = '\x1b[{}m'
LOGEND = '\x1b[0m'

# shell中的彩色输出格式为：\x1b[数字m字符串\x1b[数字m           这两个数字为定义颜色的。中间的字符串是要变色的字符串。
#                                                                   后面的\x1n[数字m不加也可，用来规定边界和其他设置
#                     \x1b此为esc的不可打印字符                 示例：\x1b[31m这是红色  
#                                                                   \x1b[30m这是黑色加下划线\x1b[4m


BLACK, RED, GREEN, YELLOW, BLUE, PERPLE, LITTILE_BLUE, WRITE = range(30,38)

logLevel = 'INFO'


COLOR_LIST = {
    'CRITICAL':RED,
    'ERROR':YELLOW,
    'WARNING':LITTILE_BLUE,
    'INFO':PERPLE,
    "DEBUG":GREEN

}

# or random.randomint(1,99)



# 日志格式化类

class FormatLoginger(logging.Formatter):        

    def __init__(self, msg, use_color=True):
        logging.Formatter.__init__(self,msg)        # 此处的msg为调用父类的__init__方法，进行日志格式的定义
        self.use_color = use_color



    def format(self, record):                       # 设置levelname，为彩色输出
        levelname = record.levelname
        
        if self.use_color and levelname in COLOR_LIST:
            result = LOGSTART.format(COLOR_LIST[levelname]) + levelname + LOGEND
            print(result.encode('utf-8'))
        record.levelname = result
        print('输出日志类 名：',record.name)
        return logging.Formatter.format(self, record)


        pass



# 日志类
class ColoredLogger(logging.Logger):

    def __init__(self, name):               # 将日志格式化类接入 日志类中
        logging.Logger.__init__(self, name, logLevel)
        log_format_method = '[ %(levelname)s ] : %(message)s  --date: %(asctime)-18s'   
                                                                # 定义日志格式，此字符串会传入日志格式化类的__init__方法，作为msg来调用
        color_format = FormatLoginger(log_format_method)
        handle = logging.StreamHandler()
        handle.setFormatter(color_format)
        self.addHandler(handle)
        
        return 


logging.setLoggerClass(ColoredLogger)       # 设定调用的日志类为当前的日志类
log = logging.getLogger('melody')           # 获取日志类对象
log.critical('i am error')                  # 弹出高危警告
log.info(' i am info')
log.warning('this is warning')