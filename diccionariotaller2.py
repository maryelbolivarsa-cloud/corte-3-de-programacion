#Ejercicio 1
persona = {}
persona["nombre"] = input("Nombre: ")
persona["edad"] = int(input("Edad: "))
persona["estatura"] = float(input("Estatura: "))
persona["ciudad"] = (input("Ciudad: "))

nombre = persona["nombre"]
mayuscula = nombre.upper()
cant_caracteres = len(nombre.replace(" ", ""))

print(f"mayuscula{mayuscula}")
print(f"Cantidad de caracteres (sin espacios): {cant_caracteres}")

cedula = persona["edad"]

if cedula < 18:
    persona["estado"] = "Menor de edad"
elif cedula >= 60:
    persona["estado"] = "Adult@ mayor"
else:
    persona["estado"] = "Adult@"

asilo = persona["estado"]

parImpar = persona["edad"]
if parImpar % 2 == 0:
    tipo_edad = "par"
    print("La edad es par")
else:
    tipo_edad = "impar"
    print("La edad es impar") 

print()
print("Datos en el diccionario")
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

mensaje = (
    f"Hola, mi herman@ se llama {mayuscula} (su nombre tiene {cant_caracteres} caracteres), "
    f"tiene {persona['edad']} años (número {tipo_edad}) por ende es {asilo}, "
    f"mide {persona['estatura']} y vive en la ciudad de {persona['ciudad']}."
)

print()
print(mensaje)

#Ejercicio 2
def calculo_sum_prom(lista):
    suma = sum(lista)
    promedio = suma / len(lista)
    return suma, promedio

def obtener_may_men(lista):
    return max(lista), min(lista)

def contar_par_impar(lista):
    pares = 0
    impares = 0
    for num in lista:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares

def obtener_positivos(lista):
    positivos = []
    for num in lista:
        if num > 0:
            positivos.append(num)
    return positivos

def obtener_unicos(lista):
    return set(lista)

cantidad = int(input("Digite la cantinad números desea ingresar: "))
while cantidad < 1:
    print("La cantidad no puede ser menor que 1.")
    cantidad = int(input("Ingrese nuevamente la cantidad: "))

numeros = []
for i in range(cantidad):
    num = float(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)

suma, promedio = calculo_sum_prom(numeros)
mayor, menor = obtener_may_men(numeros)
pares, impares = contar_par_impar(numeros)
positivos = obtener_positivos(numeros)
unicos = obtener_unicos(numeros)

print()
print("Resumen:")
print(f"Lista de números: {numeros}")
print(f"Suma: {suma}")
print(f"Promedio: {promedio}")
print(f"Número mayor: {mayor}")
print(f"Número menor: {menor}")
print(f"Cantidad de pares: {pares}")
print(f"Cantidad de impares: {impares}")
print(f"Números positivos: {positivos}")
print(f"Valores únicos (Set): {unicos}")

#Ejercicio 3

def invertir(texto):
    if len(texto) == 0:
        return texto
    return invertir(texto[1:]) + texto[0]

palabra = input("Ingrese una palabra o frase: ")

invertida = invertir(palabra)
print(f"Texto original: {palabra}")
print(f"Texto invertido: {invertida}")

original_limpio = palabra.lower().replace(" ", "")
invertido_limpio = invertida.lower().replace(" ", "")

if original_limpio == invertido_limpio:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")

vocales = 0
for letra in palabra.lower():
    if letra in "aeiouáéíóú":
        vocales = vocales + 1

print(f"Cantidad de vocales: {vocales}")
resultado = (palabra, invertida, vocales)
print(f"Respuesta: {resultado}")

#Ejercicio 4
def promedio_nota(lista_de_notas):
    promedio = sum(lista_de_notas) / len(lista_de_notas)
    return promedio

estudiantes = []

for i in range(3):
    print(f"Registro del estudiante {i+1}")
    
    estudiante = {}
    estudiante["nombre"] = input("Nombre: ")
    estudiante["codigo"] = input("Código: ")

    notas_estudiante = []
    for n in range(3):
        nota = float(input(f"Nota {n+1}: "))
        while nota < 0.0 or nota > 5.0:
            print("Error: La nota debe estar entre 0.0 y 5.0")
            nota = float(input(f"Ingrese de nuevo la nota {n+1}: "))
        notas_estudiante.append(nota)
        
    estudiante["notas"] = notas_estudiante
    
    prom = promedio_nota(estudiante["notas"])
    estudiante["promedio"] = prom

    if prom >= 3.0:
        estudiante["estado"] = "Aprobado"
    else:
        estudiante["estado"] = "Reprobado"

    estudiantes.append(estudiante)
    print()

print("RESULTADOS FINALES:")
for est in estudiantes:
    print(
        f"Nombre: {est['nombre']}, "
        f"Código: {est['codigo']}, "
        f"Promedio: {est['promedio']}, "
        f"Estado: {est['estado']}"
    )

#Ejercicio 5
grupo_python = ["Ana", "Luis", "Carlos", "Sofia", "Mateo"]
grupo_datos = ["Sofia", "Mateo", "Laura", "Ana", "Daniel"]

