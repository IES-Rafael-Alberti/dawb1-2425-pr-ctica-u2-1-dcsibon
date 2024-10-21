import os


COMANDOS = ("compra", "venta", "saldo", "reset", "deshacer", "limpiar", "fin")
MENSAJE_ERROR = "*ERROR* Entrada inválida"


def limpiar_pantalla():
    """
    Limpia la consola según el sistema operativo.

    En sistemas Windows utiliza el comando 'cls', en Linux o macOS utiliza 'clear'.
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def comprobar_importe(valor: str) -> bool:
    """
    Verifica si el importe proporcionado es un número válido.

    Args:
        valor (str): Cadena que representa el importe a verificar.

    Returns:
        bool: True si el valor es un número válido (positivo, negativo o con punto decimal), False en caso contrario.
    """
    if valor.startswith("-"):
        valor = valor[1:]

    if valor.count(".") > 1:
        return False

    valor = valor.replace(".", "")
    return valor.isdigit()


def comprobar_comando(comando: str) -> bool:
    """
    Verifica si el comando está dentro de la lista de comandos válidos.

    Args:
        comando (str): Cadena que representa el comando ingresado por el usuario.

    Returns:
        bool: True si el comando está en la lista de comandos válidos, False en caso contrario.
    """
    return comando in COMANDOS


def mostrar_mensaje_error():
    """
    Muestra el mensaje de error por entrada inválida.
    """
    print(MENSAJE_ERROR)


def procesar_compra(saldo: float, importe: float) -> float:
    """
    Procesa una operación de compra y retorna el saldo actualizado restando el importe.

    Args:
        saldo (float): El saldo actual.
        importe (float): El importe a restar por la compra.

    Returns:
        float: El saldo actualizado después de realizar la compra.
    """
    return saldo - importe


def procesar_venta(saldo: float, importe: float) -> float:
    """
    Procesa una operación de venta y retorna el saldo actualizado sumando el importe.

    Args:
        saldo (float): El saldo actual.
        importe (float): El importe a sumar por la venta.

    Returns:
        float: El saldo actualizado después de realizar la venta.
    """
    return saldo + importe


def mostrar_saldo(saldo: float, cont_compras: int, cont_ventas: int):
    """
    Muestra el saldo actual junto con el número de compras y ventas.

    Args:
        saldo (float): El saldo actual.
        cont_compras (int): Número total de compras realizadas.
        cont_ventas (int): Número total de ventas realizadas.
    """
    print(f"Saldo actual = {saldo:.2f} ({cont_compras} compras y {cont_ventas} ventas)")


def resetear_saldo(saldo: float, cont_compras: int, cont_ventas: int) -> tuple[float, int, int]:
    """
    Retorna el saldo y las operaciones realizadas, mostrando antes el saldo anterior.

    Se utiliza simplemente porque no hemos llegado a las estructuras de datos aún. 
    
    Podríamos haberlo realizado directamente en el main:
    saldo = 0
    cont_compras = 0
    cont_ventas = 0

    Returns:
        tuple[float, int, int]: El nuevo saldo (0), número de compras (0) y número de ventas (0) después del reinicio.
    """
    print(f"Saldo anterior = {saldo:.2f} ({cont_compras} compras y {cont_ventas} ventas)")
    return 0, 0, 0


def recuperar_comando_e_importe(linea: str) -> tuple[str, str]:
    """
    Recupera el comando y, si lo hay, el importe de una línea de entrada.
    
    Args:
        linea (str): Línea de texto introducida por el usuario.

    Returns:
        tuple: El comando (str o  None) y el importe (str o None).
    
    Ejemplos:
        >>> recuperar_comando_e_importe("compra 100")
        ('compra', '100')
        
        >>> recuperar_comando_e_importe("saldo")
        ('saldo', None)

        >>> recuperar_comando_e_importe("")
        (None, None)        
    """
    lista_palabras = linea.split()

    if len(lista_palabras) == 1:
        return lista_palabras[0], None
    elif len(lista_palabras) == 2:
        return lista_palabras[0], lista_palabras[1]
    else:
        return None, None


def guardar_valores(saldo, compras, ventas) -> tuple[float, int, int]:
    """
    Usar la función para agrupar las actualizaciones de saldo, compras y ventas. 
    
    Cómo aún no hemos visto los diccionarios no podemos usar esta estructura de datos.

    Args:
        saldo (float): El saldo.
        compras (int): Número de compras.
        ventas (int): Número de ventas.

    Returns:
        tuple: Una tupla con el saldo, número de compras y número de ventas.
    """
    return saldo, compras, ventas


def main():
    """
    Función principal que gestiona el flujo del programa. El programa permite al usuario realizar
    operaciones de compra y venta, consultar el saldo, restablecer las operaciones y finalizar.

    Funciona a través de un bucle que sigue las instrucciones del usuario hasta que el comando "fin" es ingresado.
    El saldo y las transacciones se actualizan según los comandos introducidos.

    Comandos disponibles:
        - compra [importe]: Resta el importe del saldo.
        - venta [importe]: Suma el importe al saldo.
        - saldo: Muestra el saldo actual junto con el número de compras y ventas.
        - reset: Restablece el saldo y las transacciones a cero.
        - fin: Termina el programa.
    
    Ejemplos:
        > compra 100
        > venta 50
        > saldo
        Saldo actual = -50.00 (1 compras y 1 ventas)
        > venta 200
        > reset
        Saldo anterior = 150.00 (1 compras y 2 ventas)
        >
        Saldo actual = 0.00 (0 compras y 0 ventas)
        > fin
    """
    encuentra_fin = False
    cont_compras = 0
    cont_ventas = 0
    saldo = 0

    # Guardar los valores previos para deshacer
    ultimo_saldo = 0
    ultimo_cont_compras = 0
    ultimo_cont_ventas = 0    

    while not encuentra_fin:
        linea = input("> ").strip().lower()
        comando, importe = recuperar_comando_e_importe(linea)

        importe_valido = importe is not None and comprobar_importe(importe)

        if comando in ("compra", "venta") and importe_valido:
            # Guardar el estado previo para deshacer
            ultimo_saldo, ultimo_cont_compras, ultimo_cont_ventas = guardar_valores(saldo, cont_compras, cont_ventas)
            # Es lo mismo que hacer esto...
            # ultimo_saldo = saldo
            # ultimo_cont_compras = cont_compras
            # ultimo_cont_ventas = cont_ventas

            importe = float(importe)

            if comando == "compra":
                saldo = procesar_compra(saldo, importe)
                cont_compras += 1

            elif comando == "venta":
                saldo = procesar_venta(saldo, importe)
                cont_ventas += 1

        elif comando in ("saldo", "reset", "deshacer", "limpiar", "fin") and importe is None:

            if comando == "saldo":
                mostrar_saldo(saldo, cont_compras, cont_ventas)

            elif comando == "reset":
                # Guardar el estado previo para deshacer
                ultimo_saldo, ultimo_cont_compras, ultimo_cont_ventas = guardar_valores(saldo, cont_compras, cont_ventas)
                # Es lo mismo que hacer esto...
                # ultimo_saldo = saldo
                # ultimo_cont_compras = cont_compras
                # ultimo_cont_ventas = cont_ventas

                saldo, cont_compras, cont_ventas = resetear_saldo(saldo, cont_compras, cont_ventas)
                # Es lo mismo que hacer esto...
                # print(f"Saldo anterior = {saldo:.2f} ({cont_compras} compras y {cont_ventas} ventas)")
                # saldo = 0
                # cont_compras = 0
                # cont_ventas = 0

            elif comando == "deshacer":
                saldo, cont_compras, cont_ventas = guardar_valores(ultimo_saldo, ultimo_cont_compras, ultimo_cont_ventas)
                # Es lo mismo que hacer esto...
                # saldo = ultimo_saldo
                # cont_compras = ultimo_cont_compras
                # cont_ventas = ultimo_cont_ventas
                print("Última operación deshecha.")

            elif comando == "limpiar":
                limpiar_pantalla()

            else:
                encuentra_fin = True

        else:
            mostrar_mensaje_error()


            
if __name__ == "__main__":
    main()