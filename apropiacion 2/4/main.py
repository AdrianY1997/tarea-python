def determinar_anemia(edad, sexo, nivel_hemoglobina):
    if edad <= 1 / 12:
        rango_hemoglobina = (10, 26) 
    elif 1 / 12 < edad <= 6 / 12:
        rango_hemoglobina = (10, 18) 
    elif 6 / 12 < edad <= 12 / 12:
        rango_hemoglobina = (11, 15) 
    elif 1 < edad <= 5:
        rango_hemoglobina = (11.5, 15) 
    elif 5 < edad <= 10:
        rango_hemoglobina = (12.6, 15.5) 
    elif 10 < edad <= 15:
        rango_hemoglobina = (12, 15.5) 
    elif sexo == "mujer" and edad > 15:
        rango_hemoglobina = (12, 16) 
    elif sexo == "hombre" and edad > 15:
        rango_hemoglobina = (14, 18) 
    else:
        print("No se dispone de rangos para esta edad y sexo.")
        return

    if nivel_hemoglobina < rango_hemoglobina[0] or nivel_hemoglobina > rango_hemoglobina[1]:
        resultado = "Positivo (anemia)"
    else:
        resultado = "Negativo (sin anemia)"

    print(f"Resultado para una persona de {edad} años, sexo {sexo}, y nivel de hemoglobina {nivel_hemoglobina} g%: {resultado}")

edad_persona = input("Ingrese su edad: ")
sexo_persona = input("Ingrese su sexo: ")
nivel_hemoglobina_persona = input("Ingrese su nivel de hemoglobina: ")

determinar_anemia(int(edad_persona), sexo_persona, float(nivel_hemoglobina_persona))
