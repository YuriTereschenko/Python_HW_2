# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д..
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]

arr = [2, 3, 5, 6]
result = []
new_arr_len = int((len(arr) / 2))

if len(arr) % 2 != 0:
    new_arr_len += 1

for i in range(0, new_arr_len):
    result.append(arr[i] * arr[-i-1])
print(result)
