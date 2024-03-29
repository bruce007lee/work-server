from paddleocr import PaddleOCR, draw_ocr
from PIL import Image
import json

def recognize(img):
    ocr = PaddleOCR(use_angle_cls=True, lang="ch")
    result = ocr.ocr(img, cls=True)
    return json.dumps(result)
