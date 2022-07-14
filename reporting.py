import json

def get_matches(tipo_cuenta):
    if tipo_cuenta == "Black":

        with open("static/json/eventos_black.json") as f:
            data = json.load(f)
            print(data)



def get_report(tipo_operacion, estado_operacion, tipo_cuenta):

    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <link rel="stylesheet" href='/static/main.css' />


        <title>Document</title>
    </head>
    <body>
        <h1>Clientes</h1>
        <ul class="test">
            <li>{tipo_operacion}</li>
            <li>{estado_operacion}</li>
            <li>{tipo_cuenta}</li>
        </ul>
    </body>
    </html>
    """

    with open(r"C:\Users\Benja\Desktop\sprint5\templates\reporte.html", "w") as f:
        f.write(html)


