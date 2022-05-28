# Написать программу преобразования двоичного числа в десятичное.

n = "1111011"
result = 0
for i in range(0, len(n)):
    result = result * 2 + int(n[i])

print(result)
