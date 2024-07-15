import pandas as pd
import math
from datetime import datetime
import sys

# Изменение лимита рекурсии
sys.setrecursionlimit(50000)


def choise_winer(win_row, count_doubles, all_buers):
    winners = pd.read_csv('winers_complete.csv')
    winners_id = all_buers.iloc[win_row].to_string(index=False)
    count_d = count_doubles
    winners_string_values = winners.values.astype(str)

    if winners_id in winners_string_values:
        count_d += 1
        new_row = win_row + 1
        count_d, all_buers = choise_winer(new_row, count_d, all_buers)
    else:
        print(f"Победитель: {win_row + 1}")
        csv_row = {'ID': winners_id}
        new_data = pd.DataFrame([csv_row])
        new_data.to_csv('winers_complete.csv', mode='a', header=False, index=False)
        all_buers = all_buers[all_buers['ID'].astype(str) != winners_id]
        num_rows = all_buers.shape[0]
        print(f"Количество строк в DataFrame all_buers: {num_rows}")

    return count_d, all_buers


# Получение текущего курса валюты
url1 = 'http://www.cbr.ru/scripts/XML_daily.asp'
daily = pd.read_xml(url1, encoding='cp1251')
#course = daily.iloc[3]['Value']
course = '21,2641'
# Чтение данных участников и победителей
all_buers = pd.read_csv('reecrent_avito.csv')
winners = pd.read_csv('winers_complete.csv')

num_buers = len(all_buers)
num_winers = len(winners)

# Расчет шага выбора победителя
Cf = course[-4:-2]
Ct = course[-2:]
s_1 = float(num_buers) - float(num_winers)
s_2 = s_1 / float(Cf)
step = math.ceil(s_2 * float(Ct))

shift = 0
num_iterations = 5  # Число итераций для поиска

print(f"Курс: {course}")
print(f"Шаг выбора победителя: {step}")
print(f"Всего участников розыгрыша: {num_buers}")

# Основной цикл
for i in range(num_iterations):
    num_rows = all_buers.shape[0]
    need_row = (((i + 1) * step) % num_rows) - 1 + shift
    print(f"Итерация {i + 1}, выбор строки: {need_row}")
    shift, all_buers = choise_winer(need_row, shift, all_buers)

print(f"Смещений из-за повтора победителя: {shift}")