import random

def obtener_opcion_usuario():
    while True:
        opcion = input("Elige una opción (piedra, papel, tijera): ").lower()
        if opcion in ["piedra", "papel", "tijera"]:
            return opcion
        else:
            print("Opción no válida. Por favor, elige piedra, papel o tijera.")

def obtener_opcion_computadora():
    opciones = ["piedra", "papel", "tijera"]
    return random.choice(opciones)

def determinar_ganador(usuario, computadora):
    if usuario == computadora:
        return "Empate"
    elif (usuario == "piedra" and computadora == "tijera") or (usuario == "tijera" and computadora == "papel") or (usuario == "papel" and computadora == "piedra"):
        return "Usuario"
    else:
        return "Computadora"

while True:
    opcion_usuario = obtener_opcion_usuario()
    opcion_computadora = obtener_opcion_computadora()

    print(f"Usuario eligió: {opcion_usuario}")
    print(f"Computadora eligió: {opcion_computadora}")

    ganador = determinar_ganador(opcion_usuario, opcion_computadora)
    print(f"Ganador: {ganador}")

    if ganador != "Empate":
        break

print("Gracias por jugar.")
