persona = {}
persona["nombre"] = input("Nombre: ")
persona["edad"] = int(input("Edad: "))
persona["estatura"] = int(input("Estatura: "))
persona["ciudad"] = (input("Ciudad: "))
nombre = persona["nombre"]
mayuscula = nombre.upper()
print(mayuscula)
for edad, valor in persona.items():
 print(f"{edad}: {valor}")

cedula  = persona["edad"]

if cedula >= 18:
    persona["estado"] = "Mayor de edad"
else:
    persona["estado"] = "Menor de edad"

print(persona)

for edad, valor in persona.items(): 
    print(f"{edad}: {valor}")

parImpar = persona["edad"]
print("prueba",parImpar)
if  parImpar%2 == 0:
    print("La edad es par")
else:
    print("La edad es impar")

asilo  = persona["edad"]

if cedula >= 60:
    persona["estado"] = "Es adulto Mayor"
else:
    persona["estado"] = "Es mayor de eda"

print(persona)