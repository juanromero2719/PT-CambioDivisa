import csv
import os

class Historial:

    ARCHIVO_CSV = "historial_conversiones.csv"

    def __init__(self):
        self.historial = []
        self.PERSISTIR_DATOS = os.getenv("PERSISTIR_DATOS", False)
        if self.PERSISTIR_DATOS:
            self._cargar_desde_csv()

    def _cargar_desde_csv(self):

        if os.path.exists(self.ARCHIVO_CSV):
            with open(self.ARCHIVO_CSV, mode="r", newline="", encoding="utf-8") as archivo:
                lector = csv.DictReader(archivo)
                self.historial = [fila for fila in lector]

    def guardar_conversion(self, moneda_base, moneda_destino, cantidad, conversion, tasa):
 
        registro = {
            "moneda_base": moneda_base,
            "moneda_destino": moneda_destino,
            "cantidad": cantidad,
            "conversion": conversion,
            "tasa": tasa
        }
        self.historial.append(registro)

        if self.PERSISTIR_DATOS:
            self._guardar_en_csv(registro)

    def _guardar_en_csv(self, registro):
        
        archivo_existe = os.path.exists(self.ARCHIVO_CSV)
        with open(self.ARCHIVO_CSV, mode="a", newline="", encoding="utf-8") as archivo:
            campos = ["moneda_base", "moneda_destino", "cantidad", "conversion", "tasa"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)

            if not archivo_existe:
                escritor.writeheader() 

            escritor.writerow(registro)

    def obtener_historial(self):
        return self.historial
