
def validar_edad(edad: int):
    if edad < 0:
        raise ValueError("La edad debe ser un número positivo.")
    if edad == 0:
        raise ValueError("La edad debe ser un número positivo mayor que cero.")
    if edad > 125:
        raise ValueError("La edad debe ser un número inferior o igual a 125.")


def pedir_edad() -> int:
    edad = None
    while edad is None:
        try:
            edad = int(input("Introduce tu edad: "))
            validar_edad(edad)
        except ValueError as e:
            if edad is None:
                print(f"*ERROR* El número introducido no es un entero válido. Inténtalo de nuevo.")
            else:
                print(f"*ERROR* {e}. Inténtalo de nuevo.")

    return edad


def mostrar_anios_cumplidos(edad: int):
    for i in range(1, edad + 1):
        if i == edad:
            print(i)
        else:
            print(i, end=", ")


def main():
    edad = pedir_edad()
    print(f"Has cumplido los siguientes años:")
    mostrar_anios_cumplidos(edad)


if __name__ == "__main__":
    main()