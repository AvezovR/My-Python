def crypto(data):
    list_prime = []
    for i_index, i_score in enumerate(data):
        from sympy import isprime
        if isprime(i_index):
            list_prime.append(i_score)
    return list_prime

print(crypto('О Дивный Новый мир!'))
