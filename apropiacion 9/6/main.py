futbol = set()
baloncesto = set()

todos_estudiantes = set()

n = int(input("Ingrese la cantidad de estudiantes: "))

for i in range(n):
    nombre_estudiante = input(f"Ingrese el nombre del estudiante {i + 1}: ")
    inscripcion_futbol = input("¿Inscribir en fútbol? (s/n): ")
    inscripcion_baloncesto = input("¿Inscribir en baloncesto? (s/n): ")

    if inscripcion_futbol == "s":
        futbol.add(nombre_estudiante)
        todos_estudiantes.add(nombre_estudiante)

    if inscripcion_baloncesto == "s":
        baloncesto.add(nombre_estudiante)
        todos_estudiantes.add(nombre_estudiante)

inscritos_en_futbol = futbol
inscritos_en_baloncesto = baloncesto
inscritos_en_ambos_deportes = futbol & baloncesto
inscritos_en_algun_deporte = futbol | baloncesto
inscritos_en_solo_un_deporte = (futbol | baloncesto) - (futbol & baloncesto)

print("\nEstudiantes inscritos en fútbol:", inscritos_en_futbol)
print("Estudiantes inscritos en baloncesto:", inscritos_en_baloncesto)
print("Estudiantes inscritos en ambos deportes:", inscritos_en_ambos_deportes)
print("Todos los estudiantes inscritos en algún deporte:", inscritos_en_algun_deporte)
print("Estudiantes inscritos en solo un deporte:", inscritos_en_solo_un_deporte)
