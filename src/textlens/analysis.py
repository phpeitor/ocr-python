import re
from html import escape


DEFAULT_POSITIVE_KEYWORDS = (
    "AMAR",
    "PERRO",
    "PERU",
    "GANADOR",
    "S/",
    "$",
    "YAPE",
    "ACEPTO",
)
DEFAULT_NEGATIVE_KEYWORDS = (
    "ODIO",
    "IA",
    "PERDEDOR",
    "ESTAFA",
)


def find_documents(text: str) -> list[str]:
    return re.findall(r"\b\d{8}\b", text)


def find_dates(text: str) -> list[str]:
    return re.findall(r"\b\d{2}/\d{2}/\d{4}\b", text)


def parse_keywords(value: str) -> set[str]:
    return {line.strip().upper() for line in value.splitlines() if line.strip()}


def extract_tokens(text: str) -> list[str]:
    words = re.findall(r"[A-ZÁÉÍÓÚÜÑ0-9]+", text.upper())
    symbols = re.findall(r"S/|\$", text.upper())
    return words + symbols


def keyword_summary(text: str, keywords: set[str]) -> tuple[int, float, list[str]]:
    tokens = extract_tokens(text)
    found = [token for token in tokens if token in keywords]
    percentage = (len(found) / len(tokens) * 100) if tokens else 0
    return len(found), percentage, found


def summarize_documents(documents: list[str]) -> str:
    return "<br>".join(escape(document) for document in documents)
