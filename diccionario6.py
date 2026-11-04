estudiantes = []
cantidad = int(input("Cantidad de estudiantes: "))

for i in range(cantidad):
    estudiante = {}
    estudiante["nombre"] = input("Nombre: ")
    estudiante["promedio"] = float(input("Promedio: "))
    estudiantes.append(estudiante)

for estudiante in estudiantes:
    print(estudiante)

mejor = estudiantes[0]

for estudiante in estudiantes:
    if estudiante["promedio"] > mejor["promedio"]:
        mejor = estudiante

print("Mejor estudiante:", mejor["nombre"])
print("Promedio:", mejor["promedio"])