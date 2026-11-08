def sum_factorials(num):
    factorial = 1
    total = 0

    for i in range(1, num + 1):
        factorial *= i
        total += factorial

    return total

number = int(input("Number: "))
fac_sum = sum_factorials(number)
print("fac_sum for", number, "is", fac_sum )