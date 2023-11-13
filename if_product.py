n = int(input())


def product(num):
    count = 0
    ls = [int(input()) for _ in range(num + 1)]
    last_ls = ls[-1]
    ls = ls[:-1]
    for i in range(len(ls)):
        for j in range(len(ls)):
            if i != j and ls[i] * ls[j] == last_ls:
                count += 1
    if count > 0:
        print('ДА')
    else:
        print('НЕТ')


product(n)
