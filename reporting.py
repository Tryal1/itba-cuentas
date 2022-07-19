import json


def get_matches(tipo_operacion, estado_operacion, tipo_cuenta):

    with open(f"static/output/json/output_{tipo_cuenta}.json") as f:

        data = json.load(f)

        transacciones = []
        for transaccion in data["transacciones"]:

            if(transaccion['estado'] == estado_operacion) and (transaccion['tipo'] == tipo_operacion if tipo_operacion != "ALL" else True):

                transacciones.append(transaccion)

        return transacciones


def get_report(tipo_operacion, estado_operacion, tipo_cuenta, transacciones):

    start = """
        <!DOCTYPE html>
        <html lang="en">
            <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta http-equiv="X-UA-Compatible" content="ie=edge">
            <link rel="stylesheet" href='/static/css/main.css' />
            <title>Document</title>
            </head>
            <body>  
                <div class="header">
                    <h1>Registro de Transacciones</h1>
                    <img src="../static/images/itbank_logo.png" alt="logo">
                </div>
                <form method="POST" id="form">
                    <label for="">Tipo de Operación</label>
                    <input type="text" name="tipo_operacion">
                    <label for="">Estado de Operación</label>
                    <input type="text" name="estado_operacion">
                    <label for="">Tipo de cuenta</label>
                    <input type="text" name="tipo_cuenta">
                    <input id = "button" type="submit" value="Enviar">
                </form>
            <section class="body-data">
    """

    # esta es la parte de los filtros utilizados que va a estar siempre en el html
    static_content = f""" 
            <div class="static-content">
                <h2>Tipo Operación: {tipo_operacion}</h2> 
                <h2>Estado Operación: {estado_operacion}</h2> 
                <h2>Tipo de cuenta:{tipo_cuenta} </h2>
            </div>  
    """

    # esta es la  que se genera en base al contenido del json, que va a cambiar segun el match
    # para cada elemento del json, se genera un "ul" y se le agrega un "li" por cada elemento
    variable_content = ""
    for transaccion in transacciones:

        text = f"""
                <div class="variable-content">
                    <h2> Nueva Transacción </h2>
                    <ul class='transaccion'>
                    <li>Estado de transaccion: {transaccion["estado"]}</li>
                    <li>Tipo de operación: {transaccion["tipo"]}</li>
                    <li>Saldo en cuenta: {transaccion["saldoEnCuenta"]}</li>
                    <li>Fecha: {transaccion["fecha"]}</li>
                    <li>Número de cuenta: {transaccion["cuentaNumero"]}</li>
                    <li>Razón de rechazo: {transaccion["razon_de_rechazo"]}</li>
                    </ul>     
                </div>  
            
    """

        variable_content += text

    # se termina el html
    end = """ </section></body>
        </html>
    """

    # aca se suman todas las partes del html
    html = start + static_content + variable_content + end

    # se escribe el html en un archivo
    with open("templates/reporte.html", "w", encoding="utf-8") as f:

        f.write(html)
