from random import *


def game():
    answer = ['Вы угадали, поздравляем!', 'Слишком много, попробуйте еще раз',
              'Слишком мало, попробуйте еще раз']
    num = randint(1, 100)
    while True:
        n = input()
        if is_valid(n):
            n = int(n)
            if n == num:
                print(answer[0])
                break
            elif n > num:
                print(answer[1])
                continue
            else:
                print(answer[2])
                continue
        else:
            print('Проверьте введенные данные. Число должно быть от 1 до 100!')


def is_valid(number):
    return number.isdigit() and 1 <= int(number) <= 100


game()
