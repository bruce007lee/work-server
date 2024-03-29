from flask import Flask, request
from PIL import Image
from controller import api, main

app = Flask(__name__)

app.register_blueprint(main.app)
app.register_blueprint(api.app)

app.run(host="0.0.0.0", port=5001)
