from flask import Flask, render_template, request
from reporting import get_report, get_matches

# se instancia el objeto Flask, con el nombre de la aplicación
app = Flask(__name__)

# se define la ruta de la aplicación, que es la raiz de la aplicación
@app.route('/')
def index():

    return render_template("index.html")

# se acepta input del usuario, y se llama a la función get_report, que se encuentra en reporting.py
@app.route('/', methods=["GET", "POST"])
def generar_reporte():

    if request.method == "POST":

        try: 

            tipo_operacion = request.form["tipo_operacion"].lower()
            estado_operacion = request.form["estado_operacion"].upper()
            tipo_cuenta = request.form["tipo_cuenta"].lower()

            # se filtran las transacciones que coincidan con los filtros
            transacciones = get_matches(tipo_operacion, estado_operacion, tipo_cuenta)

            # se llama a la funcion que genera el reporte, en base a las transacciones filtradas    
            get_report(tipo_operacion, estado_operacion, tipo_cuenta, transacciones)

            # se carga el template html, con el contenido del reporte
            return render_template("reporte.html")

        except:
            
            # en caso de que haya un error, se carga la página principal de nuevo
            return render_template("index.html")
  

# @app.route('/generar_usuario')
# def reporting():

#     return render_template("usuarios.html")


if __name__ == '__main__':

    app.run(debug=True)
