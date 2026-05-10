import streamlit as st
from html import escape


APP_NAME = "TextLens"


def apply_styles():
    st.markdown(
        """
        <style>
        .stApp {
            background:
                radial-gradient(circle at top left, rgba(88, 166, 255, 0.20), transparent 34rem),
                linear-gradient(135deg, #07111f 0%, #111827 48%, #172033 100%);
            color: #e5edf7;
        }

        [data-testid="stHeader"] {
            background: transparent;
        }

        [data-testid="stSidebar"] {
            background: rgba(8, 13, 25, 0.88);
            border-right: 1px solid rgba(148, 163, 184, 0.16);
        }

        .block-container {
            max-width: 1120px;
            padding-top: 2.5rem;
        }

        .hero {
            padding: 2rem;
            border: 1px solid rgba(148, 163, 184, 0.20);
            border-radius: 28px;
            background: linear-gradient(135deg, rgba(15, 23, 42, 0.94), rgba(30, 41, 59, 0.72));
            box-shadow: 0 24px 80px rgba(2, 6, 23, 0.35);
            margin-bottom: 1.5rem;
        }

        .eyebrow {
            display: inline-flex;
            padding: 0.35rem 0.75rem;
            border-radius: 999px;
            background: rgba(56, 189, 248, 0.12);
            color: #7dd3fc;
            font-size: 0.78rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            margin-bottom: 0.9rem;
        }

        .hero h1 {
            color: #f8fafc;
            font-size: clamp(2.4rem, 6vw, 4.7rem);
            line-height: 0.95;
            margin: 0;
        }

        .hero p {
            color: #cbd5e1;
            font-size: 1.08rem;
            max-width: 720px;
            margin-top: 1rem;
        }

        h1, h2, h3, h4,
        div[data-testid="stMarkdownContainer"] h1,
        div[data-testid="stMarkdownContainer"] h2,
        div[data-testid="stMarkdownContainer"] h3 {
            color: #f8fafc !important;
        }

        label,
        div[data-testid="stWidgetLabel"],
        div[data-testid="stWidgetLabel"] p {
            color: #cbd5e1 !important;
        }

        .feature-grid {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 1rem;
            margin: 1.5rem 0;
        }

        .feature-card, .result-card {
            border: 1px solid rgba(148, 163, 184, 0.18);
            border-radius: 22px;
            background: rgba(15, 23, 42, 0.74);
            padding: 1.1rem;
        }

        .feature-card strong, .result-card strong {
            color: #f8fafc;
            display: block;
            margin-bottom: 0.3rem;
        }

        .feature-card span, .result-card span {
            color: #94a3b8;
            font-size: 0.94rem;
        }

        .text-output {
            border-left: 4px solid #38bdf8;
            border-radius: 18px;
            background: rgba(2, 6, 23, 0.42);
            padding: 1rem 1.2rem;
            color: #dbeafe;
            white-space: pre-wrap;
        }

        div[data-testid="stFileUploader"] section {
            border: 1px dashed rgba(125, 211, 252, 0.55);
            border-radius: 22px;
            background: rgba(14, 165, 233, 0.08);
        }

        div[data-testid="stFileUploader"] section:hover {
            border-color: #38bdf8;
            background: rgba(14, 165, 233, 0.14);
        }

        button,
        button[kind="primary"],
        button[kind="secondary"],
        .stButton > button,
        .stDownloadButton > button,
        div.stButton > button,
        div.stDownloadButton > button,
        div[data-testid="baseButton-secondary"],
        div[data-testid="stFileUploader"] button,
        div[data-testid="stFileUploader"] section button,
        div[data-testid="stDownloadButton"] button {
            border: 0 !important;
            border-radius: 999px !important;
            background: linear-gradient(135deg, #38bdf8 0%, #2563eb 100%) !important;
            color: #ffffff !important;
            font-weight: 700 !important;
            letter-spacing: 0.01em;
            box-shadow: 0 12px 28px rgba(37, 99, 235, 0.28) !important;
            transition: transform 160ms ease, box-shadow 160ms ease, filter 160ms ease;
        }

        button:hover,
        button[kind="primary"]:hover,
        button[kind="secondary"]:hover,
        .stButton > button:hover,
        .stDownloadButton > button:hover,
        div.stButton > button:hover,
        div.stDownloadButton > button:hover,
        div[data-testid="baseButton-secondary"]:hover,
        div[data-testid="stFileUploader"] button:hover,
        div[data-testid="stFileUploader"] section button:hover,
        div[data-testid="stDownloadButton"] button:hover {
            color: #ffffff !important;
            filter: brightness(1.08);
            transform: translateY(-1px);
            box-shadow: 0 16px 34px rgba(37, 99, 235, 0.38) !important;
        }

        button p,
        button span,
        .stButton button p,
        .stButton button span,
        .stDownloadButton button p,
        .stDownloadButton button span,
        div[data-testid="stFileUploader"] button p,
        div[data-testid="stFileUploader"] button span,
        div[data-testid="stDownloadButton"] button p,
        div[data-testid="stDownloadButton"] button span {
            color: #ffffff !important;
            font-weight: 700 !important;
        }

        button:disabled,
        .stButton > button:disabled,
        .stDownloadButton > button:disabled,
        div[data-testid="stDownloadButton"] button:disabled,
        div.stButton > button:disabled {
            background: rgba(71, 85, 105, 0.72) !important;
            color: rgba(226, 232, 240, 0.70) !important;
            box-shadow: none !important;
            transform: none;
        }

        div[data-testid="stFileUploader"] small,
        div[data-testid="stFileUploader"] p,
        div[data-testid="stFileUploader"] span {
            color: #cbd5e1 !important;
        }

        div[data-testid="stMetric"] {
            border: 1px solid rgba(148, 163, 184, 0.18);
            border-radius: 18px;
            background: rgba(15, 23, 42, 0.58);
            padding: 1rem;
        }

        @media (max-width: 760px) {
            .feature-grid {
                grid-template-columns: 1fr;
            }

            .hero {
                padding: 1.4rem;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


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
