class Establecimiento:
    # El método __init__ se ejecuta automáticamente al crear el objeto (la ficha)
    def __init__(self, nombre, lema, direccion, telefono, correo, directora, jornada, facebook_url):
        # self guarda cada dato dentro del propio objeto
        self.nombre = nombre
        self.lema = lema
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.directora = directora
        self.jornada = jornada
        self.facebook_url = facebook_url

# Instanciamos (creamos) el objeto con los datos reales de Crisolvi
escuela_crisolvi = Establecimiento(
    nombre="Escuela Especial Crisolvi",
    lema="Unidos para Servir",
    direccion="Pasaje Nicolás Hidalgo N° 1882, Población Fresia, Arica",
    telefono="223331585",
    correo="ecrisolvi@gmail.com",
    directora="Carol Acuña Bravo",
    jornada="Lunes a Viernes de 08:00 a 13:00 hrs",
    facebook_url="https://www.facebook.com/crisolvi.crisolvi/"
)


# Clase POO para representar cada área o profesional del equipo de la escuela
class IntegranteEquipo:
    def __init__(self, cargo, dotacion, descripcion):
        self.cargo = cargo
        self.dotacion = dotacion
        self.descripcion = descripcion

# Lista de objetos con la dotación oficial del PEI 2026 y RICE 2026
equipo_crisolvi = [
    IntegranteEquipo(
        cargo="Dirección",
        dotacion="1 Directora",
        descripcion="Liderazgo institucional, gestión técnico-pedagógica y coordinación del Gabinete Técnico."
    ),
    IntegranteEquipo(
        cargo="Docentes de Educación Diferencial",
        dotacion="6 Profesoras Especialistas",
        descripcion="Planificación y enseñanza personalizada por curso (máximo 8 estudiantes) con adecuaciones curriculares."
    ),
    IntegranteEquipo(
        cargo="Técnicos Asistentes de Aula",
        dotacion="6 Técnicos en Educación Especial",
        descripcion="Apoyo permanente en aula, rutinas diarias, recreos, alimentación y cuidado integral."
    ),
    IntegranteEquipo(
        cargo="Psicología",
        dotacion="1 Psicóloga",
        descripcion="Evaluación diagnóstica, contención emocional, apoyo en convivencia y talleres a familias."
    ),
    IntegranteEquipo(
        cargo="Kinesiología",
        dotacion="1 Kinesióloga",
        descripcion="Rehabilitación motora, postura, patrones de movimiento, apoyo en Educación Física adaptada y talleres a familias."
    ),
    IntegranteEquipo(
        cargo="Fonoaudiología y Terapia Ocupacional",
        dotacion="1 Fonoaudióloga • 1 Terapeuta",
        descripcion="Estimulación del lenguaje, comunicación alternativa (pictogramas), autonomía, regulación sensorial y talleres a familias."
    )
]