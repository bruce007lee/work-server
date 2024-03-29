from paddleocr import PaddleOCR
import json

def recognize(img):
    ocr = PaddleOCR(use_angle_cls=True, lang="ch", use_gpu=True, show_log=False)
    result = ocr.ocr(img, cls=True)
    return json.dumps(result)
