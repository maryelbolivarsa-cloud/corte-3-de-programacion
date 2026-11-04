estudiante = {"nombre": "Laura Gomez","promedio": 4.2]

def mostrar_estudiante(estudiante):
    print("Nombre:", estudiante["nombre"])
    print("Promedio:", estudiante["promedio"])


def aprobo(estudiante):
    return estudiante["promedio"] >= 3.0

mostrar_esudiante(estudiante)
print("Aprobo:", aprobo(estudiante))

