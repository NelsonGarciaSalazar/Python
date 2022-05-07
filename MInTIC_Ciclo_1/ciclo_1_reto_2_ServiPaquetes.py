'''
Planteamiento de la situación

Te contrataron como ingeniero de software junior para desarrollar una aplicación, para la empresa ServiPaquetes, que ayude con la gestión de los paquetes. Específicamente para calcular el costo de los envíos de los paquetes. Para ello, tú decides que harás la aplicación de forma progresiva, semana tras semana. Es decir, el software que empieces a plantear desde esta semana, igual será útil en la última semana.

La empresa te indica que es fundamental que sigas el orden en el que ellos te indican los datos, puesto que el sistema de ellos los arroja en un orden específico. La empresa te dice que ahora tienen una nueva política de costos porque ahora deberán declarar IVA. Por esto, el costo de envío de un paquete, aunque seguirá siendo $5, tiene estas nuevas consideraciones:

Si la altura del paquete es mayor a 30 cm, al costo ya calculado se le suman $2000 adicionales. También, si el costo es mayor a $10000, se le suma el valor del IVA (19%) como OTRO valor adicional.

Por ejemplo, si un paquete mide 35 cm de alto, 10 cm de ancho y 5 cm de profundidad, el costo sería $8750, pero como la altura es mayor a 30 cm, entonces se le aplica la tarifa adicional, quedando el costo en $10750. Ahora, como el costo también es mayor a $10000, hay que sumarle el IVA (19%) quedando un valor de $12792.5.

Tu tarea esta semana es hacer que el software de la semana pasada adopte esta nueva política de costos de la empresa.
'''

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