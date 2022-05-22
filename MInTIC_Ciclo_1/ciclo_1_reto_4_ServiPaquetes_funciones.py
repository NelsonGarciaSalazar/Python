def calcularCosto(high, wide, deep):
    volume = high * wide * deep
    calulate_cost = volume * 5

    if high > 30:
        calulate_cost += 2000
    if calulate_cost > 10000:
        calulate_cost += (calulate_cost * 0.19)

    return calulate_cost


def costoTotal(numero_paquetes, descuento):
    total_cost = 0

    for _ in range(numero_paquetes):
        high = float(input())
        wide = float(input())
        deep = float(input())
        total_cost += calcularCosto(high, wide, deep)

    return total_cost * (1 - descuento / 100)


numberPackage = int(input("numP: "))
discount = int(input("dis: "))
print(calcularCosto(35, 10, 5))
print(calcularCosto(10, 5, 5))
print(costoTotal(numberPackage, discount))
