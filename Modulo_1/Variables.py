#variable int (entero)
Chocolate_caliente = 50

#variable float (decimal)
Pi = 3.141516

#variable boolean 

is_active = True

#variable string/char (texto)
Saludo = "Hola, mundo!"

#f-String
print(f'variables: {Chocolate_caliente}, {Pi}, {is_active}, {Saludo}')

#---------
#Variables list
#[lindexo,  lindex1, ......]
fruits = ["apple", 50, "cherry", [1,2,3], True]
#fruits[0]---- 'apple'

#Variable Tuple
#(VALUE1, VALUE2, .....)
coordinates = (10.0, 20.0)
#coordinates[0]---- 10.0
#coordinates[1]---- 20.0

#Variable Dictionary
#{ Key : value}
person ={
    'name' : 'kevin',
    'age' : 30,
    'city' : 'Madrid',
    'hobies' : ['football', 'read','trips'],
    'is_active' : True
}
 
print(f'Variables complejas: {fruits}, {coordinates}, {person}')