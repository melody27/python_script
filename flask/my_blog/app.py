# coding:utf-8
from flask import Flask
from flask import render_template,url_for,render_template_string,redirect
from flask import request
import os,sys
import pymmh3
import requests
import base64
import re
from tools.faviconhash import favicon
from flask import Response,make_response
import pymysql
import time
import datetime

conn=pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='root',
                     #database='test',
                     charset='utf8')

app = Flask(__name__,static_folder="static/")





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
    test_cookie = request.cookies.get('name',default=None)
    name = request.args.get('name')
    name = re.sub(r'[{}]','',name)
    html = """
    <h1>this is a new life from flask</h1>
    <h2> hello {0}~</h2>

    oh there is not SSTI
    """.format(name)

    #此处测试flask的getcookie
    if test_cookie:
        # return render_template_string(test_cookie)
        return render_template_string(html+test_cookie)

    
    return render_template_string(html)

@app.route('/')
def souye():


    day = 'welcome'
    index_1 = render_template('index.html',page=day)

    #此处测试flask使用set_cookie
    # reg = make_response(index_1)
    reg = Response(index_1)
    reg.set_cookie('name','melody')

    return reg


@app.route('/ShadonFaviconHash',methods=['POST','GET'])
def ShadonFaviconHash():
    

    arg = request.form.get('faviconUrl',type=str,default=None)
    
    if arg :
        data = favicon(arg)
        data.get_hash()
        result = '''
            其结果为：{}
            使用示例：
                shodan框输入如下：http.favicon.hash:{}
            '''.format(data.hash,data.hash)
        return render_template_string(result)


    else:
        return render_template('favicon.html')


@app.route('/study',methods = ['POST','GET'])
def study():
    if 







if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80,debug=True)