#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from datetime import date
from pacet.get_train import get_train
from pacet.select_trains import select_trains
from pacet.help_f import help_f
from pacet.display_trains import display_trains


def main():
    """""
    Главная функция программы
    """""
    print("help - список всех команд")
    trains = []
    while True:
        command = input(">>> ").lower()

        if command == "help":
            help_f()

        elif command == "add":
            train = get_train()
            # Добавить словарь в список.
            trains.append(train)
            # Сортировка в случае необходимости
            if len(trains) > 1:
                trains.sort(key=lambda item: item.get('number', ''))

        elif command == 'list':
            display_trains(trains)

        elif command == 'exit':
            break

        elif command.startswith('select '):
            parts = command.split(' ', maxsplit=1)
            selected_num = int(parts[1])
            selected = select_trains(trains, selected_num)
            display_trains(selected)

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()
