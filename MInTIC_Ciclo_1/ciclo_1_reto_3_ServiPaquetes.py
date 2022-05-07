numberPackages = int(input())
totalCost = 0

for i in range(numberPackages):
    high = float(input())
    wide = float(input())
    deep = float(input())

    volume = high * wide * deep
    cost_envio = volume * 5

    if high > 30:
        cost_envio += 2000
    if cost_envio > 10000:
        cost_envio += (cost_envio * 0.19)

    print(volume)
    print(cost_envio)

    totalCost += cost_envio

print(totalCost)
