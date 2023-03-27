items = [[6, 76562], [30, 54688],
         [23, 67599], [24, 16152],
         [45, 3084], [29, 88326],
         [48, 53130], [50, 85330],
         [11, 1627], [15, 28339],
         [33, 50321], [26, 34688],
         [30, 27722], [7, 38273]]
# список предметов, где первое значение - вес, а вторая - цена


thief_w = 100 # Вес который вор может украсть за раз
thief_r = 20 # Кол-во заходов


def stole():
    c = 0 # Стоимость укдаденного
    b = 0 # Лежит в рюкзаке
    r = 1 # Заход
    for i in items:
        if r >= thief_r:
            break # Если заходы закончились - выходим из цикла
        if b + i[0] <= thief_w: # Проверяем что влезет
            c+=i[1]
            # print(i)
            b+=i[0]
            # print(i)
        elif i[0] > thief_w: # Если предмет больше чем весь рюкзак - пропускаем
            continue
        else: # Опустошаем рюкзак и прибавляем заход
            b = 0
            r +=1
    return c

for i in range(0, len(items)): # Сортировка по цене
    for q in range(i, len(items)):
        if items[i][1] < items[q][1]:
            items[i], items[q] = items[q], items[i]

print('Жадный алгоритм:       ', stole(), ' денег')



for i in items:
    i.append(i[1]/i[0])
    # Считаем для каждого предмета соотношение цены/вес

for i in range(0, len(items)): # Сортировка по соотношению цены/вес
    for q in range(i, len(items)):
        if items[i][2] < items[q][2]:
            items[i], items[q] = items[q], items[i]

print('Оптимальный алгоритм:  ', stole(), ' денег')