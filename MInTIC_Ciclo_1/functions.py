def sum_function(a, b):
    c = a + b
    return c


number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

result = sum_function(number1, number2)
print("The result of sum is: " + str(result))
