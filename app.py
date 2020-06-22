from flask import Flask
# from flask_restful import Resource, Api

app = Flask(__name__)
# api = Api(app)

@app.route('/<string:name>')
def hello(name):
    return "hello %s" %name

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
