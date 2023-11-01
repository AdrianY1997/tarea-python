diccionario_frutas = {}

while True:
    fruta = input("Ingrese el nombre de una fruta en español (o 'salir' para finalizar): ").lower()

    if fruta == "salir":
        break

    if fruta in diccionario_frutas:
        traduccion = diccionario_frutas[fruta]
        print(f"Traducción al inglés: {traduccion}")
    else:
        print("La fruta no está en el diccionario.")
        agregar = input("¿Desea agregar la fruta al diccionario? (s/n): ").lower()
        if agregar == "s":
            traduccion_nueva = input(f"Ingrese la traducción de '{fruta}' al inglés: ").lower()
            diccionario_frutas[fruta] = traduccion_nueva
            print(f"'{fruta}' ha sido agregada al diccionario como '{traduccion_nueva}'.")

print("Hasta luego.")
