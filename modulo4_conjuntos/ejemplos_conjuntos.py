# Módulo 4: Conjuntos
# Un conjunto guarda elementos únicos, no repetidos.

numeros = {1, 2, 3, 3, 4, 4, 5}
print("Conjunto sin repetidos:", numeros)

# Agregar elemento
numeros.add(6)
print("Después de agregar 6:", numeros)

# Eliminar elemento
numeros.discard(2)
print("Después de eliminar 2:", numeros)

# Operaciones entre conjuntos
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Unión:", a | b)
print("Intersección:", a & b)
print("Diferencia:", a - b)
