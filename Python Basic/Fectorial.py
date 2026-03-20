def calculate_fect(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

print(calculate_fect(5))