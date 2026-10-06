# Estándares de interfaz Streamlit

- Mantener la composición de la página en `src/textlens/app.py`.
- Mantener componentes visuales y estilos en `src/textlens/ui.py` y
  `assets/styles.css`; evitar CSS inline salvo el HTML estructural existente.
- Renderizar el texto OCR escapado y no tratarlo como HTML confiable.
- Mantener mensajes claros para carga, procesamiento, resultados y errores.
- Conservar compatibilidad con `python -m streamlit run main.py`.
- Verificar la interfaz con imágenes PNG, JPG y JPEG, incluyendo una imagen sin
  texto y una carga que supere el límite configurado.
