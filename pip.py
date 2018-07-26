from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "QQ, maman"

app.run(port=8001)
