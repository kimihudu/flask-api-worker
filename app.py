from flask import Flask
from datetime import datetime
# from flask_restful import Resource, Api

app = Flask(__name__)
# api = Api(app)
@app.route('/')
def hello():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

@app.route('/<string:name>')
def helloName(name):
    return "hello %s" %name


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
