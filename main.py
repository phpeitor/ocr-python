import streamlit as st
from PIL import Image
import pytesseract

import functions.functions as fc
from functions.ui import APP_NAME, apply_styles, render_feature_cards, render_header, render_text_output


class OCR:

    def __init__(self):
        st.set_page_config(page_title=APP_NAME, page_icon="🔎", layout="wide")
        apply_styles()
        self.texto = ""
        self.analisar_texto = False

    def inicial(self):
        render_header()
        render_feature_cards()

        st.sidebar.title(APP_NAME)
        st.sidebar.caption("Panel de analisis OCR")
        self.analisar_texto = st.sidebar.toggle("Analizar contenido", value=True)

        left_column, right_column = st.columns([0.95, 1.25], gap="large")

        with left_column:
            st.subheader("Carga tu imagen")
            imagem = st.file_uploader("Seleccione imagen", type=["png", "jpg", "jpeg"])

            if not imagem:
                st.info("Sube una imagen para comenzar el reconocimiento de texto.")
                return

            img = Image.open(imagem)
            st.image(img, caption="Vista previa", use_column_width=True)

        with right_column:
            st.subheader("Texto detectado")
            with st.spinner("Extrayendo texto con Tesseract..."):
                self.texto = self.extrair_texto(img)

            render_text_output(self.texto)
            st.download_button(
                "Descargar texto",
                self.texto,
                file_name="textlens-ocr.txt",
                mime="text/plain",
                disabled=not bool(self.texto.strip()),
            )

        if self.analisar_texto:
            self.mostrar_analise()

    def extrair_texto(self, img):
        texto = pytesseract.image_to_string(img)
        return texto

    def mostrar_analise(self):
        documentos = fc.buscar_documento(self.texto)
        datas = fc.buscar_data(self.texto)
        p_boas, percentual_bom, palabras_encontradas_boas = fc.buscar_palavras_boas(self.texto)
        p_mas, percentual_mau, palabras_encontradas_malas = fc.buscar_palavras_mas(self.texto)

        st.divider()
        st.subheader("Resumen del analisis")

        dni_count = len(documentos) if documentos else 0
        date_count = len(datas) if datas else 0
        metric_a, metric_b, metric_c, metric_d = st.columns(4)
        metric_a.metric("DNI", dni_count)
        metric_b.metric("Fechas", date_count)
        metric_c.metric("Palabras positivas", p_boas, f"{percentual_bom:.2f}%")
        metric_d.metric("Palabras negativas", p_mas, f"{percentual_mau:.2f}%")

        result_a, result_b = st.columns(2, gap="large")

        with result_a:
            if not documentos:
                st.warning("No se encontro ningun DNI")
            else:
                st.success("DNI encontrado(s):")
                st.markdown(fc.sumarizar_cpf(documentos), unsafe_allow_html=True)

            if not datas:
                st.info("No se encontraron fechas")
            else:
                st.info("Fechas encontradas: {}".format(", ".join(datas)))

        with result_b:
            self.mostrar_sentimiento(p_boas, percentual_bom, palabras_encontradas_boas, "positivas")
            self.mostrar_sentimiento(p_mas, percentual_mau, palabras_encontradas_malas, "negativas")

    def mostrar_sentimiento(self, cantidad, percentual, palabras, tipo):
        if cantidad == 0:
            st.warning("No se encontraron palabras {}".format(tipo))
            return

        if tipo == "positivas":
            st.success("Palabras positivas")
        else:
            st.error("Palabras negativas")

        st.write("{} palabra(s) representan {:.2f}% del texto".format(cantidad, percentual))
        st.write("Palabras encontradas: {}".format(", ".join(palabras)))


ocr = OCR()
ocr.inicial()
