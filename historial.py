import csv
import os
from dotenv import load_dotenv

load_dotenv()

class Historial:
    ARCHIVO_CSV = "historial_conversiones.csv"

    def __init__(self):
        self.historial = []
        self.PERSISTIR_DATOS = os.getenv("PERSISTIR")
        print("constructor de historial " + self.PERSISTIR_DATOS)
        if self.PERSISTIR_DATOS == "True":
            print("cargando datos del csv")
            self.cargarCSV() 

    def cargarCSV(self):
        
        if os.path.exists(self.ARCHIVO_CSV) and os.path.getsize(self.ARCHIVO_CSV) > 0:
            with open(self.ARCHIVO_CSV, mode="r", newline="", encoding="utf-8") as archivo:
                lector = csv.DictReader(archivo)
                self.historial = [fila for fila in lector]

    def guardarConversion(self, moneda_base, moneda_destino, cantidad, conversion, tasa):

        print("intentando guardar la informacion...")

        load_dotenv()
        
        print(type(self.PERSISTIR_DATOS))
        print("valor de la variable: " + self.PERSISTIR_DATOS)

        registro = {
            "moneda_base": moneda_base,
            "moneda_destino": moneda_destino,
            "cantidad": cantidad,
            "conversion": conversion,
            "tasa": tasa
        }

        self.historial.append(registro)

        if self.PERSISTIR_DATOS == "True":
            print("guardando en csv...")
            self.guardarCSV(registro)

            

    def guardarCSV(self, registro):
        # Verificar si el archivo existe y tiene contenido (es decir, cabecera escrita)
        archivo_existe = os.path.exists(self.ARCHIVO_CSV) and os.path.getsize(self.ARCHIVO_CSV) > 0
        with open(self.ARCHIVO_CSV, mode="a", newline="", encoding="utf-8") as archivo:
            campos = ["moneda_base", "moneda_destino", "cantidad", "conversion", "tasa"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)

            if not archivo_existe:
                escritor.writeheader()

            escritor.writerow(registro)

    def obtenerHistorial(self):
        return self.historial
    
