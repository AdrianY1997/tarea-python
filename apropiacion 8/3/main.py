def numeros_pares_hasta_n(numero):
    if numero < 1:
        return
    if numero % 2 == 0:
        print(numero)
    numeros_pares_hasta_n(numero - 1)

numero = int(input("Ingrese un número: "))
print("Números pares hasta", numero)
numeros_pares_hasta_n(numero)
