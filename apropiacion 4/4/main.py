def numeros_a_palabras(numero):
    numeros = {
        '0': 'cero',
        '1': 'uno',
        '2': 'dos',
        '3': 'tres',
        '4': 'cuatro',
        '5': 'cinco',
        '6': 'seis',
        '7': 'siete',
        '8': 'ocho',
        '9': 'nueve'
    }
    
    numero_str = str(numero)
    nombres = [numeros[digito] for digito in numero_str]
    
    return " - ".join(nombres)

numero = int(input("Ingrese un número: "))
resultado = numeros_a_palabras(numero)
print(resultado)
