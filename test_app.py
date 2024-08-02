from flask import Flask

app = Flask(__name__)

@app.before_first_request
def before_first_request_func():
    print("Before first request")

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
