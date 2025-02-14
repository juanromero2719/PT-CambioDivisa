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

```API_KEY=fca_live_V8L3Dv7CMpRx2jACwI218uYN2aba13mmo0Q5MQ5T```
Clave de acceso para la API de divisas. Esta clave es necesaria para autenticar las solicitudes y obtener las tasas de cambio.

2. **CANTIDAD_DIGITOS**

```CANTIDAD_DIGITOS=5```
Define la cantidad de dígitos decimales que se mostrarán en las conversiones. Esto permite controlar la precisión de los resultados.

3. **PERSISTIR_DATOS**

```PERSISTIR_DATOS=True```
Indica si se deben guardar y mantener los datos de conversiones en el historial. Útil para sesiones posteriores y para llevar un registro de las conversiones realizadas.

## Uso

Una vez que hayas configurado el entorno e instalado las dependencias, ejecuta la aplicación con:

```bash
python main.py
```

La aplicación mostrará un menú en el que podrás:

- Seleccionar una o dos monedas.
- Ingresar la cantidad a convertir.
- Elegir la moneda destino para la conversión.
- Ver las tasas de cambio y el resultado de la conversión.
- Acceder al historial de conversiones.

## Notas adicionales

- Asegúrate de que el archivo ```.env``` se encuentre en la raíz del proyecto para que la librería ```python-dotenv``` pueda cargar correctamente las variables de entorno.

- Si necesitas modificar la precisión de los resultados, ajusta el valor de ```CANTIDAD_DIGITOS``` en el archivo ```.env```.

- La persistencia de datos está controlada por la variable ```PERSISTIR_DATOS```. Configúrala según tus necesidades.