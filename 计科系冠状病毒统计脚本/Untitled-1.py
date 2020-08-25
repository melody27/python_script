import requests,re

s=requests.Session()

url = "http://lab1.xseclab.com/xss2_0d557e6d2a4ac08b749b61473a075be1/index.php"
jisuan = s.get(url)
jisuan.encoding="UTF-8"
text = str(jisuan.content)
# print(text)

re1=re.findall(r'\d{4}.*\)',text)
print(eval(re1[0]))

payload = {'v':eval(re1[0])}
x = s.post(url,data=payload)
x.encoding="utf-8"
print(x.text)





# f= open('tt.text','w',encoding="utf-8")
# f.write(jisuan.text)
# f.write("1111")
# f.close