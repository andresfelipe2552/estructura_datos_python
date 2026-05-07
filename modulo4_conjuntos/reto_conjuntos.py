# Reto Módulo 4: Conjuntos
# Comparar estudiantes inscritos en dos cursos.

python = {"Ana", "Luis", "Carlos", "Marta"}
javascript = {"Carlos", "Marta", "Sofía", "Andrés"}

print("Estudiantes de Python:", python)
print("Estudiantes de JavaScript:", javascript)

print("Todos los estudiantes:", python | javascript)
print("Estudiantes en ambos cursos:", python & javascript)
print("Solo en Python:", python - javascript)
print("Solo en JavaScript:", javascript - python)
