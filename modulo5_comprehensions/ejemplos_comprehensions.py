# Módulo 5: Comprehensions
# Sirven para crear listas, diccionarios o conjuntos de forma corta.

numeros = [1, 2, 3, 4, 5]

cuadrados = [numero ** 2 for numero in numeros]
print("Cuadrados:", cuadrados)

pares = [numero for numero in numeros if numero % 2 == 0]
print("Números pares:", pares)

precios = [1000, 2000, 3000]
precios_con_iva = [precio * 1.19 for precio in precios]
print("Precios con IVA:", precios_con_iva)

# Diccionario con comprehension
tabla = {numero: numero * 2 for numero in numeros}
print("Tabla del doble:", tabla)
