from collections import defaultdict


class Animal:

    """
    хранит данные о соседях в формате:
    Nothing: 1,
    Fishes: 2 и тд.
    """
    count_of_neighbors_dict = defaultdict

    def count_of_neighbors(self, map, i, j):
        """
        :param map: текущая карта океана, обьект класса Maps
        :param i: строка клетки
        :param j: столбец клетки
        :return: подсчитывает количество соседей всех типов
        и записывает их в словарь count_of_neighbors_dict
        по ключу вид животного
        """
        self.count_of_neighbors_dict.clear()
        for r in {i - 1, i, i + 1}:
            for w in {j - 1, j, j + 1}:
                if (0 <= r < len(map)) and \
                        (0 <= w < len(map[0])) and \
                        not (r == i and w == j):
                self.count_of_neighbors_dict[map[r][w]] += 1
                    
    def rules_of_updating(self):
        """
        для каждого наследника определены условия обновления клетки,
        которые зависят от количества определенных видов соседей.
        Количество соседей по видам хранится в словаре
        :return: какой класс запишется после upgrade
        класса по его правилам
        """
        pass

    def short_name():
        """
        :return: возвращает первую букву названия вида животного
        в строчном формате
        """
        pass


class Fishes(Animal):

    def rules_of_updating(self):
        if(not Fishes in self.count_of_neighbors_dict):
            self.count_of_neighbors_dict[Fishes] = 0
        if(self.count_of_neighbors_dict[Fishes] >= 4) or \
                (self.count_of_neighbors_dict[Fishes] < 2):
            return Nothing
        else:
            return Fishes

    def short_name():
        return "f"


class Shrimps(Animal):

    def rules_of_updating(self):
        if(not Shrimps in self.count_of_neighbors_dict):
            self.count_of_neighbors_dict[Shrimps] = 0
        if(self.count_of_neighbors_dict[Shrimps] >= 4) or \
                (self.count_of_neighbors_dict[Shrimps] < 2):
            return Nothing
        else:
            return Shrimps

    def short_name():
        return "s"


class Nothing(Animal):

    def rules_of_updating(self):
        if(not Fishes in self.count_of_neighbors_dict):
            self.count_of_neighbors_dict[Fishes] = 0
        if (not Shrimps in self.count_of_neighbors_dict):
            self.count_of_neighbors_dict[Shrimps] = 0
        if self.count_of_neighbors_dict[Fishes] == 3:
            return Fishes
        elif self.count_of_neighbors_dict[Shrimps] == 3:
            return Shrimps
        else:
            return Nothing

    def short_name():
        return "n"


class Rock(Animal):

    def rules_of_updating(self):
        return Rock

    def short_name():
        return "r"


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

    def upgrade(self, k):
        """
        :param k: количество поколений, через которое надо
        подсчитать ответ
        :return: обновляет k раз карту по правилам, указанным в классах животных,
        получая ответ
        """
        for s in range(k):
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
            print(cell.short_name(), end="")
        print()


"""
long_name_dict: словарь, обеспечивающий 
доступ по краткому имени к названию класса
"""
long_name_dict = {
    'f': Fishes,
    'r': Rock,
    'n': Nothing,
    's': Shrimps,
}
