from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def hello_world():
    response = jsonify(        
        message="Hello world!"        
    )
    return response