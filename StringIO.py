'''
from io import StringIO
f=StringIO()
f.write('jisuan')
f.write('yijia')
f.write('er')
print(f.getvalue())
print('---'*10)
o=StringIO('jikexi\nzhangxiangke')
d=o.read()
print(d)
'''

'''
from io import BytesIO
f=BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
d=BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(d.read())
'''
from io import StringIO
s=StringIO()
s.write('jiluyiqie')
print(s.getvalue())
print('---'*10)
e=StringIO('jiluyiqie')
a=e.read()
print(a)

print('+++'*10)
from io import BytesIO
f=BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
print('***'*10)

d=BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
c=d.read()
print(c)