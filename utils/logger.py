import logging
import os

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logPath = "logs"
if not os.path.exists(logPath):
    os.makedirs(logPath)
handler = logging.FileHandler(logPath + "/app.log")
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)
