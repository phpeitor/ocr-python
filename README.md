## TextLens OCR 🐍
[![forthebadge](http://forthebadge.com/images/badges/made-with-python.svg)](https://www.linkedin.com/in/drphp/)
[![forthebadge](http://forthebadge.com/images/badges/built-with-love.svg)](https://www.linkedin.com/in/drphp/)

<a href="https://www.instagram.com/amvsoft.tech/">
  <img src="https://cdn.dribbble.com/userupload/16288591/file/original-3925e50a24ee40dfc622624e3579b7d8.jpg" alt="instagram" width="600">
</a>

[![Video Demo](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/watch?v=K9n4jRPH-94) `Hello Everyone 🙌`

## Resumen

TextLens es una aplicación local de OCR construida con Python y Streamlit.
Permite cargar una imagen, extraer su texto con Tesseract y analizar
documentos de identidad, fechas y palabras configurables.

La aplicación procesa las imágenes durante la sesión y no requiere base de
datos ni un backend adicional.

## Funcionalidades

- OCR para imágenes `PNG`, `JPG` y `JPEG`.
- Configuración de idioma mediante Tesseract (`spa`, `eng`, etc.).
- Descarga del texto reconocido como archivo `.txt`.
- Detección de documentos de identidad de ocho dígitos.
- Detección de fechas con formato `dd/mm/yyyy`.
- Diccionario editable de palabras buenas y malas desde el panel lateral.
- Soporte para tokens especiales como `S/` y `$`.
- Temas `System`, `Light` y `Dark`.
- Límite configurable para el tamaño de las imágenes.

## Requisitos

- Windows, macOS o Linux.
- Python 3.10 o superior.
- Tesseract OCR.
- Modelo de idioma de Tesseract correspondiente al valor de `OCR_LANGUAGE`.

## Instalación de Tesseract en Windows

1. Descarga el instalador desde la [página de Tesseract para Windows](https://github.com/UB-Mannheim/tesseract/wiki).
2. Instala Tesseract y el paquete de idioma español (`spa`) si procesarás
   documentos en español.
3. Comprueba la instalación:

```powershell
tesseract --version
tesseract --list-langs
```

Si Tesseract no está en `PATH`, define su ruta en `.env`:

```env
TESSERACT_CMD=C:\Program Files\Tesseract-OCR\tesseract.exe
```

Para español debe aparecer `spa` en la salida de `tesseract --list-langs`.

## Instalación del proyecto

Desde la raíz del repositorio:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e .
```

Si PowerShell bloquea la activación del entorno:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## Configuración

Copia la plantilla y ajusta los valores locales:

```powershell
Copy-Item .env.example .env
```

Configuración recomendada para español:

```env
APP_NAME=TextLens
APP_PAGE_ICON=🔎
OCR_LANGUAGE=spa
TESSERACT_CMD=C:\Program Files\Tesseract-OCR\tesseract.exe
MAX_UPLOAD_SIZE_MB=5
```

| Variable | Descripción | Valor predeterminado |
| --- | --- | --- |
| `APP_NAME` | Nombre mostrado en la aplicación. | `TextLens` |
| `APP_PAGE_ICON` | Icono de la página de Streamlit. | `🔎` |
| `OCR_LANGUAGE` | Idioma utilizado por Tesseract. | Sin idioma explícito |
| `TESSERACT_CMD` | Ruta del ejecutable de Tesseract. | `PATH` del sistema |
| `MAX_UPLOAD_SIZE_MB` | Tamaño máximo de una imagen. | `5` |

No subas `.env` al repositorio. El archivo está excluido mediante
`.gitignore`.

## Ejecución

```powershell
python -m streamlit run main.py
```

También está disponible el comando instalado por el paquete:

```powershell
textlens
```

Abre la URL que muestre Streamlit, normalmente
`http://localhost:8501`.

## Uso

1. Carga una imagen desde **Carga tu imagen**.
2. Revisa la vista previa y espera el resultado del OCR.
3. Descarga el texto si lo necesitas.
4. Activa o desactiva **Analizar contenido**.
5. Consulta DNI, fechas y coincidencias del diccionario.

### Diccionario OCR

En el panel lateral abre **Diccionario OCR**. Añade o elimina una palabra o
símbolo por línea en **Palabras buenas** y **Palabras malas**. Los valores
iniciales son:

```text
Buenas: AMAR, PERRO, PERU, GANADOR, S/, $, YAPE, ACEPTO
Malas:  ODIO, IA, PERDEDOR, ESTAFA
```

Los cambios son válidos durante la sesión actual. **Restaurar palabras
iniciales** recupera los valores predeterminados.

### Tema visual

En el menú de tres puntos de Streamlit, abre **Settings** y selecciona
`System`, `Light` o `Dark`. El diseño pixel-game adapta sus superficies,
colores y contraste al tema seleccionado.

## Estructura

```text
ocr-python/
├── .ia-context/          # Reglas y estándares del proyecto
├── assets/styles.css     # Tema visual pixel-game
├── src/textlens/
│   ├── analysis.py       # Detección y análisis de texto
│   ├── app.py            # Interfaz y flujo de Streamlit
│   ├── config.py         # Configuración desde .env
│   ├── ocr.py            # Integración con pytesseract
│   └── ui.py             # Componentes visuales
├── .env.example
├── main.py               # Punto de entrada compatible
├── pyproject.toml        # Metadatos y dependencias
└── README.md
```

## Desarrollo y validación

Validación rápida:

```powershell
python -m compileall -q src main.py
python -m pip install -e .
```

Para probar la aplicación, inicia Streamlit y procesa imágenes nítidas,
imágenes sin texto y archivos cercanos al límite configurado.

## Solución de problemas

### `tesseract is not installed or it's not in your PATH`

Comprueba `tesseract --version` y define `TESSERACT_CMD` en `.env` si el
ejecutable no está disponible en el `PATH`.

### `Failed loading language 'spa'`

Instala `spa.traineddata` en la carpeta `tessdata` de Tesseract y confirma
que `tesseract --list-langs` muestre `spa`.

### El OCR no reconoce bien el texto

Usa imágenes nítidas, con buena iluminación y texto horizontal. Verifica que
`OCR_LANGUAGE` coincida con el idioma del documento.

### La interfaz no refleja cambios de estilos

Reinicia Streamlit con `Ctrl + C` y vuelve a ejecutar:

```powershell
python -m streamlit run main.py
```

## Tecnologías

- Python
- Streamlit
- Pillow
- pytesseract
- python-dotenv
- Tesseract OCR
