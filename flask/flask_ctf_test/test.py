from flask import Flask
from flask import redirect,render_template,render_template_string,session
from flask import request

app = Flask(__name__)

url_prefix = '/test'

@app.route('/flask',methods=['GET'])
def index():
    return render_template_string('this is a flask')



if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=80)