# Создайте программу, которая будет играть в игру “коровы и быки” с пользователем. Игра работает так:
#
# Случайным образом генерируйте 4-значное число. Попросите пользователя угадать 4-значное число. За каждую цифру,
# которую пользователь правильно угадал в нужном месте, у них есть “корова”. За каждую цифру, которую пользователь
# угадал правильно, в неправильном месте стоит “бык”. Каждый раз, когда пользователь делает предположение,
# скажите им, сколько у них “коров” и “быков”. Как только пользователь угадает правильное число, игра окончена.
# Следите за количеством догадок, которые пользователь делает на протяжении всей игры, и сообщите пользователю в конце.
import random

rnd_num = list(str(random.randint(1000, 9999)))

print(rnd_num)
attempts = 0
win = False
while win is False:
    user_num = list(input("Введите число "))
    cows = 0
    bull = 0
    for i in range(0, len(rnd_num)):
        if user_num[i] == rnd_num[i]:
            cows += 1
        else:
            for j in range(0, len(rnd_num)):
                if user_num[i] == rnd_num[j]:
                    bull += 1
    print(f"Коров: {cows}, быков: {bull} ")
    attempts += 1
    if cows == 4:
        win = True
        print(f"Вы победили!!! Попыток: {attempts}")



