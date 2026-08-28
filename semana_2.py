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

#Mostramos Datos
print("Edad:", edad)
print("Peso:", peso)
print("Estatura:", estatura)

#Calulo de IMC
imc = peso / (estatura ** 2)
#Mostramos el resultado del IMC
print("Tu IMC es:", imc)