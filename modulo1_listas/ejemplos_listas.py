# Módulo 1: Listas
# Una lista permite guardar varios datos en una sola variable y se puede modificar.

frutas = ["manzana", "banano", "pera"]
print("Lista inicial:", frutas)

# Agregar un elemento
frutas.append("uva")
print("Después de agregar uva:", frutas)

# Acceder a un elemento por posición
print("Primera fruta:", frutas[0])

# Modificar un elemento
frutas[1] = "mango"
print("Después de cambiar banano por mango:", frutas)

# Eliminar un elemento
frutas.remove("pera")
print("Después de eliminar pera:", frutas)

# Recorrer una lista
print("Recorrido de la lista:")
for fruta in frutas:
    print("-", fruta)
