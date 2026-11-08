import random
N = [random.randint(1, 100) for _ in range(random.randint(5, 10))]
print(N)
A = random.randint(0, 3)
print(A)
B = random.randint(A+1, len(N))
print(B)
N[A:B] = []
print(N)