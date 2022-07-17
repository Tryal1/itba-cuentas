import json
import random

class Cliente():

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

    def guardarDatos(self):
        rand = random.randrange(100000,999999)
        with open(f"static/json/{self.nombre}_{self.apellido}.json", 'a') as usuario:
            json.dump({
                'numero': rand,
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
            }, usuario)
