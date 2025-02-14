# Cambio de Divisas

Esta aplicación permite convertir divisas utilizando tasas de cambio obtenidas de una API. El proyecto está diseñado siguiendo principios de Clean Code y buenas prácticas de programación.

## Requisitos

- Python 3.8 o superior
- Conexión a Internet (para acceder a la API de divisas)

## Configuración del Entorno

1. **Crear un entorno virtual:**

   ```bash
   python -m venv venv
    ```

2. **Activar el entorno virtual:**

    * Windows

    ```bash
   venv\Scripts\activate
    ```

   * Linux
   ```bash
   source venv/bin/activate
    ```

2. **Seleccionar el interprete de Python en tu IDE:**

Asegúrate de que el intérprete seleccionado sea el que se encuentra en el entorno virtual recién creado.

## Instalar dependencias

instala las siguientes librerías utilizando pip:

- pip install freecurrencyapi
- pip install python-dotenv
- pip install rich

## Variables de entorno

El proyecto utiliza un archivo ```.env``` para almacenar variables de configuración. A continuación se explica la función de cada variable:

1. **API_KEY**

API_KEY=fca_live_V8L3Dv7CMpRx2jACwI218uYN2aba13mmo0Q5MQ5T
Clave de acceso para la API de divisas. Esta clave es necesaria para autenticar las solicitudes y obtener las tasas de cambio.

CANTIDAD_DIGITOS
CANTIDAD_DIGITOS=5
Define la cantidad de dígitos decimales que se mostrarán en las conversiones. Esto permite controlar la precisión de los resultados.

PERSISTIR_DATOS
PERSISTIR_DATOS=True
Indica si se deben guardar y mantener los datos de conversiones en el historial. Útil para sesiones posteriores y para llevar un registro de las conversiones realizadas.