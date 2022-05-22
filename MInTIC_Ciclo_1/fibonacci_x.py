def fibonacci(terms):
    term_1 = 0
    term_2 = 1
    term_3 = 1

    list_terms = []
    for _ in range(terms):
        term_4 = (term_1 + term_2) ** term_3
        list_terms.append(term_1)
        term_1 = term_2
        term_2 = term_3
        term_3 = term_4
    return list_terms


print(fibonacci(5))
