#Pedimos el nombre
nombre = input("¿Cuál es tu nombre?") .capitalize()
nombre= str(nombre)

#Pedimos el apellido paterno
apellido_paterno = input("¿Cuál es tu apellido paterno?") .capitalize()
apellido_paterno= str(apellido_paterno)

#Pedimos el apellido materno
apellido_materno = input("¿Cuál es tu apellido materno?") .capitalize()
apellido_materno = str(apellido_materno)

#Pedimos la edad
edad = input("¿cuál es tu edad?")
#convertimos la edad a entero
edad = int(edad)

#Pedimos el peso
peso = input("¿cuál es tu peso?")
#Convertimos el peso a decimal
peso = float(peso)

#Pedimos la estatura
estatura = input("¿cuál es tu estatura?")
#Convertimos la estatura a decimal
estatura =float(estatura)

#Mostramos datos 
# F-String
print(f"Nombre: {nombre}")
print(f"Apellido Paterno: {apellido_paterno}")
print(f"Apellido Materno: {apellido_materno}")
print(f"Edad: {edad}")
print(f"Peso: {peso}")
print(f"Estatura: {estatura}")

#Calulo de IMC
imc = peso / (estatura ** 2)
#Mostramos el resultado del IMC con dos puntos decimales
print(f"Tu IMC es: {imc:.2f}")

