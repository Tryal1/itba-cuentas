from flask import Flask, render_template, request
from reporting import get_report, get_matches
import json

app = Flask(__name__)

# se carga el template html
@app.route('/')
def index():
  return render_template("index.html")

# @app.route('/reporting')
# def reporting():
#   return render_template("usuarios.html")

# se acepta input del usuario
@app.route('/', methods = ["GET", "POST"])
def generar_reporte():

    if request.method == "POST":

        tipo_operacion = request.form["tipo_operacion"]
        estado_operacion = request.form["estado_operacion"]
        tipo_cuenta = request.form["tipo_cuenta"]

        print(tipo_operacion, estado_operacion, tipo_cuenta)
        get_matches(tipo_cuenta=tipo_cuenta)

        # se llama a la funcion que genera el reporte
        get_report(tipo_operacion, estado_operacion, tipo_cuenta)


        # time.sleep(1)

        return render_template("reporte.html")

        
    
       # return render_template("index.html")

    else:

        print("No se ha recibido ningun dato")

        return render_template("index.html")    


if __name__ == '__main__':
  app.run(debug=True)