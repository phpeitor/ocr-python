import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = None


if load_dotenv:
    load_dotenv(BASE_DIR / ".env")


APP_NAME = os.getenv("APP_NAME", "TextLens")
APP_PAGE_ICON = os.getenv("APP_PAGE_ICON", "🔎")
OCR_LANGUAGE = os.getenv("OCR_LANGUAGE") or None
TESSERACT_CMD = os.getenv("TESSERACT_CMD") or None


def get_ocr_options():
    if OCR_LANGUAGE:
        return {"lang": OCR_LANGUAGE}

    return {}
