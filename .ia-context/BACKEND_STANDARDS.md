# Estándares de procesamiento OCR

Este proyecto no expone un backend HTTP. El procesamiento ocurre en la sesión
local de Streamlit y debe permanecer encapsulado en `src/textlens/ocr.py`.

- Configurar Tesseract únicamente mediante `TESSERACT_CMD` o el `PATH` del
  sistema.
- Usar `pytesseract.image_to_string` y propagar errores de configuración de
  Tesseract de forma clara a la interfaz.
- Mantener el idioma en `OCR_LANGUAGE`; `spa` requiere que el paquete de
  idioma español esté instalado en Tesseract.
- No aceptar rutas locales proporcionadas por el usuario: procesar únicamente
  el objeto de carga de Streamlit.
- No añadir almacenamiento persistente de imágenes o texto sin documentar el
  cambio y su tratamiento de datos sensibles.
