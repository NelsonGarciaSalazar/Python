def palindromos(number):
    var = ""
    for i in range(len(number) - 1, -1, -1):
        var += number[i]
    return var


number = input("Enter a number greater than one digit: ")
new_number = palindromos(number)
print(new_number)

# Yo hago yoga hoy
