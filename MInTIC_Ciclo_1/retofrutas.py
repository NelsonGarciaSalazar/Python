# No se deben colocar textos en los print porque al comparar con la respuesta que serúa un número, fallarí
numeroperas=int(input())
numeromanzanas=int(input())
numeromandarinas=int(input())
numeronaranjas=int(input()) 
preciomanzana=2000
precioperas=1800
preciomandarinas=1900
precionaranjas=3600
subtotal=numeroperas*precioperas+numeromanzanas*preciomanzana+numeronaranjas*precionaranjas+numeromandarinas*preciomandarinas
total=subtotal*1.19
print(subtotal)
print(total)
