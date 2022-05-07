# Different format of the Cycle FOR #

print("Count number from 1 to 4")
for dix in range(1, 5):
    print(dix)

print("Count number from 0 to 4")
for dix in range(5):
    print(dix)

print("values form 0 to 3 and")
i = 0
while i < 9:
    if i <= 3 or (6 <= i <= 8):
        print(i)
    i += 1

print("it = 5")
value = 0
it = 0
while value < 10:
    if value > 5:
        value += 3
    else:
        value += 2
    it += 1
print(it)

print("Filter the items not nulls and print")
items = [None, "Liz", None, "Nelson"]
for value in items:
    if value is not None:
        print(value)
