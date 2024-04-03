from PIL import Image
import numpy as np
from io import BytesIO
from service import ocr as ocrService
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
        logger.error("Recognize error: %s", e)
        return {"success": False, "errorMessage": "Recognize error"}
