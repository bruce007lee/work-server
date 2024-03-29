from paddleocr import PaddleOCR
import json


def recognize(img, lang="ch"):
    ocr = PaddleOCR(use_angle_cls=True, lang=lang, use_gpu=True, show_log=False)
    result = ocr.ocr(img, cls=True)
    return json.dumps(result)
