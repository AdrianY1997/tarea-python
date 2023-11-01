def agregar_una_vez(lista, elemento):
    try:
        if elemento in lista:
            raise ValueError(f"Error: Imposible añadir elementos duplicados => {elemento}")
        lista.append(elemento)
    except ValueError as error:
        print(error)

mi_lista = [1, 2, 3, 4]
elemento = 2
agregar_una_vez(mi_lista, elemento)
print("Gracias por usar este programa")
