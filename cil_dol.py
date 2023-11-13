n = int(input())
ls = [input() for _ in range(n)]


def antivirus(lst):
    quarantine = []
    virus = 'anton'
    for j in range(len(lst)):
        flag = False
        for i in range(len(virus)):
            if virus[i] in lst[j]:
                symbol = lst[j].find(virus[i])
                lst[j] = lst[j][symbol:]
                flag = True
            else:
                flag = False
        if flag:
            quarantine.append(lst[j])


antivirus(ls)
