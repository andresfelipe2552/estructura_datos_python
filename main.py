# Integración final de estructuras de datos
# Mini sistema de registro de aprendices.

aprendices = [
    {"nombre": "Ana", "notas": [4.5, 4.0, 5.0], "curso": "Python"},
    {"nombre": "Luis", "notas": [3.2, 3.8, 4.0], "curso": "Python"},
    {"nombre": "Marta", "notas": [5.0, 4.8, 4.7], "curso": "JavaScript"}
]

cursos = {aprendiz["curso"] for aprendiz in aprendices}

print("Cursos registrados:", cursos)
print("Reporte de aprendices")
print("---------------------")

for aprendiz in aprendices:
    nombre = aprendiz["nombre"]
    notas = aprendiz["notas"]
    promedio = sum(notas) / len(notas)
    estado = "Aprobado" if promedio >= 3.5 else "No aprobado"
    print(f"{nombre} | Curso: {aprendiz['curso']} | Promedio: {round(promedio, 2)} | {estado}")
