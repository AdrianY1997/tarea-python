import random

def adivina_el_numero():
    numero_secreto = random.randint(0, 10)
    oportunidades = 3

    print("¡Bienvenido al juego de Adivina el Número!")
    print("Tienes 3 oportunidades para adivinar un número entre 0 y 10.")

    for _ in range(oportunidades):
        intento = int(input("Introduce tu suposición: "))
        if intento == numero_secreto:
            print("¡Felicidades! Adivinaste el número.")
            break
        else:
            print("Número incorrecto. ¡Inténtalo de nuevo!")

    else:
        print(f"El número secreto era {numero_secreto}. ¡El juego ha terminado!")
        
    input("Gracias por jugar, presione cualquier tecla...")

if __name__ == "__main__":
    adivina_el_numero()
