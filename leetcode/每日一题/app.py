from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/hello", methods=['POST'])
def hello_world():
    return "hello,world"


@app.route("/login", methods=['POST'])
def login():
    data = request.json
    print(data)
    username = data.get("username")
    password = data.get("password")
    if 'shy' == username and 'shy' == password:
        return jsonify({'message': '%s login successfully!' % username})
    else:
        return jsonify({'ERROR': '%s login failed!' % username})
