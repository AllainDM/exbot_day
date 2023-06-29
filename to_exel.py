from datetime import datetime

import xlrd
import xlwt


# Наши улицы в "совместных" районах
moscow = [" Смоленская ул.", " Киевская ул."]
frunze = [" Тосина ул.", " Тамбовская ул."]
kirov = [" Канонерский о-в", " Шотландская ул.", " Двинская ул.", " Оборонная ул.",
         " Севастопольская ул.", " Турбинная ул.", " Гладкова ул."]

west_all_street_for_userside = [" Канонерский о-в", " Шотландская ул.", " Двинская ул.", " Оборонная ул.",
                                " Севастопольская ул.", " Турбинная ул.", " Гладкова ул.",
                                " Тосина ул.", " Тамбовская ул.",
                                " Смоленская ул.", " Киевская ул."]


def save_to_exel_from_userside(table_name, arr, t_o):
    t_o_rus = ""
    if t_o == "TOWest":
        t_o_rus = "ТО_Запад"
    elif t_o == "TONorth":
        t_o_rus = "ТО_Север"
    elif t_o == "TOSouth":
        t_o_rus = "ТО_Юг"
    elif t_o == "TOEast":
        t_o_rus = "ТО_Восток"
    wb = xlwt.Workbook()
    ws = wb.add_sheet(f'{table_name}')
    num_string = 2  # Стартовый номер строки для екселя
    for i in arr:
        print(f"список3143 {i}")
        ws.write(num_string, 0, i[0])  # Бренд
        ws.write(num_string, 1, i[1])  # Дата
        ws.write(num_string, 2, i[2])  # Номер договора
        ws.write(num_string, 3, i[3])  # Улица
        ws.write(num_string, 4, i[4])  # Дом
        ws.write(num_string, 5, i[5])  # Квартира
        ws.write(num_string, 6, i[6])  # Мастер
        ws.write(num_string, 7, i[7])  # Район
        ws.write(num_string, 10, i[8])  # Метраж
        num_string += 1

    date_now = datetime.now()
    ws.write(0, 0, f"Версия 004 Время: {date_now}")

    wb.save(f'{t_o}/{t_o_rus}_{table_name}.xls')


