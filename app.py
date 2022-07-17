from flask import Flask, render_template, request
from reporting import get_report, get_matches
from usuarios import Cliente

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
            transacciones = get_matches(
                tipo_operacion, estado_operacion, tipo_cuenta)

            # se llama a la funcion que genera el reporte, en base a las transacciones filtradas
            get_report(tipo_operacion, estado_operacion,
                       tipo_cuenta, transacciones)

            # se carga el template html, con el contenido del reporte
            return render_template("reporte.html")

        except:

            # en caso de que haya un error, se carga la página principal de nuevo
            return render_template("index.html")


@app.route('/generar_usuario', methods=[ 'GET',"POST"])
def generar_data():
    try:
        nombre = request.form['nombre'].lower()
        apellido = request.form['apellido'].lower()
        dni = request.form['dni'].lower()
        tipo_cuenta = request.form['tipo_cuenta'].lower()
        direccion_calle = request.form['direccion_calle'].lower()
        direccion_numero = request.form['direccion_numero'].lower()
        direccion_ciudad = request.form['direccion_ciudad'].lower()
        direccion_provincia = request.form['direccion_provincia'].lower()
        direccion_pais = request.form['direccion_pais'].lower()
        regustro = Cliente(nombre, apellido, dni, tipo_cuenta, direccion_calle,
                           direccion_numero, direccion_ciudad, direccion_provincia, direccion_pais)
        regustro.guardarDatos()
        return render_template("usuarios.html")
    except:
        return render_template("usuarios.html")


if __name__ == '__main__':

    app.run(debug=True)
