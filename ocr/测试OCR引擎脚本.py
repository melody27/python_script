import pytesseract
from PIL import Image


image=Image.open('D:\百度云下载\oxcode.png')
text=pytesseract.image_to_string(image)
print(text)
