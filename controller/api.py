from flask import Blueprint, request
from PIL import Image
import numpy as np
from service import ocr as ocrService
from utils.logger import logger

app = Blueprint("api", __name__)


@app.route("/ocr", methods=["POST"])
def ocr():
    """
    文字识别接口
    """
    try:
        file = request.files["file"]
        lang = request.form["lang"]
        image = Image.open(file)
        data = ocrService.recognize(img=np.array(image), lang=lang)
        return {"success": True, "data": data}
    except:
        logger.error("Recognize error [%s]", file.filename)
        return {"success": False, "errorMessage": "Recognize error"}
