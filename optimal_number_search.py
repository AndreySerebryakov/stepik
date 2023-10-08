from math import log2, ceil


def search(number):
    return ceil(log2(number))


n = int(input('Введите число:'))

print(search(n))
