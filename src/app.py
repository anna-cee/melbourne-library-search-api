from flask import Flask

app = Flask(__name__)

message = 'Hello, world!'

@app.route('/')
def index():
    return ('test is okay, 201')

if __name__ == '__main__':
    app.run(debug=True, port=5000)