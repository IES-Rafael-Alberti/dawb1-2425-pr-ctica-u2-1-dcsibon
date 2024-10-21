def fahr2cel(fahr:float) -> float:
    ''' Convertir grados Fahrenheit a grados Celsius'''
    if fahr < -459.67:
        raise ValueError('Temperatura Fahrenheit incorrecta: ' + str(fahr))

    cel = (fahr - 32.0) * 5.0 / 9.0
    return cel


def main():
    numero_correcto = False
    fahr = None
    while not numero_correcto:
        try:
            ent = input("Introduzca la Temperatura Fahrenheit:")
            fahr = float(ent)
            cel = fahr2cel(fahr)
            numero_correcto = True
        except ValueError:   # Si no se puede convertir a float
            if fahr == None:
                print("Por favor introduzca un número.")
            else:
                print("La temperatura Fahrenheit es incorrecta: " + str(fahr))

    print(cel)


if __name__ == "__main__":
    main()
