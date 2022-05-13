def calcularCosto(alto, ancho, profundo):
    volumen = alto * ancho * profundo
    calcularCosto = volumen * 5

    if alto > 30:
        calcularCosto += 2000
    if calcularCosto > 10000:
        calcularCosto += (calcularCosto * 0.19)

    return calcularCosto


def costoTotal(numeroPaquetes, descuento):

    costoTotal = 0

    for i in range(numeroPaquetes):
        alto = float(input())
        ancho = float(input())
        profundo = float(input())
        costoTotal += calcularCosto(alto, ancho, profundo)

    return costoTotal * (descuento/100)