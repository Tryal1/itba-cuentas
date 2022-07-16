# el nombre apellido y numero siempre se va a mostrar en pantalla, haya o no un match
nombre = "Pepito"
apellido = "Jaimito"
numero = "123456789"

# aca hay un ejemplo de como se devolveria el resultrado del filtrado del JSON
transacciones = [{
			"estado": "ACEPTADA",
			"tipo": "RETIRO_EFECTIVO_CAJERO_AUTOMATICO",
			"cuentaNumero": 190,
			"cupoDiarioRestante": 9000,
			"cantidadExtraccionesHechas": 1,
			"monto": 1000,
			"fecha": "06/06/2022 10:00:55",
			"numero": 1,
			"saldoEnCuenta": 100000,
			"totalTarjetasDeCreditoActualmente" : 5,
			"totalChequerasActualmente" : 2
		},
		{
			"estado": "ACEPTADA",
			"tipo": "RETIRO_EFECTIVO_CAJERO_AUTOMATICO",
			"cuentaNumero": 190,
			"cupoDiarioRestante": 9000,
			"cantidadExtraccionesHechas": 1,
			"monto": 1000,
			"fecha": "06/06/2022 10:00:55",
			"numero": 1,
			"saldoEnCuenta": 100000,
			"totalTarjetasDeCreditoActualmente" : 5,
			"totalChequerasActualmente" : 2
		},
		{
			"estado": "ACEPTADA",
			"tipo": "RETIRO_EFECTIVO_CAJERO_AUTOMATICO",
			"cuentaNumero": 190,
			"cupoDiarioRestante": 9000,
			"cantidadExtraccionesHechas": 1,
			"monto": 1000,
			"fecha": "06/06/2022 10:00:55",
			"numero": 1,
			"saldoEnCuenta": 100000,
			"totalTarjetasDeCreditoActualmente" : 5,
			"totalChequerasActualmente" : 2
		}
		]

# se separa el html en 4 partes

# el principio del html, en donde esta el link al css, etc.
start = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <link rel="stylesheet" href='/static/main.css' />
        <title>Document</title>
        <body>
"""

# esta es la parte del nombre, apellido y numero, que siempre va a estar en el html
static_content = f""" 
    <h1>Clientes</h1> 
    <h2>Nombre: {nombre}</h2> 
    <h2>Apellido: {apellido}</h2> 
    <h2>Numero:{numero} </h2> 
"""

# esta es la  que se genera en base al contenido del json, que va a cambiar segun el match
# para cada elemento del json, se genera un "ul" y se le agrega un "li" por cada elemento
variable_content = ""
for transaccion in transacciones:

    text = f""" 
                <h2> Nueva Transacción </h2>
                <ul class='transaccion'>
                <li>Estado de transaccion: {transaccion["estado"]}</li>
                <li>Cantidad Extracciones: {transaccion["cantidadExtraccionesHechas"]}</li>
                <li>Saldo en cuenta: {transaccion["saldoEnCuenta"]}</li>
                <li>Fecha: {transaccion["fecha"]}</li>
                </ul>        
"""

    variable_content += text
     

# se termina el html     
end = """ </body>
    </html>
"""

# aca se suman todas las partes del html
html = start + static_content + variable_content + end

# se escribe el html en un archivo
# para probar como funciona con distintos matches, se pueden agregar o eliminar elementos del json y va a cambiar el output
with open("reporte.html", "w", encoding="utf-8") as f:
        f.write(html)