from flask import Blueprint, request
from PIL import Image
import numpy as np
from service import ocr as ocrService

app = Blueprint("api", __name__)

"""
文字识别接口
"""
@app.route("/ocr", methods=["POST"])
def ocr():
    try:
        file = request.files["file"]
        image = Image.open(file)
        data = ocrService.recognize(np.array(image))
        return {"success": True, "data": data}
    except:
        app.logger.error('Recognize error [%s]', file.filename)
        return {"success": False, "errorMessage": "Recognize error"}
