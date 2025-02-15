from rich.console import Console
from rich.table import Table
from cambioDivisa import cambioDivisa
from historial import Historial
import os
from dotenv import load_dotenv

class Vista:

    def __init__(self):
        load_dotenv()
        self.console = Console()
        self.cambio = cambioDivisa()
        self.divisas = list(self.cambio.obtenerDivisas())
        self.historial = Historial()
        self.cantidad_digitos = os.getenv("CANTIDAD_DIGITOS", 5)
        

    def run(self):
        while True:
            self.ejecutarPrograma()
            opcion = self.menuPostConversion()
            if opcion == "1":
                continue
            elif opcion == "2":
                
                while True:
                    self.mostrarHistorial()
                    opcion_post = self.menuPostConversion()
                    if opcion_post == "1":
                        break  
                    elif opcion_post == "2":
                        continue  
                    else:
                        self.salir()
                        return
            else:
                self.salir()
                break

    def ejecutarPrograma(self):
        self.menu()
        cantidad_monedas = self.solicitarCantidadMonedas()
        conversiones = []
        for i in range(cantidad_monedas):
            moneda_digitada = f"Ingrese la moneda {i+1}:"
            moneda_base = self.solicitarMoneda(moneda_digitada)
            while not self.validarMoneda(moneda_base):
                moneda_base = self.solicitarMoneda(moneda_digitada)
            self.mostrarTablaTasas(moneda_base)
            destino_digitada = f"Ingrese la moneda destino para convertir {moneda_base}:"
            moneda_destino = self.solicitarMoneda(destino_digitada)
            while True:
                if moneda_destino == moneda_base:
                    self.console.print("\n[bold red]La moneda destino debe ser diferente a la moneda base.[/bold red]")
                    moneda_destino = self.solicitarMoneda(destino_digitada)
                    continue
                if not self.validarMoneda(moneda_destino):
                    moneda_destino = self.solicitarMoneda(destino_digitada)
                    continue
                break
            cantidad_valor = self.solicitarCantidad(moneda_base)
            conversiones.append((moneda_base, moneda_destino, cantidad_valor))
        for moneda_base, moneda_destino, cantidad in conversiones:
            self.mostrarValorCambio(moneda_base, moneda_destino, cantidad)

    def menu(self):
        self.console.print("\n[bold magenta]Bienvenido a nuestra plataforma para cambio de divisa:[/bold magenta]")
        self.console.print("\n[bold magenta]Monedas Soportadas:[/bold magenta]\n")
        table = Table(show_header=False)
        num_columnas = 6
        for _ in range(num_columnas):
            table.add_column(justify="center", style="cyan", no_wrap=True)
        for i in range(0, len(self.divisas), num_columnas):
            row = self.divisas[i:i+num_columnas]
            row += [""] * (num_columnas - len(row))
            table.add_row(*row)
        self.console.print(table)

    def solicitarCantidadMonedas(self):
        cantidad_str = self.console.input("\n[bold cyan]¿Cuántas monedas deseas seleccionar? (1 o 2): [/bold cyan]")
        try:
            cantidad = int(cantidad_str)
            if cantidad in [1, 2]:
                return cantidad
            else:
                self.console.print("[bold red]Solo se permite seleccionar 1 o 2 monedas.[/bold red]")
                return self.solicitarCantidadMonedas()
        except ValueError:
            self.console.print("[bold red]Por favor, ingrese un número válido (1 o 2).[/bold red]")
            return self.solicitarCantidadMonedas()

    def solicitarMoneda(self, mensaje):
        return self.console.input(f"[bold cyan]{mensaje} [/bold cyan]").upper()

    def solicitarCantidad(self, moneda):
        cantidad_str = self.console.input(f"[bold cyan]Ingrese la cantidad de {moneda}: [/bold cyan]")
        try:
            cantidad = float(cantidad_str)
        except ValueError:
            self.console.print("[bold red]Por favor ingrese un número válido (Para dígitos decimales use '.' ).[/bold red]")
            return self.solicitarCantidad(moneda)
        if cantidad <= 0:
            self.console.print("[bold red]Por favor ingrese un número mayor a 0.[/bold red]")
            return self.solicitarCantidad(moneda)
        return cantidad

    def validarMoneda(self, moneda):
        if moneda in self.divisas:
            self.console.print(f"\n[bold green]Ha seleccionado:[/bold green] [yellow]{moneda}[/yellow] 🎉")
            return True
        else:
            self.console.print(f"\n[bold red]Moneda no válida:[/bold red] [yellow]Por favor seleccione una opción de la tabla[/yellow] ❌")
            return False

    def mostrarTablaTasas(self, moneda_base):
        self.console.print(f"\n[bold magenta]Tasas de Cambio (Base: {moneda_base}):[/bold magenta]\n")
        tasas_cambio = self.cambio.obtenerTasasCambio(moneda_base).get("data", {})
        if moneda_base not in tasas_cambio:
            self.console.print(f"[bold red]Error:[/bold red] La moneda base {moneda_base} no se encuentra en las tasas de cambio.")
            return
        valor_base = tasas_cambio[moneda_base]
        pares = []
        for moneda, valor in tasas_cambio.items():
            tasa = valor / valor_base
            pares.append((moneda, f"{tasa:.{int(self.cantidad_digitos)}f}"))
        table = Table(show_header=True)
        for _ in range(6):
            table.add_column("Moneda", justify="center", style="cyan", no_wrap=True)
            table.add_column("Valor", justify="center", style="yellow", no_wrap=True)
        for i in range(0, len(pares), 6):
            chunk = pares[i:i+6]
            fila = []
            for moneda, tasa in chunk:
                fila.append(moneda)
                fila.append(tasa)
            if len(chunk) < 6:
                for _ in range(6 - len(chunk)):
                    fila.extend(["", ""])
            table.add_row(*fila)
        self.console.print(table)

    def mostrarValorCambio(self, moneda_base, moneda_destino, cantidad):
        self.console.print(f"\n[bold magenta]Conversión: {cantidad} {moneda_base} a {moneda_destino}:[/bold magenta]\n")
        tasas_cambio = self.cambio.obtenerTasasCambio(moneda_base).get("data", {})
        if moneda_destino not in tasas_cambio:
            self.console.print(f"[bold red]Error:[/bold red] No se encontró la tasa de cambio para {moneda_destino}.")
            return
        tasa = tasas_cambio[moneda_destino]
        conversion = tasa * cantidad

        self.historial.guardarConversion(moneda_base, moneda_destino, cantidad, conversion, tasa)

        table = Table(show_header=True)
        table.add_column(moneda_base, justify="center", style="cyan", no_wrap=True)
        table.add_column(moneda_destino, justify="center", style="yellow", no_wrap=True)
        table.add_row(f"{cantidad:.{self.cantidad_digitos}f}", f"{conversion:.{self.cantidad_digitos}f}")
        self.console.print(table)

    def mostrarHistorial(self):
        historial = self.historial.obtenerHistorial()
        if not historial:
            self.console.print("[bold red]No hay historial de conversiones.[/bold red]")
            return
        self.console.print("\n[bold magenta]Historial de Conversiones:[/bold magenta]\n")
        for idx, registro in enumerate(historial, start=1):
            moneda_base = registro["moneda_base"]
            moneda_destino = registro["moneda_destino"]
            cantidad = float(registro["cantidad"])
            conversion = float(registro["conversion"])
            self.console.print(f"[bold green]Conversión {idx}: Base: {moneda_base}, Destino: {moneda_destino}, Cantidad: {cantidad}[/bold green]")
            table = Table(show_header=True)
            table.add_column(moneda_base, justify="center", style="cyan", no_wrap=True)
            table.add_column(moneda_destino, justify="center", style="yellow", no_wrap=True)
            table.add_row(f"{cantidad:.{self.cantidad_digitos}f}", f"{conversion:.{self.cantidad_digitos}f}")
            self.console.print(table)

    def menuPostConversion(self):
        self.console.print("\n[bold magenta]Opciones:[/bold magenta]")
        self.console.print("[bold cyan]1.[/bold cyan] Volver a ejecutar el programa")
        self.console.print("[bold cyan]2.[/bold cyan] Mostrar historial de conversiones")
        self.console.print("[bold cyan]3.[/bold cyan] Salir")
        opcion = self.console.input("\n[bold cyan]Seleccione una opción: [/bold cyan]")
        if opcion not in ["1", "2", "3"]:
            self.console.print("[bold red]Error:[/bold red] Seleccione una opción válida.")
            return self.menuPostConversion()
        return opcion

    def salir(self):
        self.console.print("\n[bold magenta]Gracias por usar nuestra plataforma para cambio de divisa. ¡Hasta la próxima! 🚀[/bold magenta]")
