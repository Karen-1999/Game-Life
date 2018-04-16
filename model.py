class Animal:

    count_of_neighbors_nothing = 0
    count_of_neighbors_fish = 0
    count_of_neighbors_shrimp = 0
    count_of_neighbors_rock = 0

    def count_of_neighbors(self, map, i, j):
        """
        :param map: текущая карта океана
        :param i: строка клетки
        :param j: столбец клетки
        :return: подсчитывает количество соседей всех типов
        и записывает их в соответствующие атрибуты
        """
        self.count_of_neighbors_nothing = 0
        self.count_of_neighbors_fish = 0
        self.count_of_neighbors_shrimp = 0
        self.count_of_neighbors_rock = 0
        for r in {i - 1, i, i + 1}:
            for w in {j - 1, j, j + 1}:
                if (0 <= r < len(map)) and \
                        (0 <= w < len(map[0])) and \
                        not (r == i and w == j):
                    if map[r][w] == Nothing:
                        self.count_of_neighbors_nothing += 1
                    if map[r][w] == Fishes:
                        self.count_of_neighbors_fish += 1
                    if map[r][w] == Rock:
                        self.count_of_neighbors_rock += 1
                    if map[r][w] == Shrimps:
                        self.count_of_neighbors_shrimp += 1

    def rules_of_updating(self):
        """
       :param start_map: исходная карта океана
       :param i: столбец клетки
       :param j: строка клетки
       :return: какой класс запишется после upgrade
       класса по его правилам
        """
        pass

    def short_name():
        """
        :return: first letter of the name of this class, lowercase
        """
        pass


class Fishes(Animal):

    def rules_of_updating(self):
        if(self.count_of_neighbors_fish >= 4) or \
                (self.count_of_neighbors_fish < 2):
            return Nothing
        else:
            return Fishes

    def short_name():
        return "f"


class Shrimps(Animal):

    def rules_of_updating(self):
        if(self.count_of_neighbors_shrimp >= 4) or \
                (self.count_of_neighbors_shrimp < 2):
            return Nothing
        else:
            return Shrimps

    def short_name():
        return "s"


class Nothing(Animal):

    def rules_of_updating(self):
        if self.count_of_neighbors_fish == 3:
            return Fishes
        elif self.count_of_neighbors_shrimp == 3:
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
        :param start: инициализируем по исхожноый карте
        start_map, width, height
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
        :return: обновляет k раз карту по правилам, получая ответ
        """
        for s in range(k):
            edit_map = []
            for i in range(self.height):
                for j in range(self.width):
                    cell = self.start_map[i][j]
                    cell.count_of_neighbors(self, self.start_map, i, j)
                    new_cell = \
                        cell.rules_of_updating(self)
                    if cell != new_cell:
                        edit_map.append([i, j, new_cell])
            for i in range(len(edit_map)):
                self.start_map[edit_map[i][0]][edit_map[i][1]] = edit_map[i][2]


def print_map(map):
    for i in map:
        for j in i:
            print(j.short_name(), end="")
        print()


"""
long_name_dict:    Доступ по краткому имени к названию класса
"""
long_name_dict = {
    'f': Fishes,
    'r': Rock,
    'n': Nothing,
    's': Shrimps,
}
