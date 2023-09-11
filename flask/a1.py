# 从flask这个包中 导入Flask这个类
from flask import Flask

# 使用Flask类实例化一个app对象
# __name__ :代表当前py文件模块
# 1、出现Bug后可以帮助快速定位
# 2、对于寻找模版文件，有一个相对路径
app = Flask(__name__)



# 创建一个路由和一个视图函数的映射
@app.route('/')  # 根路由
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()

