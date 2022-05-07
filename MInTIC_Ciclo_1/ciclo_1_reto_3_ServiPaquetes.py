
numeroPaquetes = int(input("Ingrese el numero de paquetes a procesar: "))
totalVolumen = 0

for i in range(numeroPaquetes):
    alto = float(input())
    ancho = float(input())
    profundo = float(input())

    volumen = alto * ancho * profundo
    costo_envio = volumen * 5

    if (alto > 30):
        costo_envio = costo_envio + 2000
    if (costo_envio > 10000):
        costo_envio = costo_envio + (costo_envio * 0.19)

    print(volumen)
    print(costo_envio)

    totalVolumen += volumen

print(totalVolumen)