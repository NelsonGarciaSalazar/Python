def calcularCosto(high, width, deep):
    volume = high * width * deep
    shipping_cost = volume * 5

    if high > 30:
        shipping_cost += 2000
    if shipping_cost > 10000:
        shipping_cost += (shipping_cost * 0.19)

    return shipping_cost


def costoTotal(numberPackage, discount):

    total_cost = 0

    for i in range(numberPackage):
        high = float(input())
        width = float(input())
        deep = float(input())
        total_cost += calcularCosto(high, width, deep)

    return total_cost * (discount/100)


numberPackage = int(input("numP: "))
discount = int(input("dis: "))
print(calcularCosto(35,10,5))
print(calcularCosto(10,5,5))
print(costoTotal(numberPackage, discount))
