from flask import Flask
from flask import render_template,url_for,render_template_string,redirect
from flask import request
import os,sys
import pymmh3
import requests
import base64
import re


app = Flask(__name__)


@app.route('/pwd/')
def index():
    return os.getcwd()

@app.route('/hello')
def hello():
    name = request.args.get('name')
    return render_template('index.html',content = name)

#正常代码
# @app.route('/test')
# def test_string():
#     name = request.args.get('name')
#     html = """
#     <h1>this is a new life from flask</h1>
#     <h2> hello {{ name }}~</h2>
#     """
#     return render_template_string(html,name=name)

@app.route('/test')
def test_string():
    name = request.args.get('name')
    html = """
    <h1>this is a new life from flask</h1>
    <h2> hello {0}~</h2>
    """.format(name)
    return render_template_string(html)

@app.route('/')
def souye():
    index_1 = '''
    there is a melody space index page

    you can find certain tools that you want to 

    there is a first tools <a href=./ShadonFaviconHash>计算shodan图标hash</a>
    '''
    return render_template_string(index_1)

def change_format(content):
    count = len(content) % 76
    items = re.findall(r".{76}", content)
    final_item = content[-count:]
    items.append(final_item)
    return "{0}\n".format("\n".join(items))

@app.route('/ShadonFaviconHash',methods=['POST','GET'])
def ShadonFaviconHash():
    

    arg = request.form.get('faviconUrl',type=str,default=None)
    
    if arg :
        response = requests.get(arg)
        if response.headers['Content-Type'] == "image/x-icon":
            favicon = base64.b64encode(response.content).decode('utf-8')
            hash = pymmh3.hash(change_format(favicon))
            result = '''
                其结果为：{}
            '''.format(hash)
            return render_template_string(result)


    else:
        return '''
            请输入你要查询的参数：
            <form method='post' action=''>
                <input type="text" name='faviconUrl' value="http://www.baidu.com/favicon.ico">
                <input type="submit" value="提交">
            </form>
        '''








if __name__ == "__main__":

    app.run(host='0.0.0.0',port=5000,debug=True)