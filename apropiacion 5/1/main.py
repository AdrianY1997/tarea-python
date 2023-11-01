mi_lista = [10, 20, 30, 40, 50]

while True:
    try:
        posicion = input("Ingrese una posición de la lista: ")
        posicion = int(posicion)

        if 0 <= posicion < len(mi_lista):
            valor = mi_lista[posicion]
            print(f"El valor en la posición {posicion} es: {valor}")
            break
        else:
            print("La posición está fuera de rango. Intente nuevamente.")
    except ValueError:
        print("Debe ingresar un número entero como posición.")
    except IndexError:
        print("La posición no existe en la lista. Intente nuevamente.")
