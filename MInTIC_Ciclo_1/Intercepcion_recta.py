#Ejercicio ecu recta y = mx + b
x1 = float(input("Ingrese la coordenada x1:"))
y1 = float(input("Ingrese la coordenada y1:"))
x2 = float(input("Ingrese la coordenada x2:"))
y2 = float(input("Ingrese la coordenada y2:"))

print(f"El punto P1 es:  ({x1},{y1})")
print(f"El punto P2 es:  ({x2},{y2})")

m = (y2-y1)/(x2-x1)
b = y1 -m*x1

#y = "La ecuación de la recta es: y = "+str(m)+"x + "+str(b)
print(f"La ecuación de la recta es: y = {m:.3f}x + ({b:.3f})")
#print(y)