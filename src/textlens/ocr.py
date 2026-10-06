from PIL import Image
import pytesseract

from .config import settings


def configure_tesseract() -> None:
    """Configure an explicit Tesseract executable when one is provided."""
    if settings.tesseract_cmd:
        pytesseract.pytesseract.tesseract_cmd = settings.tesseract_cmd


def extract_text(image: Image.Image) -> str:
    configure_tesseract()
    options = {"lang": settings.ocr_language} if settings.ocr_language else {}
    return pytesseract.image_to_string(image, **options)
