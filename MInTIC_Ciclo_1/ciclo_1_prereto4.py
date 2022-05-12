"""
    Una empresa requiere discriminar si un paquete puede ser enviado o no de acuerdo a su peso y su volumen. La empresa
    considera que el paquete puede ser enviado si su peso es menor a 2 kg y si su volumen es menor a 0.027 m^3.
    Escriba una función llamada procesar_dato que reciba dos datos: el peso y el volumen de un paquete (el primer
    parámetro recibido por la función debe ser el peso y el segundo el volumen). Esta función debe retornar verdadero si
    el paquete puede ser enviado y retornar falso si el paquete no puede ser enviado.
"""


# Function send package
def procesar_dato(w, v):
    send = False
    if (w < 2) and (v < 0.027):
        send = True
    return send


# Function par_impar
def par_impar(number):
    result = False
    if number % 2 == 0:
        result = True
    return result


# Function split
value = "Item 1, Item 2, Item 3, Item 4, Item 5"
print(int(value.split(',')[1].split(' ')[2]))


# Function convert
def peso_a_euro(peso):
    return peso / 4500


# Function greatest number
def maxinum(a, b):
    max_num = b
    if a > b:
        max_num = a
    return max_num
