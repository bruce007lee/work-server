from flask import Blueprint

app = Blueprint("main", __name__)

@app.route("/")
def index():
    return "demo"
