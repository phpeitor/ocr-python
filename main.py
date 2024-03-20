import streamlit as st
from PIL import Image
import pytesseract
import functions.functions as fc

class OCR:

    def __init__(self):
        st.set_page_config(page_title="WEB OCRIFY")
        self.texto = ""
        self.analisar_texto = False

    def inicial(self):
        st.title("OCRify")
        st.write("Optical Character Recognition (OCR) implementado con Python")
        imagem = st.file_uploader("Seleccione imagen", type=["png","jpg"])

        if imagem:
            img = Image.open(imagem)
            st.image(img, width=350)
            st.info("Extraer texto")
            self.texto = self.extrair_texto(img)
            st.write("{}".format(self.texto))
            
            self.analisar_texto = st.sidebar.checkbox("🤖 Analizando OCR")
            if self.analisar_texto==True:
                self.mostrar_analise()
    
    def extrair_texto(self, img):
        texto = pytesseract.image_to_string(img)
        return texto
    
    def mostrar_analise(self):
        cpf = fc.buscar_documento(self.texto)
        datas = fc.buscar_data(self.texto)
        p_boas, percentual_bom, palabras_encontradas_boas = fc.buscar_palavras_boas(self.texto)
        p_mas, percentual_mau, palabras_encontradas_malas = fc.buscar_palavras_mas(self.texto)
        
        if cpf==None:
            st.warning("No se encontró ningún DNI")
        else:
            cpf = fc.sumarizar_cpf(cpf)
            st.success("DNI encontrado(s):")
            st.markdown(cpf, unsafe_allow_html=True)
        
        if p_boas == 0:
            st.warning("✔️ No se encontraron palabras positivas")
        else:
            st.success("✔️ Palabras positivas:")
            st.write("{} palabra(s) representan {:.2f}% del texto".format(p_boas, percentual_bom))
            if palabras_encontradas_boas:
                st.write("Palabras encontradas: {}".format(", ".join(palabras_encontradas_boas)))
            else:
                st.write("No se encontraron palabras específicas")


        if p_mas == 0:
            st.error("❌ No se identificaron palabras negativas")
        else:
            st.error("❌ Palabras negativas:")
            st.write("{} palabra(s) Representan {:.2f}% del texto".format(p_mas, percentual_mau))
            st.write("Palabras encontradas: {}".format(", ".join(palabras_encontradas_malas)))

ocr = OCR()
ocr.inicial()