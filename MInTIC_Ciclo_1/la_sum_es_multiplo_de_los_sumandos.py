number1 = int(input("Number 1: "))
number2 = int(input("Number 1: "))

valSum = number1 + number2

if valSum % number1 == 0:
    print("The sum is multiple of number1", number1)
elif valSum % number2 == 0:
    print("The sum is multiple of number2", number2)
else:
    print("The sum not is multiple of numbers", number1, " and ", number2)
