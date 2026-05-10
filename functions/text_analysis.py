import re
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def buscar_palabras(texto, archivo):
    palabras_clave = cargar_palabras(archivo)
    tokens = extraer_tokens(texto)
    encontradas = [token for token in tokens if token in palabras_clave]
    percentual = calcula_percentual(len(encontradas), len(tokens))
    return len(encontradas), percentual, encontradas


def cargar_palabras(archivo):
    ruta = BASE_DIR / archivo
    with open(ruta, encoding="utf-8") as f:
        return {linea.strip().upper() for linea in f if linea.strip()}


def extraer_tokens(texto):
    texto = texto.upper()
    palabras = re.findall(r"[A-ZÁÉÍÓÚÜÑ0-9]+", texto)
    simbolos = re.findall(r"S/|\$", texto)
    return palabras + simbolos


def calcula_percentual(quantidade, tamanho):
    if tamanho > 0:
        return (quantidade / tamanho) * 100

    return 0
