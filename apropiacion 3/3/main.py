mi_lista = []

while True:
    print("\nAplicaciones con Listas:")
    print("1. Ingresar lista nueva")
    print("2. Ordenar lista")
    print("3. Promedio lista")
    print("4. Buscar elemento")
    print("5. Salir")

    opcion = input("Elija una opción: ")

    if opcion == "1":
        mi_lista = input("Ingrese la lista separada por espacios: ").split()
        mi_lista = [int(x) for x in mi_lista]
        print("Lista ingresada:", mi_lista)
    elif opcion == "2":
        mi_lista.sort()
        print("Lista ordenada:", mi_lista)
    elif opcion == "3":
        promedio = sum(mi_lista) / len(mi_lista) if mi_lista else 0
        print("Promedio de la lista:", promedio)
    elif opcion == "4":
        elemento = int(input("Ingrese el elemento a buscar: "))
        if elemento in mi_lista:
            print(f"El elemento {elemento} se encuentra en la lista.")
        else:
            print(f"El elemento {elemento} no se encuentra en la lista.")
    elif opcion == "5":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida.")
