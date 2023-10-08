from random import *


print('Добро пожаловать в игру! Угадайте число. Удачи!')


class Game:
    def input_border(self):
        x = int(input('Введите крайний правый диапазон случайного числа:'))
        num_x = x
        return num_x


    def resume_game(self):
        while True:
            end = input('Хотите сыграть еще раз? (Y/N)')
            if end.upper() == 'Y':
                return self.game()
            elif end.upper() == 'N':
                break
            else:
                print('Введите Y (сыграть еще раз) или N (закончить игру)')

    def is_valid(self, number):
        return number.isdigit() and 1 <= int(number) <= self.input_border()   #  <= x доделать функции. разбить game на большее количество функций

    def game(self):
        #    x = int(input('Введите крайний правый диапазон случайного числа:'))
        print('Начнем!')
        answer = ['Вы угадали, поздравляем!', 'Слишком много, попробуйте еще раз',
                  'Слишком мало, попробуйте еще раз']
        num = randint(1, self.num_x)
        try_counter = 0
        while True:
            n = input()
            if self.is_valid(n):
                n = int(n)
                if n == num:
                    print(answer[0], 'Вам понадобилось попыток:', try_counter)
                    if self.resume_game():
                        continue
                    else:
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
                print('Проверьте введенные данные. Число должно быть больше 0 и не превышать', self.num_x)


Game()
