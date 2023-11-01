def inspeccionar_pieza(entrada_binaria):
    if '0' in entrada_binaria:
        print("La pieza ha sido rechazada debido a estándares de calidad no cumplidos.")
    else:
        print("La pieza ha sido aprobada y cumple con los estándares de calidad.")

entrada = input("Ingrese la calificación de calidad: ")

inspeccionar_pieza(entrada)
