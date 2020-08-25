import base64
# from urlparse import urlparse

miwen = 'fR4aHWwuFCYYVydFRxMqHhhCKBseH1dbFygrRxIWJ1UYFhotFjA='

miwen = base64.b64decode(miwen)
# miwen1 = '}\\x1e\\x1a\\x1dl.\\x14&\\x18W\'EG\x13*\\x1e\\x18B(\\x1b\\x1e\\x1fW[\\x17(+G\\x12\\x16\'U\\x18\\x16\\x1a-\\x160'

# miwen1 = urlparse(miwen1)
# miwen1 = miwen1.replace('\\x','%')
# print(miwen1)
# miwen1 = miwen.decode('utf-8')
print(miwen.decode('utf-8'))