import freecurrencyapi
import os
from dotenv import load_dotenv

class ConexionApi:
    
    _instancia = None  

    def __new__(cls):

        if cls._instancia is None:
            cls._instancia = super(ConexionApi, cls).__new__(cls)
            cls._instancia._initialize() 

        return cls._instancia

    def _initialize(self):
        load_dotenv()  
        self.api_key = os.getenv("API_KEY")

    def conectar_api(self):

        if not self.api_key:
            print("Error: No se encontró la API_KEY en las variables de entorno.")
            return None

        try:
            cliente = freecurrencyapi.Client(self.api_key)
            return cliente
        
        except Exception as e:
            print(f"Error al intentar conectar con la API: {e}")
            return None
        
   