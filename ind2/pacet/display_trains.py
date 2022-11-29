#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def display_trains(trains):
    """""
    Отобразить список рейсов
    """""
    # Заголовок таблицы.
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 5,
        '-' * 20,
        '-' * 14,
        '-' * 16
    )
    print(line)
    print(
        '| {:^5} | {:^20} | {:^14} | {:^16} |'.format(
            "№",
            "Едет в",
            "№ поезда",
            "Время отпр-ния"
        )
    )
    print(line)
    # Вывести данные о всех поездах.
    for idx, tr in enumerate(trains, 1):
        print(
            '| {:>5} | {:<20} | {:<14} | {:>16} |'.format(
                idx,
                tr.get('dist', ''),
                tr.get('number', 0),
                tr.get('time', '')
            )
        )
    print(line)
