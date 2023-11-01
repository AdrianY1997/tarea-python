def contar_letras(palabra):
    contador = {}
    for letra in palabra:
        if letra in contador:
            contador[letra] += 1
        else:
            contador[letra] = 1
    return contador

palabra = input("Digite una palabra: ")
resultado = contar_letras(palabra)
print(resultado)
