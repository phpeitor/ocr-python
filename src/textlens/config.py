from dataclasses import dataclass
import os
from pathlib import Path

from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parents[2]
PACKAGE_ROOT = Path(__file__).resolve().parent
load_dotenv(PROJECT_ROOT / ".env")


@dataclass(frozen=True)
class Settings:
    app_name: str = os.getenv("APP_NAME", "TextLens")
    page_icon: str = os.getenv("APP_PAGE_ICON", "🔎")
    ocr_language: str | None = os.getenv("OCR_LANGUAGE") or None
    tesseract_cmd: str | None = os.getenv("TESSERACT_CMD") or None
    max_upload_size_mb: int = int(os.getenv("MAX_UPLOAD_SIZE_MB", "5"))


settings = Settings()
