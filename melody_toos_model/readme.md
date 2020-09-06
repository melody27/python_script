
#此处对python的打包参靠：
https://www.cnblogs.com/Yemilice/p/10529720.html        # 主要参考
https://www.cnblogs.com/mangM/p/11619247.html           # 次要参考，较复杂

#以及简单的模块打包：
https://blog.csdn.net/qq_40771567/article/details/88990830



#打包示例：
python3 setup.py sdist

安装：
pip3 install tools-1.2.1.tar.gz


导入：
from tools.faviconhash import favicon

使用：
from tools.faviconhash import favicon

a = favicon('http://www.baidu.com/favicon.ico')
print(a)


或者：
需要先安装包
pip3 install tools-1.2.2.tar.gz

然后
python3 faviconhash.py http://www.baidu.com/favicon.ico
