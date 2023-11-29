from flask import url_for,Flask,render_template

app = Flask(__name__)

@app.route("/hello/")
@app.route('/hello/<name>')
def index(name=None):
    return render_template("hello.html",name = name)

@app.route('/login')
def login():
    return 'login'



@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'



if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080,debug=True)

