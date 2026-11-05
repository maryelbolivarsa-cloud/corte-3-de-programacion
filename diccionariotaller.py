# Ejercicio 1
producto = {
    "codigo": "P001",
    "nombre": "Teclado Mecánico",
    "precio": 45.0,
    "stock": 15
}
print("Datos del producto")
for clave, valor in producto.items():
    print(clave, ":", valor)
# Ejercicio 2
inventario = {
    "P001": "Teclado",
    "P002": "Mouse",
    "P003": "Monitor"
}
print("Búsqueda en inventario")
codigo_buscar = input("Ingrese el código a buscar (ej: P001): ")
if codigo_buscar in inventario:
    nombre_producto = inventario[codigo_buscar]
    print("El producto", nombre_producto, "sí existe en el inventario.")
else:
    print("El código no existe en el inventario.")
# Ejercicio 3
materias_notas = {
    "Matemáticas financieras": 4.5,
    "Programación": 4.8,
    "Conjuntos y combinatoria": 3.0,
    "Cálculo diferencial": 4.2,
    "Álgebra lineal": 4.5
}
promedio = sum(materias_notas.values()) / len(materias_notas)
print("Promedio de notas")
print("El promedio de las notas es:", promedio)
# Ejercicio 4
estudiantes = [
    {"nombre": "Ana", "promedio": 4.2},
    {"nombre": "Carlos", "promedio": 2.5},
    {"nombre": "Bernardo", "promedio": 3.8},
    {"nombre": "Haider", "promedio": 2.9},
    {"nombre": "Elena", "promedio": 3.0}
]
print("Estudiantes aprobados (promedio >= 3.0)")
for estudiante in estudiantes:
    if estudiante["promedio"] >= 3.0:
        print(estudiante["nombre"], estudiante["promedio"])
# Ejercicio 5
def calcular_valor_inventario(prod):
    return prod["precio"] * prod["stock"]
print("Valor total del inventario")
total = calcular_valor_inventario(producto)
print("El valor total en stock del producto", producto["nombre"], "es:", total)