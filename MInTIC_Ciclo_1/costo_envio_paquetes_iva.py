alto = float(input())
ancho = float(input())
profundo = float(input())

volumen = alto * ancho * profundo
costo_envio = volumen * 5

if (alto > 50) and (ancho > 20) and (profundo > 40):
    costo_envio = costo_envio + 5000
if (costo_envio > 100000):
    costo_envio = costo_envio + (costo_envio * 0.19)

print(volumen)
print(costo_envio)