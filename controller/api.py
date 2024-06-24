from PIL import Image
import numpy as np
from io import BytesIO
from service import image as imageService, ocr as ocrService
from utils.logger import logger
from fastapi import APIRouter, UploadFile

router = APIRouter()

@router.post("/api/ocr")
async def ocr(file: UploadFile, lang: str = "ch"):
    """
    文字识别接口
    """
    try:
        content = await file.read()
        io = BytesIO(content)
        image = Image.open(io)
        data = ocrService.recognize(img=np.array(image), lang=lang)
        return {"success": True, "data": data[0]}
    except Exception as e:
        logger.error("OCR recognize error: %s", e)
        return {"success": False, "errorMessage": "Recognize error"}


@router.post("/api/recognizeImageColor")
async def recognizeImageColor(file: UploadFile):
    """
    图像颜色识别
    """
    try:
        content = await file.read()
        io = BytesIO(content)
        img = Image.open(io)
        data = imageService.recognizeImageColor(img)
        return {"success": True, "data": data}
    except Exception as e:
        logger.error("RecognizeImageColor error: %s", e)
        return {"success": False, "errorMessage": "Recognize error"}
