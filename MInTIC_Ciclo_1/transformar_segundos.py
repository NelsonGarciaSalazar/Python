'''
    Escriba un programa que entrando un número en seconds determine los días, horas y minutos.
     En caso que los día sea mayor que 7 genere una alerta en pantalla como recordatorio.
'''

seconds = int(input("Input the amount of seconds: "))

days = (seconds // 86400)
rest_seconds_days = (seconds % 86400)

hours = (rest_seconds_days // 3600)
rest_seconds_hours = (rest_seconds_days % 3600)

minutes = (rest_seconds_hours // 60)

print("Days: ", days, " hours: ", hours, " Minutes :", minutes)

if days > 7:
    print("The days are greater than 7")