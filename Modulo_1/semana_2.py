# Pedimos el nombre
nombre = input("¿Cuál es tu nombre?").capitalize()
nombre= str(nombre)

# Validar datos
while nombre == "":
    print("Error: no se pueden dejar campos vacíos")
    nombre = input("¿Cuál es tu nombre?").capitalize() 

#Pedimos el apellido paterno
apellido_paterno = input("¿Cuál es tu apellido paterno?").capitalize()
apellido_paterno= str(apellido_paterno)

# Validar datos
while apellido_paterno == "":
    print("Error: no se pueden dejar campos vacíos")
    apellido_paterno = input("¿Cuál es tu apellido paterno?").capitalize()

#Pedimos el apellido materno
apellido_materno = input("¿Cuál es tu apellido materno?").capitalize()
apellido_materno = str(apellido_materno)

# Validar datos
while apellido_materno == "":
    print("Error: no se pueden dejar campos vacíos")
    apellido_materno = input("¿Cuál es tu apellido materno?").capitalize()

#Pedimos la edad
# Validar datos
while True:
    try:
        edad = input("¿cuál es tu edad?")
        if edad =="":
            print("Error: no se pueden dejar campos vacíos")
        else:
            edad = int(edad)
            if edad > 0:
                break
            else:
                print("Error: la edad debe de ser mayor que cero")
    except ValueError:
        print("Error: la edad debe de ser un número entero")



#Pedimos el peso
# Validamos datos del peso
while True:
    try:
        peso = input("¿cuál es tu peso en kg?")
        if peso == "":
            print("Error: no se pueden dejar campos vacíos")
        else:
            peso = float(peso)
            if peso > 0:
                break
            else:
                print("Error: el peso debe de ser mayor que cero")
    except ValueError:
        print("Error: el peso debe ser un número valido")



#Pedimos la estatura
# Validacio de estatura
while True:
    try:
        estatura = input("¿cuál es tu estatura en metros?")
        if estatura == "":
            print("Error: no se pueden dejar campos vacíos")
        else:
            estatura = float(estatura)
            if estatura > 0:
                break
            else:
                print("Error: la estatura debe ser mayor que cero")
    except ValueError:
        print("Error: la estatura debe ser un número valido")


#Mostramos datos ingresados por el usuario
# F-String
print(f"Nombre: {nombre}")
print(f"Apellido Paterno: {apellido_paterno}")
print(f"Apellido Materno: {apellido_materno}")
print(f"Edad: {edad}")
print(f"Peso: {peso}")
print(f"Estatura: {estatura}")

# Calulo de IMC
imc = peso / (estatura ** 2)

#Mostramos el resultado del IMC con dos puntos decimales
print(f"Tu IMC es: {imc:.2f}")

