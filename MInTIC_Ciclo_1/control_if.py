edad = int(input("Ingrese la edad de la persona: "))

if edad<0:
    print("Ingreso un númeñro negativo")
else:
    if edad<18:
        print("Es menor de edad")
    else:
        print("Es mayor de edad")