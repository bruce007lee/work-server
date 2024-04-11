from paddleocr import PaddleOCR

def recognize(img, lang="ch"):
    ocr = PaddleOCR(use_angle_cls=True, lang=lang, use_gpu=True, show_log=False, det_db_unclip_ratio=2.1)
    return ocr.ocr(img, cls=True)
