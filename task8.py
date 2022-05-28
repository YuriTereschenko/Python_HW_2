# Простые делители числа 13195 - это 5, 7, 13 и 29.
# Каков самый большой делитель числа 600851475143, являющийся простым числом?

def is_prime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n



n = 600851475143
result = n
while True:
    result -= 2
    if n % result == 0:
        if is_prime(result) is True:
            break

print(result)

