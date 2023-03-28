# Простая программа создаёт список из категорий на каждый день недели под запись. Держите свои дела в порядке.

import datetime


print('Введите категории, которые хотели бы заполнить на днях для отчёта.')
cat = input('Вводите через пробел категории: ')
cat_list = cat.split(' ')
print(cat_list)

f = open('report.txt', 'w')

now = datetime.datetime.now()
now_day_1 = now - datetime.timedelta(days=now.weekday())

dates = {}
week_days = ['ПН', 'ВТ', 'СР', 'ЧТ', 'ПТ', 'СБ', 'ВС']

for n_week in range(1):
    dates[n_week] = [(now_day_1 + datetime.timedelta(days=d+n_week*7)).strftime("%d.%m.%Y") for d in range(7)]

for day in range(7):
    print(dates[0][day], '-', week_days[day], file = f)
    for i, cat in enumerate(cat_list):
        print(f'{i+1}. {cat}: ', file = f)
    print(file = f)
f.close()
