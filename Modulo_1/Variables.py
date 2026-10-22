#Variable int (entero)
chocolate_caliente = 50

#Variable float (decimal)
PI = 3.141516

#Variable boolean 
is_active = True

#Variable string/char (texto)
Saludo = 'Hola, mundo!'

#print("tengo un chocolate caliente que vale:", chocolate_caliente, "pesos mexicamos.")


#f-String
#print(f'Tengo un chocolate caliente que vale: {chocolate_caliente + 1} pesos mexicanos.')

#print(f'Variables simples: {chocolate_caliente}, {PI}, {is_active}, {Saludo}')

#---------
#Variables list
#[lindexo,  lindex1, index2, ...]
fruits = ['apple', 50, 'cherry', [1,2,3], True]
#fruits[0]-- 'apple'

#Variable Tuple
#(value1, value2, ...)
coordinates = (10.0, 20.0)
#coordinates[0]---- 10.0
#coordinates[1]---- 20.0

#Variable Dictionary
#{key : value}
#person ={
 #   'name': 'Alexander',
  #  'age': 30,
    #'city': 'Madrid',
   # 'hobbies': ['football', 'read', 'trips'],
    #'is_active': True
#}

#print(f'variables complejas: {fruits}, {coordinates}, {person}')

#-------------------

#Ejemplo de conversión de tipos
numero_str = "100"

#a + b a y b deben ser del mismo tipo (decimal, enteros)
#No podemos sumar/concatenar un string con un entero directamente
print(f'{numero_str} 50') #output "10050"

numero_int  = int(numero_str) + 50 #conversión de string a entero y sumar 50
print(numero_int) 

fruits_str = ["10","20", "30"]
print(fruits_str) #output ['10', '20', '30']
fruits_int = list(map(int,fruits_str))
print(fruits_int)

flotante = 25.657
entero = int(flotante) #convercion de float a entero 
print(entero) #output 25
print(round(flotante, 0))

flotante_nuevo = float(numero_str) #convertimos de entero a float
print(flotante_nuevo) #output 100.0
print(entero + flotante_nuevo) #output 125.0

# Ejemplo de convercion a un boleano
is_boolean = True
is_boolean_str = str(is_boolean) #convertir boolean a string
print(is_boolean_str) #output "True"
is_boolean_int = int(is_boolean)
print(is_boolean_int) #output 1
is_boolean_float = float(is_boolean)
print(is_boolean_float) #output 1.0
boolean_float =bool(is_boolean_float)
print(boolean_float) #output True