import calculadora

while True:
    print("\nMenú de Calculadora:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Operación")
    print("6. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        numeros = input("Ingresa los números a sumar separados por espacios: ").split()
        numeros = [float(num) for num in numeros]
        resultado = calculadora.sumar(*numeros)
        print(f"Resultado: {resultado}")
    elif opcion == "2":
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        resultado = calculadora.restar(num1, num2)
        print(f"Resultado: {resultado}")
    elif opcion == "3":
        numeros = input("Ingresa los números a multiplicar separados por espacios: ").split()
        numeros = [float(num) for num in numeros]
        resultado = calculadora.multiplicar(*numeros)
        print(f"Resultado: {resultado}")
    elif opcion == "4":
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        resultado = calculadora.dividir(num1, num2)
        print(f"Resultado: {resultado}")
    elif opcion == "5":
        num1 = float(input("Ingresa el primer número: "))
        operador = input("Ingresa el operador (+, -, *, /): ")
        num2 = float(input("Ingresa el segundo número: "))
        resultado = calculadora.operacion(num1, operador, num2)
        print(f"Resultado: {resultado}")
    elif opcion == "6":
        break
    else:
        print("Opción no válida. Por favor, elige una opción del menú.")
