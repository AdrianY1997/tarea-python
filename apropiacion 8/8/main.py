estudiantes = []

for i in range(5):
    print(f"Ingrese la información del estudiante {i + 1}:")
    id_estudiante = input("ID: ")
    nombre_estudiante = input("Nombre: ")
    edad_estudiante = input("Edad: ")
    nota_estudiante = input("Nota: ")

    estudiante = {
        "id": id_estudiante,
        "nombre": nombre_estudiante,
        "edad": edad_estudiante,
        "nota": nota_estudiante
    }
    estudiantes.append(estudiante)

print("\n(a) Información de todos los estudiantes:")
for estudiante in estudiantes:
    print("ID:", estudiante["id"])
    print("Nombre:", estudiante["nombre"])
    print("Edad:", estudiante["edad"])
    print("Nota:", estudiante["nota"])
    print()

id_buscar = input("Ingrese el ID del estudiante que desea buscar: ")
encontrado = False

for estudiante in estudiantes:
    if estudiante["id"] == id_buscar:
        encontrado = True
        print(f"\n(b) Información del estudiante con ID {id_buscar}:")
        print("Nombre:", estudiante["nombre"])
        print("Edad:", estudiante["edad"])
        print("Nota:", estudiante["nota"])
        break

if not encontrado:
    print("Estudiante no encontrado.")
