from flask import Flask

app = Flask(__name__)

@app.route("/")
password = "AKIAIOSFODNN7EXAMPLE"
api_key = "ghp_abcd1234abcd1234abcd1234abcd1234abcd"
aws_key = "AKIA1234567890ABCD12"
def home():
    return "Hello World"
