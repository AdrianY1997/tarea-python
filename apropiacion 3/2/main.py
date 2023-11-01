
frase1 = input("Ingrese la primera frase: ")
frase2 = input("Ingrese la segunda frase: ")

letras_repetidas = []

if len(frase1) != len(frase2):
    print("Las frases no tienen la misma longitud.")
else:

    for i in range(len(frase1)):
        if frase1[i] == frase2[i]:
            letras_repetidas.append(frase1[i])


    if len(letras_repetidas) > 0:
        print("Letras repetidas en la misma posición:", letras_repetidas)
    else:
        print("No hay letras repetidas en la misma posición en las frases.")
