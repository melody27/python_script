from flask import url_for,Flask,render_template,request
from model.long import * 
from model.chain import Chain
import pickle

app = Flask(__name__)


@app.route('/test/')
@app.route('/test/<username>')
def login(username=None):
    if username == None:
        return render_template("index.html",name = "world")
    return render_template("index.html",name=username)



# 定义model的测试接口               
# 接口 正常
@app.route('/registe',methods = ["GET","POST"])
def registe():
    if request.method == "GET":
        return render_template("registe.html")
    elif request.method == "POST":
        type = request.form['type']
        name = request.form['name']
        summary = request.form['summary']
        desc = request.form['desc']
        deadline = request.form['deadline']
        important = request.form['important']
        emergent = request.form['emergent']
        processing = request.form['processing']
        status = request.form['status']
        priority = request.form['priority']

        l1 = Long_im_not(name,summary,desc,deadline,important,emergent,processing,status,priority)
        with open('./database/'+type, 'rb') as file:
            c1 = pickle.load(file)
        
        c1.append()   # to here
        with open('./database/'+type, 'wb') as file:
            pickle.dump(c1, file)
        return "你注册成功啦"
    print(l1)
        



if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080,debug=True)

