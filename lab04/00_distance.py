#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

distances = {}
# TODO здесь заполнение словаря
for city1, coord1 in cities.items():
    distances[city1] = {}
for city2, coord2 in cities.items():
    if city1 != city2:
        distance = ((coord1[0] - coord2[0]**2 + (coord1[1] - coord2[1])**2)**0,5)
        distances[city1][city2] = distance

        print(distances)






