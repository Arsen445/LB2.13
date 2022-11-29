#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_train():
    """""
    Запросить данные о рейсе.
    """""
    dist = input("Введите пункт для поезда:  ")
    time = input("Введите время поезда:  ")
    number = int(input("Введите номер поезда:  "))
    return {
        'dist': dist,
        'number': number,
        'time': time,
    }
