# В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части
# элементов. Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
arr = [1.1, 1.4, 3.15, 5, 10.01]

for i in range(0, len(arr)):
    arr[i] %= 1

result = str(max(arr) - min(arr))
print(result[0:4])





