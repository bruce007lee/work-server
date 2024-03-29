import logging
import os

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

os.mkdir('logs')
handler = logging.FileHandler("logs/app.log")
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)