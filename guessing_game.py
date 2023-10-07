from random import *


def game():
    answer = ['Вы угадали, поздравляем!', 'Слишком много, попробуйте еще раз',
              'Слишком мало, попробуйте еще раз']
    num = randint(1, 100)
    while True:
        n = int(input())
        if n == num:
            print(answer[0])
            break
        elif n > num:
            print(answer[1])
            continue
        else:
            print(answer[2])
            continue


game()
