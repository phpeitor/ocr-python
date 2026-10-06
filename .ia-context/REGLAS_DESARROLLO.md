# Reglas de desarrollo — TextLens OCR

## Alcance

Este repositorio es una aplicación Python moderna con Streamlit para procesar
imágenes mediante Tesseract OCR. No contiene backend PHP, API REST, frontend
JavaScript independiente ni base de datos.

## Estructura

- La aplicación vive en `src/textlens/`.
- `app.py` contiene la composición de la interfaz Streamlit.
- `ocr.py` encapsula la integración con `pytesseract`.
- `analysis.py` contiene detección y análisis de texto sin dependencias de UI.
- `config.py` centraliza variables cargadas desde `.env`.
- Las palabras analizables se editan en la interfaz y sus valores iniciales
  viven como constantes en `analysis.py`.
- Los estilos se mantienen en `assets/styles.css`.
- `main.py` es un punto de entrada compatible para `streamlit run main.py`.

## Calidad y seguridad

- No registrar ni enviar fuera del proceso el contenido de las imágenes o del
  texto extraído.
- Validar el tipo de archivo y limitar el tamaño de las cargas desde Streamlit.
- Escapar texto OCR antes de renderizarlo como HTML.
- Mantener la ruta del ejecutable Tesseract en `.env`, nunca en credenciales ni
  código compartido.
- Añadir o actualizar pruebas para cambios en detección, configuración u OCR.
- Documentar en `README.md` cualquier cambio de instalación o comportamiento.

## Verificación local

Usar un entorno virtual, instalar el proyecto en editable y ejecutar:

```powershell
python -m compileall src main.py
python -m streamlit run main.py
```

Para cambios de dependencias, actualizar `pyproject.toml` y regenerar el
entorno, sin incluir `.venv` ni `.env` en Git.
