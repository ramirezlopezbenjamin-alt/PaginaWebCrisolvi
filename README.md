# Sitio Web Institucional - Escuela Especial Crisolvi

Portal informativo desarrollado durante mi práctica profesional para la **Escuela Especial Crisolvi** (Arica, Chile - RBD 12536-9), institución especializada en la atención integral de estudiantes con TEA, discapacidad visual y multidéficit hubicada en Nicolás Hidalgo 1882.

## Tecnologías Utilizadas
* **Backend:** Python 3 y Flask.
* **Arquitectura:** Programación Orientada a Objetos (**POO**) para el modelado de datos institucionales y equipo multiprofesional.
* **Frontend:** HTML5, CSS3 (variables de marca institucional), Bootstrap 5 y motor de plantillas **Jinja2**.
* **Control de Versiones:** Git.

## Estructura del Proyecto
* `app.py`: Controlador principal y definición de rutas (**routes**) de Flask.
* `models.py`: Clases y objetos (`Establecimiento`, `IntegranteEquipo`) que estructuran la información.
* `templates/index.html`: Interfaz principal responsiva con renderizado dinámico.
* `static/`: Recursos estáticos (hojas de estilo CSS, logotipo oficial y documentos PDF del PEI y RICE).

## Cómo ejecutar el proyecto localmente
1. Activar el entorno virtual:
   `venv\Scripts\activate`
2. Instalar dependencias (si es un equipo nuevo):
   `pip install flask`
3. Iniciar el servidor de desarrollo:
   `python app.py`
4. Abrir en el navegador: `http://127.0.0.1:5000`