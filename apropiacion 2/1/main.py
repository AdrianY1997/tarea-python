def calcular_tiempo_ancho_banda(con_vel, file_size):
    if con_vel > 20:
        velocidad_descarga = 10
    elif con_vel > 5:
        velocidad_descarga = 5
    else:
        velocidad_descarga = 1

    tiempo_descarga = file_size / (velocidad_descarga / 8)
    ancho_banda_utilizado = velocidad_descarga

    return tiempo_descarga, ancho_banda_utilizado

con_vel_user = input("Ingrese la velocidad de su conexión: ")
file_size = input("Ingrese el tamaño del archivo: ")

time, bw = calcular_tiempo_ancho_banda(int(con_vel_user), int(file_size))

print(f"Tiempo de descarga: {time:.2f} segundos")
print(f"Ancho de banda utilizado: {bw} Mbps")
