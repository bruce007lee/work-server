from flask import Blueprint, request
from PIL import Image
import numpy as np
from service import ocr as ocrService

app = Blueprint('api', __name__)

@app.route('/ocr', methods=['GET', 'POST'])
def ocr():
    file = request.files['file']
    image = Image.open(file)
    data = ocrService.recognize(np.array(image))
    return data