# Ecuación cuadratica
# y = -b +- raíz cuadrada (b ^ 2) -4ab / 2a
from cmath import sqrt

a = float(input("Input the value a: "))
b = float(input("Input the value b: "))
c = float(input("Input the value c: "))

# is discriminating is less zero no have solution
discriminating = (b ** 2) - 4 * a * c

if discriminating <= 0:
    print("Not exist real solution", discriminating)
else:
    x1 = (-b + sqrt(discriminating)) / (2 * a)
    x2 = (-b - sqrt(discriminating)) / (2 * a)

    print(x1)
    print(x2)
