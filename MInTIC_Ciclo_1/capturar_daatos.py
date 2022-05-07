from unicodedata import name

'''
name = input('Digite la varible: ')
age = input('Digite la edad: ')

age = int(age)

print('El nombre es: ' + name)
print('La edad es: ' + str(age)) 

print('El nombre es: ' + name + ' y la edad es: ' + str(age))
'''

"""
# Siempre que se pide un dato, este es de tipo str
numero1 = input('Digite el primer numero: ')
numero2 = input('Digite el segundo numero: ')

# Esto imprime el numero de veces la variable numero1(4) porque es un str
print(10*numero1) # 4444444444

numero1 = int(numero1)
numero2 = int(numero2)

resultado = (numero1 + numero2)*(30/100)

print('El 30% de la suma de los numeros: ' + str(numero1) + ' y ' + str(numero2) + ' es: ' +str(resultado))
"""

# Imprimir variables sin concatenarlas con el comodin (,) esto inserta un espacio implicitamente
area = 4

print("El área es: " + str(area))
print("El área es:", area)

