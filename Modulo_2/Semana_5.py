#Guardar palabras que el usuario ingrese
palabras =[]

# Tupla con los nombres de los cuadrantes.
cuadrantes = ("Cuadrante 1", "Cuadrante 2", "Cuadrante 3", "Cuadrante 4")


# comprobar la longitud de una palabra
def comprobar_palabra ():
    palabra = input("ingresa una palabra: ")
    # Guardar cada intento, aunque la palabra sea incorrecta
    palabras.append(palabra)
    
    
# comparar la longuitud de la palabra con el rango permetido
    while len(palabra) < 4 or len(palabra) > 8:
        print("La palabra es  incorrecta")
        palabra = input("ingresa otra palabra: ")
        # Guardar también los siguientes intentos
        palabras.append(palabra)
        
        if len(palabra) >= 4 and len (palabra) <= 8:
            print("La palabra es correcta")
        elif len(palabra) < 4:
            print("Hacen falta letras")
        else:
            print("la palabra tiene demaciadas letras")
            
# Mostrar las palabras guardadas
    print("Palabras guardadas:", palabras)


# Pedir las cordenadas de un punto y determinar en que cuadrante se encuentra
def comprobar_cuadrante():
    x = int(input("ingresa el valor x: "))
    y = int(input("ingresa el valor y: "))
    
# Comprobar que los valores no sean cero
    while x == 0 or y == 0:
        print("Error: intente de nuevo ingresar otra coordenada")
        x = int(input("ingresa el valor x nuevamente: "))
        y = int(input("ingresa el valor y nuevamente: "))

# Comprobar en que cuadrante esta el punto
    if x > 0 and y > 0:
        print("El punto esta en el", cuadrantes[0])
    elif x < 0 and y > 0:
        print("El punto esta en el", cuadrantes[1])
    elif x < 0 and y < 0:
        print("El punto esta en el", cuadrantes[2])
    elif x > 0 and y < 0:
        print("El punto esta en el", cuadrantes[3])

# Llamar a las funciones
comprobar_palabra()
comprobar_cuadrante()
