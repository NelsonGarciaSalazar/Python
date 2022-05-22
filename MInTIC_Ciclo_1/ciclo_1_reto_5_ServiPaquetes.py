import json

with open('paquetes.json') as file:
    empresa = json.load(file)


def calcularCosto(high, wide, deep):
    volume = high * wide * deep
    calulate_cost = volume * 5

    if high > 30:
        calulate_cost += 2000
    if calulate_cost > 10000:
        calulate_cost += (calulate_cost * 0.19)

    return calulate_cost


def costoTotal(listpackage, discont):
    total_cost = 0

    for i in range(len(listpackage)):
        high = listpackage[i]['ALTO']
        wide = listpackage[i]['ANCHO']
        deep = listpackage[i]['PROFUNDO']

        total_cost += calcularCosto(high, wide, deep)

    return total_cost * (1 - discont / 100)


print(costoTotal(empresa['PAQUETES'], 10))