from flask import Flask
from controller import api, main

app = Flask(__name__)

app.register_blueprint(main.app)
app.register_blueprint(api.app)

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=5001)
