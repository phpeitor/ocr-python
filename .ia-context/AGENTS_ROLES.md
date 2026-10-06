# Roles de trabajo asistido

Antes de cambiar el repositorio, leer `README.md` y estas reglas. Confirmar si
el cambio afecta la interfaz Streamlit, la integración con Tesseract, el
análisis de texto o solo la configuración.

- Reutilizar `src/textlens/config.py` para nuevas variables de entorno.
- Mantener lógica de negocio independiente de Streamlit para poder probarla.
- No reintroducir estructuras PHP, JavaScript o Composer que no pertenecen a
  esta aplicación.
- Actualizar README cuando cambien comandos, dependencias, rutas o variables.
- Ejecutar al menos la compilación de Python y las pruebas relevantes antes de
  entregar.
