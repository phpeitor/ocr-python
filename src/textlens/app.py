import streamlit as st
from PIL import Image

from .analysis import (
    DEFAULT_NEGATIVE_KEYWORDS,
    DEFAULT_POSITIVE_KEYWORDS,
    find_dates,
    find_documents,
    parse_keywords,
    keyword_summary,
    summarize_documents,
)
from .config import settings
from .ocr import extract_text
from .ui import apply_styles, render_feature_cards, render_header, render_text_output


def render_sentiment(count: int, percentage: float, words: list[str], kind: str) -> None:
    if count == 0:
        st.warning(f"No se encontraron palabras {kind}")
        return
    (st.success if kind == "positivas" else st.error)(f"Palabras {kind}")
    st.write(f"{count} palabra(s) representan {percentage:.2f}% del texto")
    st.write(f"Palabras encontradas: {', '.join(words)}")


def render_analysis(text: str, positive_keywords: set[str], negative_keywords: set[str]) -> None:
    documents = find_documents(text)
    dates = find_dates(text)
    positive = keyword_summary(text, positive_keywords)
    negative = keyword_summary(text, negative_keywords)

    st.divider()
    st.subheader("Resumen del analisis")
    metric_a, metric_b, metric_c, metric_d = st.columns(4)
    metric_a.metric("DNI", len(documents))
    metric_b.metric("Fechas", len(dates))
    metric_c.metric("Palabras positivas", positive[0], f"{positive[1]:.2f}%")
    metric_d.metric("Palabras negativas", negative[0], f"{negative[1]:.2f}%")

    result_a, result_b = st.columns(2, gap="large")
    with result_a:
        if documents:
            st.success("DNI encontrado(s):")
            st.markdown(summarize_documents(documents), unsafe_allow_html=True)
        else:
            st.warning("No se encontro ningun DNI")
        if dates:
            st.info(f"Fechas encontradas: {', '.join(dates)}")
        else:
            st.info("No se encontraron fechas")
    with result_b:
        render_sentiment(*positive, "positivas")
        render_sentiment(*negative, "negativas")


def reset_keyword_editor() -> None:
    st.session_state.positive_keywords_text = "\n".join(DEFAULT_POSITIVE_KEYWORDS)
    st.session_state.negative_keywords_text = "\n".join(DEFAULT_NEGATIVE_KEYWORDS)


def render_keyword_editor() -> tuple[set[str], set[str]]:
    if "positive_keywords_text" not in st.session_state:
        st.session_state.positive_keywords_text = "\n".join(DEFAULT_POSITIVE_KEYWORDS)
    if "negative_keywords_text" not in st.session_state:
        st.session_state.negative_keywords_text = "\n".join(DEFAULT_NEGATIVE_KEYWORDS)

    with st.sidebar.expander("Diccionario OCR", expanded=True):
        st.caption("Una palabra o símbolo por línea")
        st.text_area(
            "Palabras buenas",
            key="positive_keywords_text",
            height=150,
            help="Se buscarán como coincidencias positivas en el texto detectado.",
        )
        st.text_area(
            "Palabras malas",
            key="negative_keywords_text",
            height=120,
            help="Se buscarán como coincidencias negativas en el texto detectado.",
        )
        st.button(
            "Restaurar palabras iniciales",
            use_container_width=True,
            on_click=reset_keyword_editor,
        )

    return (
        parse_keywords(st.session_state.positive_keywords_text),
        parse_keywords(st.session_state.negative_keywords_text),
    )


def main() -> None:
    st.set_page_config(
        page_title=settings.app_name,
        page_icon=settings.page_icon,
        layout="wide",
    )
    apply_styles()
    render_header()
    render_feature_cards()

    st.sidebar.title(settings.app_name)
    st.sidebar.caption("Panel de analisis OCR")
    analyze = st.sidebar.toggle("Analizar contenido", value=True)
    positive_keywords, negative_keywords = render_keyword_editor()

    left_column, right_column = st.columns([0.95, 1.25], gap="large")
    with left_column:
        st.subheader("Carga tu imagen")
        upload = st.file_uploader(
            "Seleccione imagen",
            type=["png", "jpg", "jpeg"],
            max_upload_size=settings.max_upload_size_mb,
        )
        if not upload:
            st.info("Sube una imagen para comenzar el análisis")
            return
        image = Image.open(upload)
        st.image(image, caption="Vista previa", use_container_width=True)

    with right_column:
        st.subheader("Texto detectado")
        with st.spinner("Extrayendo texto con Tesseract..."):
            text = extract_text(image)
        render_text_output(text)
        st.download_button(
            "Descargar texto",
            text,
            file_name="textlens-ocr.txt",
            mime="text/plain",
            disabled=not bool(text.strip()),
        )

    if analyze:
        render_analysis(text, positive_keywords, negative_keywords)


if __name__ == "__main__":
    main()
