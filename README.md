## TextLens OCR 🐍
[![forthebadge](http://forthebadge.com/images/badges/made-with-python.svg)](https://www.linkedin.com/in/drphp/)
[![forthebadge](http://forthebadge.com/images/badges/built-with-love.svg)](https://www.linkedin.com/in/drphp/)

[![Video](https://img.youtube.com/vi/K9n4jRPH-94/0.jpg)](https://www.youtube.com/watch?v=K9n4jRPH-94)  

[![Video Demo](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube)](https://www.youtube.com/watch?v=K9n4jRPH-94)

## Caracteristicas

- Carga imagenes `PNG`, `JPG` y `JPEG` desde el navegador.
- Extrae texto con `pytesseract` y Tesseract OCR.
- Permite descargar el texto detectado en `.txt`.
- Detecta documentos de identidad de 8 digitos.
- Detecta fechas con formato `dd/mm/yyyy`.
- Permite agregar y eliminar palabras buenas y malas desde dos cajas editables
  en el panel lateral.
- Soporta tokens con simbolos como `S/` y `$`.
- Usa variables de entorno con `.env`.
- Tiene estilos separados en `assets/styles.css`.
- Incluye temas `System`, `Light` y `Dark` desde el menu de Streamlit.

## Requisitos

- Python 3.10 o superior.
- pip.
- Tesseract OCR instalado en el sistema.

## Instalacion Tesseract OCR

### Windows

1. Descarga el instalador desde:

```text
https://github.com/UB-Mannheim/tesseract/wiki
```

2. Instala Tesseract OCR.
3. Asegurate de que el ejecutable quede disponible en el PATH.
4. Verifica la instalacion:

```powershell
tesseract --version
```

Si el comando no funciona, configura la ruta en tu archivo `.env`:

```env
TESSERACT_CMD=C:\Program Files\Tesseract-OCR\tesseract.exe
```

## Instalacion Proyecto

1. Clona el repositorio:

```powershell
git clone <url-del-repositorio>
cd ocr-python
```

2. Crea un entorno virtual:

```powershell
python -m venv .venv
```

3. Activa el entorno virtual:

```powershell
.\.venv\Scripts\Activate.ps1
```

Si PowerShell bloquea la activacion, ejecuta una vez:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

4. Instala dependencias y el paquete local:

```powershell
python -m pip install -e .
```

## Configuracion .env

El proyecto incluye `.env.example` como plantilla. Crea tu archivo `.env` local:

```powershell
copy .env.example .env
```

Variables disponibles:

```env
APP_NAME=TextLens
APP_PAGE_ICON=🔎
OCR_LANGUAGE=spa
TESSERACT_CMD=C:\Program Files\Tesseract-OCR\tesseract.exe
MAX_UPLOAD_SIZE_MB=5
```

Uso de cada variable:

- `APP_NAME`: nombre mostrado en la app.
- `APP_PAGE_ICON`: icono de la pestana del navegador.
- `OCR_LANGUAGE`: idioma usado por Tesseract, por ejemplo `spa` para espanol o `eng` para ingles.
- `TESSERACT_CMD`: ruta al ejecutable de Tesseract si no esta en PATH.
- `MAX_UPLOAD_SIZE_MB`: limite de tamano para imagenes subidas.

Ejemplo para OCR en espanol:

```env
OCR_LANGUAGE=spa
```

Para usar `spa`, debes tener instalado el paquete de idioma espanol de Tesseract.

## Ejecutar App

Desde la raiz del proyecto:

```powershell
python -m streamlit run main.py
```

Tambien puedes usar el comando instalado por el paquete:

```powershell
textlens
```

Streamlit mostrara una URL local similar a:

```text
http://localhost:8501
```

Abre esa URL en tu navegador.

### Cambiar tema visual

Abre el menu de tres puntos de Streamlit, selecciona **Settings** y elige
`System`, `Light` o `Dark`. La interfaz pixel-game adapta automaticamente sus
fondos, tarjetas, texto, metricas y colores de contraste al tema seleccionado.

## Como Usar

1. Sube una imagen con texto visible.
2. Revisa la vista previa de la imagen.
3. Espera la extraccion de texto.
4. Descarga el texto si lo necesitas.
5. Activa o desactiva el analisis desde el panel lateral.
6. Revisa DNI, fechas, palabras positivas y palabras negativas detectadas.

## Personalizar Palabras

En el panel lateral abre **Diccionario OCR** y edita las cajas **Palabras
buenas** y **Palabras malas**. Agrega o elimina una palabra o símbolo por
línea. Los valores iniciales son:

```text
# Palabras buenas
AMAR
PERRO
PERU
GANADOR
S/
$
YAPE
ACEPTO

# Palabras malas
ODIO
IA
PERDEDOR
ESTAFA
```

Los cambios se aplican al siguiente análisis de la sesión actual. El botón
**Restaurar palabras iniciales** recupera la configuración incluida por defecto.

## Estructura Principal

```text
ocr-python/
├── assets/
│   └── styles.css
├── src/
│   └── textlens/
│       ├── analysis.py
│       ├── app.py
│       ├── config.py
│       ├── ocr.py
│       ├── ui.py
├── pyproject.toml
├── main.py
├── .env.example
└── README.md
```

## Solucion Bugs

### `tesseract is not installed or it's not in your PATH`

Instala Tesseract OCR o define `TESSERACT_CMD` en `.env`.

### El OCR no reconoce bien textos en espanol

Instala el idioma espanol de Tesseract y configura:

```env
OCR_LANGUAGE=spa
```

### Cambie estilos y no se ven en el navegador

Recarga con `Ctrl + F5` o reinicia Streamlit con `Ctrl + C` y luego:

```powershell
python -m streamlit run main.py
```

## Tecnologias

- Streamlit
- Pillow
- pytesseract
- python-dotenv
- Tesseract OCR
