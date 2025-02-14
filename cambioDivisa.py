
from conexionApi import ConexionApi

class cambioDivisa():

    def __init__(self):
        self.conexion = ConexionApi()
        self.cliente = self.conexion.conectarApi()

    def obtenerTasasCambio(self, divisa):
        tasas = self.cliente.latest(base_currency=divisa)
        return tasas
 
    def convertir(self, cantidad, divisa, divisa_a_convertir):
        tasas = self.obtenerTasasCambio(divisa)
        if divisa_a_convertir not in tasas["data"]:
            print(f"Error: No se encontró la tasa de cambio para {divisa_a_convertir}.")
            return None
        tasa_cambio = tasas["data"][divisa_a_convertir]
        resultado = cantidad * tasa_cambio
        return resultado
    
    def obtenerDivisas(self):
        tasas = self.obtenerTasasCambio("USD")
        divisas = tasas["data"].keys()
        return divisas
              
if __name__ == "__main__":
    cambio = cambioDivisa()
    divisas = cambio.obtenerTasasCambio("USD")
    print(divisas)
