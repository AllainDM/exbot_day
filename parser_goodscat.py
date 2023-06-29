from datetime import datetime, timedelta

import main
import to_exel

west_all_street = ["Канонерский остров", "Шотландская",
                   "Двинская", "Оборонная", "Смоленская",
                   "Тамбовская", "Турбинная", "Тосина"]


# Функция сбора подключений из ГК за прошлый день. Различается по статусу
def save_from_goodscat_for_day(table, status, date2, area):
    arr = []
    print(f'Всего должно быть абонентов {len(table)}')
    for i in table:
        user = []
        td_class_all = i.find_all('td', class_="")
        date1 = td_class_all[10].text[0:10]
        # Первым делом отсеим даты, при статусе Архив
        # Для статуса Архив, должна быть "вчерашняя" дата, то есть получаемая аргументом
        # if status == "archive":
        if date2 != date1:
            continue

        # У адреса другой класс
        address_class = i.find('td', class_="addr")
        # Тут нужно запустить парсер для Нетаба, но хз как его запускать отсюда
        # user.append(td_class_all[1].text)  # 0 = Номер ГК
        gk_num = td_class_all[1].text
        answer = main.parser_netup(gk_num)
        print(f"answer {answer}")

        user.append("ЭтХоум")  # Бренд

        # У даты нужно обрезать время, заменить тире и развернуть
        date1 = date1.split("-")
        date1 = f"{date1[2]}.{date1[1]}.{date1[0]}"
        user.append(date1)  # Дата

        user.append(answer[0])  # Договор

        # Отдельно берем адрес, заодно уберем лишние пробелы по краям
        address = address_class.text.strip()
        address = address.split(",")
        user.append(address[0])  # Адрес
        user.append(address[-2][2:])  # Адрес
        user.append(address[-1][4:])  # Адрес

        user.append(answer[1])  # Мастер
        user.append(area)  # Район
        user.append(answer[2])  # Метраж

        arr.append(user)  # Добавим итог в общий массив с адресами
    return arr


# Отфильтруем чужие улицы спорных районов
def street_filter(table, t_o):
    new_table = []
    for i in table:
        # Найдем адрес по классу
        address_class = i.find('td', class_="addr")
        # Обрежем пробелы по краям
        address = address_class.text.strip()
        address = address.split(",")
        # print(f"Тут должен быть список частей адреса: {address}")
        if t_o == "TOWest":
            for street in west_all_street:  # Список улиц
                if street in address:
                    # print(f"Улица {address} найдена в списке")
                    new_table.append(i)
        elif t_o == "TOSouth":
            for a in address:  # Список улиц
                if a not in west_all_street:
                    new_table.append(i)
                    break
                else:
                    break
    return new_table
