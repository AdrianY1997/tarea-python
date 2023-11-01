n = int(input("Cuántos elementos desea ingresar en la lista: "))

mi_lista = []

for i in range(n):
    elemento = input(f"Ingrese el elemento {i + 1}: ")
    mi_lista.append(elemento)

print("Lista original:", mi_lista)

mi_lista_invertida = mi_lista[::-1]

print("Lista invertida:", mi_lista_invertida)
