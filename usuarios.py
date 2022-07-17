import json
import random
import csv
import pathlib


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

    #guardar json
    def guardarDatos(self):
        rand = random.randrange(100000, 999999)
        if not pathlib.Path(f"static/json/{self.nombre}_{self.apellido}.json").exists():
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

    # Guardar csv
    def guardarDatosCsv(self):
        rand = random.randrange(100000, 999999)
        archivo = f"static/csv/{self.nombre}_{self.apellido}.csv"

        fieldnames = ["Numero", "Nombre", "Apellido", "Dni",
                      "Tipo", "Calle", "Numero", "Ciudad", "Provincia", "Pais"]

        if not pathlib.Path(archivo).exists():
            with open(archivo, 'w', newline='') as create_file:
                writer = csv.DictWriter(
                    create_file, fieldnames=fieldnames, delimiter=';')
                writer.writeheader()

        with open(archivo, 'a', newline='') as escribir_csv:
            writer = csv.DictWriter(
                escribir_csv, fieldnames=fieldnames, delimiter=';')
            writer.writerow({
                'numero': rand,
                "nombre": self.nombre,
                "apellido": self.apellido,
                "dni":  self.dni,
                "tipo": self.tipo_cuenta,
                "calle": self.direccion_calle,
                "numero": self.direccion_numero,
                "ciudad": self.direccion_ciudad,
                "provincia": self.direccion_provincia,
                "pais": self.direccion_pais,
            })
