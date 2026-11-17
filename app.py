from flask import Flask, render_template
# Importamos tanto el objeto de la escuela como la lista de objetos del equipo
from models import escuela_crisolvi, equipo_crisolvi

app = Flask(__name__)

# Inyectamos ambos datos en todas las vistas HTML
@app.context_processor
def inyectar_datos_escuela():
    return dict(escuela=escuela_crisolvi, equipo=equipo_crisolvi)

@app.route("/")
def inicio():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=False)