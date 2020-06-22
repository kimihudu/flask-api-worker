from flask import Flask

app = Flask(__name__)

@app.route('/<string:name>')
def hello(name):
    return "hello %s" %name