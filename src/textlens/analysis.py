import re
from html import escape
from pathlib import Path


DATA_DIR = Path(__file__).resolve().parent / "data"


def find_documents(text: str) -> list[str]:
    return re.findall(r"\b\d{8}\b", text)


def find_dates(text: str) -> list[str]:
    return re.findall(r"\b\d{2}/\d{2}/\d{4}\b", text)


def load_keywords(filename: str) -> set[str]:
    path = DATA_DIR / filename
    return {
        line.strip().upper()
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    }


def extract_tokens(text: str) -> list[str]:
    words = re.findall(r"[A-ZÁÉÍÓÚÜÑ0-9]+", text.upper())
    symbols = re.findall(r"S/|\$", text.upper())
    return words + symbols


def keyword_summary(text: str, filename: str) -> tuple[int, float, list[str]]:
    tokens = extract_tokens(text)
    found = [token for token in tokens if token in load_keywords(filename)]
    percentage = (len(found) / len(tokens) * 100) if tokens else 0
    return len(found), percentage, found


def summarize_documents(documents: list[str]) -> str:
    return "<br>".join(escape(document) for document in documents)
