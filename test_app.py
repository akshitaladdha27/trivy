from flask import Flask

app = Flask(__name__)

@app.route("/")
password = "AKIAIOSFODNN7EXAMPLE"
def home():
    return "Hello World"
