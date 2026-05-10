import streamlit as st
from html import escape
from pathlib import Path


APP_NAME = "TextLens"
ASSETS_DIR = Path(__file__).resolve().parent.parent / "assets"


def apply_styles():
    styles = (ASSETS_DIR / "styles.css").read_text(encoding="utf-8")
    st.markdown(f"<style>{styles}</style>", unsafe_allow_html=True)


def render_header():
    st.markdown(
        f"""
        <section class="hero">
            <div class="eyebrow">OCR inteligente para imagenes</div>
            <h2>{APP_NAME}</h2>
            <p>
                Extrae texto desde imagenes, detecta documentos de identidad y resume
                palabras positivas o negativas dentro del contenido reconocido.
            </p>
        </section>
        """,
        unsafe_allow_html=True,
    )


def render_feature_cards():
    st.markdown(
        """
        <div class="feature-grid">
            <div class="feature-card">
                <strong>1. Carga imagenes</strong>
                <span>Sube PNG, JPG o JPEG con texto visible.</span>
            </div>
            <div class="feature-card">
                <strong>2. Extrae texto</strong>
                <span>Tesseract OCR convierte la imagen en contenido editable.</span>
            </div>
            <div class="feature-card">
                <strong>3. Analiza contenido</strong>
                <span>Encuentra DNI, fechas y palabras relevantes.</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_text_output(texto):
    safe_text = escape(texto.strip() or "No se detecto texto en la imagen.")
    st.markdown(f'<div class="text-output">{safe_text}</div>', unsafe_allow_html=True)
