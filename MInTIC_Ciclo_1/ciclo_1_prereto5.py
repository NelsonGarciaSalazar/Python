# Question 3
def materias(courses):
    list_courses = courses.split(',')
    return list_courses


print(materias("English,Physic,Socials,History,Programming"))


# Question 4
def listaFrutas(fruits):
    for i in range(len(fruits)):
        print(fruits[i])


listaFrutas(["Apples", "Grape", "Avocado"])


# Question 5
def multiplicarNumeros(numbers):
    total = 1

    for i in range(len(numbers)):
        total = total * numbers[i]

    return total


print(multiplicarNumeros([2, 3, 5]))
print(multiplicarNumeros([2, 2, 2]))

dictionary = [{'valor': 5}, {'valor': 2}]
for i in range(len(dictionary)):
    x = dictionary[i]['valor']
    print(x)
