import random

palabras = []
intentos_permitidos = 6

def agregar_palabra():
    palabra = input("Ingresa una palabra: ")
    palabras.append(palabra)
    print("Palabra agregada con éxito.")

def configurar():
    global intentos_permitidos
    try:
        intentos = int(input("Ingresa el número de intentos permitidos: "))
        if intentos > 0:
            intentos_permitidos = intentos
            print(f"Intentos permitidos configurados a {intentos_permitidos}.")
        else:
            print("El número de intentos debe ser mayor que 0.")
    except ValueError:
        print("Por favor, ingresa un número válido.")

def seleccionar_palabra():
    return random.choice(palabras)

def jugar():
    palabra_secreta = seleccionar_palabra()
    palabra_adivinada = ["_"] * len(palabra_secreta)
    intentos = 0

    print("¡Bienvenido al juego del ahorcado!")

    while intentos < intentos_permitidos and "_" in palabra_adivinada:
        letra = input("Adivina una letra: ").lower()

        if len(letra) == 1 and letra.isalpha():
            acierto = False
            for i in range(len(palabra_secreta)):
                if palabra_secreta[i] == letra:
                    palabra_adivinada[i] = letra
                    acierto = True

            if acierto:
                print("¡Adivinaste una letra!")
            else:
                intentos += 1
                print(f"Letra incorrecta. Te quedan {intentos_permitidos - intentos} intentos.")

            print("Palabra actual: " + " ".join(palabra_adivinada))
        else:
            print("Ingresa una letra válida.")

    if "_" not in palabra_adivinada:
        print("¡Felicidades! Ganaste. La palabra era: " + palabra_secreta)
    else:
        print("¡Perdiste! La palabra era: " + palabra_secreta)

while True:
    print("\nMenú del juego del ahorcado:")
    print("1. Agregar Palabra")
    print("2. Configurar")
    print("3. Jugar")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        agregar_palabra()
    elif opcion == "2":
        configurar()
    elif opcion == "3":
        jugar()
    elif opcion == "4":
        break
    else:
        print("Opción no válida. Por favor, elige una opción del menú.")
