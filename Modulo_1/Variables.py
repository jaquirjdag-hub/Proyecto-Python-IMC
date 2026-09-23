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
#
#-------------------
#Ejemplo de conversión de tipos
numero_str = "100"

#a + b a y b deben ser del mismo tipo (decimal, enteros)
#No podemos sumar/concatenar un string con un entero directamente
print(f'{numero_str}50') #output "10050"

numero_int  = int(numero_str) + 50 #conversión de string a entero y sumar 50
print(numero_int)