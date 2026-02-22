from flask import Flask

app = Flask(__name__)

# Ye aapka normal application code hai
@app.route("/")
def home():
    return "Hello World"