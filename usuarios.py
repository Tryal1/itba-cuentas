import json
import random

class Cliente():

    """ clase que permite crear clientes, con sus atributos y guardarlos en un archivo json y csv"""

    def __init__(self, nombre, apellido, dni, tipo_cuenta, direccion_calle, direccion_numero, direccion_ciudad, direccion_provincia, direccion_pais):

        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.tipo_cuenta = tipo_cuenta
        self.direccion_calle = direccion_calle
        self.direccion_numero = direccion_numero
        self.direccion_ciudad = direccion_ciudad
        self.direccion_provincia = direccion_provincia
        self.direccion_pais = direccion_pais

    #guardar json
    def guardarDatos(self):

            id_cliente = random.randrange(100000, 999999)

            with open(f"static/output/clientes.json", 'a') as usuarios_json:
                json.dump({
                    'numero': id_cliente,
                    "nombre": self.nombre,
                    "apellido": self.apellido,
                    "dni":  self.dni,
                    "tipo": self.tipo_cuenta,
                    "direccion": {
                        "calle": self.direccion_calle,
                        "numero": self.direccion_numero,
                        "ciudad": self.direccion_ciudad,
                        "provincia": self.direccion_provincia,
                        "pais": self.direccion_pais,
                    },
                }, usuarios_json)

    # guarda el csv de los datos
    def guardarDatosCsv(self):

        # en caso de que ya exista, se agrega un nuevo registro. Si no, se crea el archivo
        with open('static/output/clientes.csv','a') as f:

            # se crea aleatoriamente un numero de cuenta
            id_cliente = random.randrange(100000, 999999)

            nombre = self.nombre
            apellido = self.apellido
            dni = self.dni
            tipo_cuenta = self.tipo_cuenta
            direccion_calle = self.direccion_calle
            direccion_numero = self.direccion_numero
            direccion_ciudad = self.direccion_ciudad
            direccion_provincia = self.direccion_provincia
            direccion_pais = self.direccion_pais

            # se escribe el archivo, usando el ";" como separador
            items = f"{id_cliente};{nombre};{apellido};{dni};{tipo_cuenta};{direccion_calle};{direccion_numero};{direccion_ciudad};{direccion_provincia};{direccion_pais}\n"

            # se escribe el archivo
            f.write(items)
