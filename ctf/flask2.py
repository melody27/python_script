from flask import Flask
import json


app = Flask(__name__)

@app.route('/')

def hellow():
    kkp = {'name':'kkp','age':'19','sex':'man'}

    # x = json.loads(kkp)
    return kkp

if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=8889,
        debug=False
    )