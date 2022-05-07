"""
    The number perfects are when a number and the sum of your dividers are equals
    Example 6: 1 + 2 + 3 = 6
"""
number = int(input("Enter the number: "))
total = 0

for i in range(1, number, 1):
    if number % i == 0:
        total = total + i

if total == number:
    print(f"The number {number} is perfect")
else:
    print(f"The number {number} is not perfect")