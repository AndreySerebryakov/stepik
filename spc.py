timur = input()
ruslan = input()
key = timur + '-' + ruslan

dictionary = {
    'камень-камень': 'ничья',
    'камень-ножницы': 'Тимур',
    'камень-бумага': 'Руслан',
    'камень-ящерица': 'Тимур',
    'камень-Спок': 'Руслан',
    'ножницы-ножницы': 'ничья',
    'ножницы-бумага': 'Тимур',
    'ножницы-камень': 'Руслан',
    'ножницы-ящерица': 'Тимур',
    'ножницы-Спок': 'Руслан',
    'бумага-бумага': 'ничья',
    'бумага-камень': 'Тимур',
    'бумага-ножницы': 'Руслан',
    'бумага-ящерица': 'Руслан',
    'бумага-Спок': 'Руслан',
    'ящерица-ящерица': 'ничья',
    'ящерица-Спок': 'Тимур',
    'ящерица-ножницы': 'Руслан',
    'ящерица-бумага': 'Тимур',
    'ящерица-камень': 'Руслан',
    'Спок-Спок': 'ничья',
    'Спок-ножницы': 'Тимур',
    'Спок-бамага': 'Руслан',
    'Спок-камень': 'Тимур',
    'Спок-ящерица': 'Руслан'
}

print(dictionary[key])
