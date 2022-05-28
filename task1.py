# Найти сумму чисел списка стоящих на нечетной позиции
# Пример:[1,2,3,4] -> 4

array = [1, 2, 3, 4, 5, 6]
result = 0
for i in range(0, len(array), 2):
    result += array[i]
print(result)