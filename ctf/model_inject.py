from flask import Flask

x = ''
t = 0
# print(x.__class__)
# with open('class.txt','w') as f:
#     for y in x.__class__.__mro__[1].__subclasses__():
#         print(t,y)
#         f.write(str(t))
#         f.write(str(y))
#         f.write("\n")
#         t+=1
#     # print(f.__class__)

for a in x.__class__.__mro__[1].__subclasses__():
    try:
        if 'os' in a.__init__.__globals__:
            print(t,a)
    except Exception as identifier:
        pass
    # print('-')
    t+=1
