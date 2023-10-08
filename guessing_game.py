from random import *


print('Добро пожаловать в игру! Угадайте число. Удачи!')


def game():
    x = int(input('Введите крайний правый диапазон случайного числа:'))
    print('Начнем!')
    answer = ['Вы угадали, поздравляем!', 'Слишком много, попробуйте еще раз',
              'Слишком мало, попробуйте еще раз']
    num = randint(1, x)
    try_counter = 0
    while True:
        n = input()
        if is_valid(n):
            n = int(n)
            if n == num:
                print(answer[0], 'Вам понадобилось попыток:', try_counter)
                while True:
                    end = input('Хотите сыграть еще раз? (Y/N)')
                    if end == 'Y':
                        return game()
                    elif end == 'N':
                        break
                    else:
                        print('Введите Y (сыграть еще раз) или N (закончить игру)')
                else:
                    continue
                break
            elif n > num:
                print(answer[1])
                try_counter += 1
                continue
            else:
                print(answer[2])
                try_counter += 1
                continue
        else:
            print('Проверьте введенные данные. Число должно быть больше 0 и не превышать', x)


def is_valid(number):
    return number.isdigit() and 1 <= int(number)    #<= x доделать функции. разбить game на большее количество функций


game()
