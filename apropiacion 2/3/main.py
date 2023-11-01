def calcular_descuento_precio(estrato, edad, valor_matricula):
    if estrato == 1:
        if edad < 18:
            descuento = 0.20
        else:
            descuento = 0.15
    elif estrato == 2:
        if edad < 18:
            descuento = 0.10
        else:
            descuento = 0.05
    else:
        descuento = 0

    precio_con_descuento = valor_matricula * (1 - descuento)
    valor_descuento = valor_matricula * descuento

    return precio_con_descuento, valor_descuento

estrato_estudiante = input("Ingrese su estrato: ")
edad_estudiante = input("Ingrese su edad: ")
valor_matricula = input("Ingrese el valor de su matricula: ")

precio_final, descuento_aplicado = calcular_descuento_precio(int(estrato_estudiante), int(edad_estudiante), int(valor_matricula))

print(f"Precio de matrícula con descuento: ${precio_final:.2f}")
print(f"Descuento aplicado: ${descuento_aplicado:.2f}")
