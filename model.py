from collections import defaultdict
import sys
import argparse


class Animal:
    """
    хранит данные о соседях в формате:
    Nothing: 1,
    Fishes: 2 и тд.
    """
    _count_of_neighbors_dict = defaultdict(int)
    short_name = "a"
    """
    первая буква названия вида животного
    в строчном формате
    """

    def get_count_of_neighbors_dict(self):
        """
        возвращает приватный аттрибут _count_of_neighbors_dict
        :return:
        """
        return self._count_of_neighbors_dict

    def count_of_neighbors(self, map, raw, collumn):
        """
        :param map: текущая карта океана, обьект класса Maps
        :param raw: строка клетки
        :param collumn: столбец клетки
        :return: подсчитывает количество соседей всех типов
        и записывает их в словарь _count_of_neighbors_dict
        по ключу вид животного
        """
        self._count_of_neighbors_dict.clear()
        for r in {raw - 1, raw, raw + 1}:
            for c in {collumn - 1, collumn, collumn + 1}:
                if (0 <= r < len(map)) and \
                        (0 <= c < len(map[0])) and \
                        not (r == raw and c == collumn):
                    self._count_of_neighbors_dict[map[r][c]] += 1

    def rules_of_updating(self):
        """
        для каждого наследника определены условия обновления клетки,
        которые зависят от количества определенных видов соседей.
        Количество соседей по видам хранится в словаре
        :return: какой класс запишется после upgrade
        класса по его правилам
        """
        pass


class Fishes(Animal):
    short_name = 'f'

    def rules_of_updating(self):
        if (self._count_of_neighbors_dict[Fishes] >= 4) or \
                (self._count_of_neighbors_dict[Fishes] < 2):
            return Nothing
        else:
            return Fishes


class Shrimps(Animal):
    short_name = 's'

    def rules_of_updating(self):
        if (self._count_of_neighbors_dict[Shrimps] >= 4) or \
                (self._count_of_neighbors_dict[Shrimps] < 2):
            return Nothing
        else:
            return Shrimps


class Nothing(Animal):
    short_name = 'n'

    def rules_of_updating(self):
        if self._count_of_neighbors_dict[Fishes] == 3:
            return Fishes
        elif self._count_of_neighbors_dict[Shrimps] == 3:
            return Shrimps
        else:
            return Nothing


class Rock(Animal):
    short_name = 'r'

    def rules_of_updating(self):
        return Rock


class Maps(object):

    def __init__(self, start):
        """
        :param start: инициализируем по исходной карте
        start_map - в ячейки записываем instance соответствующих классов,
        width - ширина океана,
        height - высота океана
        """
        for i in range(len(start)):
            for j in range(len(start[i])):
                start[i][j] = long_name_dict[start[i][j]]
        self.start_map = start
        self.width = len(start[0])
        self.height = len(start)

    def upgrade(self, number_of_generations):
        """
        :param number_of_generations: количество поколений, через которое надо
        подсчитать ответ
        :return: обновляет k раз карту по правилам, указанным в классах животных,
        получая ответ
        """
        for generation in range(number_of_generations):
            edit_map = []
            for i in range(self.height):
                for j in range(self.width):
                    cell = self.start_map[i][j]
                    cell.count_of_neighbors(self.start_map[i][j], self.start_map, i, j)
                    new_cell = \
                        cell.rules_of_updating(self.start_map[i][j])
                    if cell != new_cell:
                        edit_map.append([i, j, new_cell])
            for i in range(len(edit_map)):
                self.start_map[edit_map[i][0]][edit_map[i][1]] = edit_map[i][2]


def print_map(map):
    """
    :param map: получает карту океана, которую надо печатать
    в формате "первая буква(строчная) класса" без пробелов
    :return: печатает карту
    """
    for raw in map:
        for cell in raw:
            print(cell.short_name, end="")
        print()


"""
long_name_dict: словарь, обеспечивающий 
доступ по краткому имени к названию класса,
генерируется автоматически для всех
подклассов класса Animal
"""

long_name_dict = {
    sub_classes_of_Animal.short_name: sub_classes_of_Animal
    for sub_classes_of_Animal in Animal.__subclasses__()
}
