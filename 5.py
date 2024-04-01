import csv

f = open('astronaut_time.csv', encoding='utf-8')    # открытие файла
data = list(csv.DictReader(f))  # чтение файла в список
sl = {}   # словарь, где ключ - номер станции, а значение - информация о станции
for el in data:
    if el['numberStation'].split('-')[0] not in sl.keys():
        sl[el['numberStation'].split('-')[0][:2]] = [el]
    else:
        sl[el['numberStation'].split('-')[0][:2]].append(el)
for i in sl.keys():
    sum_hours, cnt = 0, 0  # сумма часов простоя и количество астронавтов
    cabins = []   # носера кают
    for el in sl[i]:
        sum_hours += int(el['count'])
        cnt += 1
        cabins.append(el['cabinNumber'])
    print(f'Номер группы: {i}. Каюты: {", ".join(cabins)}. Время простоя: {sum_hours / cnt}')
