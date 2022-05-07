name = input("What is your name?")
last_Name = input("What is your lastname?")
identification = int(input("What is your identification?"))
salary = float(input("What is your salary?"))
email = input("What is your email?")

annual_salary = 12 * salary
digits = identification % 100

if annual_salary >= 50831000:
    print(f"{name}, {last_Name}, with identification {identification}, have to declarer income")
    print(f"Communicate to email{email}")

    if digits >= 0 and digits <= 50:
        print("Have to declare to 27 april")
    elif digits >= 51 and digits <= 70:
        print("Have to declare to 27 may")
    else:
        print("Have to declare to 27 jun")
else:
    print("Have to declare to 27 july")