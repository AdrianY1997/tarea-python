def separar_pares_impares(lista_numeros):
    pares = []
    impares = []

    for numero in lista_numeros:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)

    return sorted(pares), sorted(impares)

# Ejemplo de uso
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares, impares = separar_pares_impares(lista_numeros)
print("Números pares:", pares)
print("Números impares:", impares)
