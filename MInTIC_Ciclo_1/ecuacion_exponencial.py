value = int(input("Input the first number: "))
op = int(input("Input the second number: "))

if op == 1:
    print(f"The result is: {100 * value}")
elif op == 2:
    print(f"The result is: {100 ** value}")
elif op == 3:
    print(f"The result is: {100 /value}")
else:
    print(f"The result is: {0}")