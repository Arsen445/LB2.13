#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def select_trains(trains, selected_num):
    """""
    Выбрать рейсы с заданным номером
    """""
    # Инициализировать счетчик.
    count = 0
    # Сформировать список поездов
    result = []
    # Проверить сведения работников из списка.
    for tr in trains:
        if tr.get('zodiak', '') == selected_num:
            count += 1
            result.append(tr)

    return result
