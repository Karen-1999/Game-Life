class Animal(object):
    @staticmethod
    def final_state(map, i, j):
        pass

    @staticmethod
    def short_name():
        pass


class Fishes(Animal):
    @staticmethod
    def final_state(start_map, i, j):
        """
        :param start_map: исходная карта океана
        :param i: столбец клетки
        :param j: строка клетки
        :return: какой класс запишется после upgrade
        класса по его правилам
        """
        count_shrimps = 0
        for r in {i - 1, i, i + 1}:
            for w in {j - 1, j, j + 1}:
                if (0 <= r < len(start_map)) and \
                     (0 <= w < len(start_map[0])) and \
                        not (r == i and w == j):
                    if start_map[r][w] == Fishes:
                        count_shrimps += 1
        if(count_shrimps >= 4) or(count_shrimps < 2):
            return Nothing
        else:
            return Fishes

    @staticmethod
    def short_name():
        """
        :return: first letter of the name of this class, lowercase
        """
        return "f"


class Shrimps(Animal):
    @staticmethod
    def final_state(start_map, i, j):
        """
        :param start_map: исходная карта океана
        :param i: столбец клетки
        :param j: строка клетки
        :return: какой класс запишется после upgrade
        класса по его правилам
        """
        count_shrimps = 0
        for r in {i - 1, i, i + 1}:
            for w in {j - 1, j, j + 1}:
                if (0 <= r < len(start_map)) and \
                    (0 <= w < len(start_map[0])) and \
                        not (r == i and w == j):
                    if start_map[r][w] == Shrimps:
                        count_shrimps += 1
        if(count_shrimps >= 4) or(count_shrimps < 2):
            return Nothing
        else:
            return Shrimps

    @staticmethod
    def short_name():
        return "s"


class Nothing(Animal):
    @staticmethod
    def final_state(start_map, i, j):
        """
        :param start_map: исходная карта океана
        :param i: столбец клетки
        :param j: строка клетки
        :return: какой класс запишется после upgrade
        класса по его правилам
        """
        count_shrimps = 0
        count_fishes = 0
        for r in {i - 1, i, i + 1}:
            for w in {j - 1, j, j + 1}:
                if (0 <= r < len(start_map)) and \
                    (0 <= w < len(start_map[0])) and \
                        not (r == i and w == j):
                    if start_map[r][w] == Shrimps:
                        count_shrimps += 1
                    if start_map[r][w] == Fishes:
                        count_fishes += 1
        if count_fishes == 3:
            return Fishes
        elif count_shrimps == 3:
            return Shrimps
        else:
            return Nothing

    @staticmethod
    def short_name():
        return "n"


class Rock(object):

    @staticmethod
    def final_state(start_map, i, j):
        """
        :param start_map: исходная карта океана
        :param i: столбец клетки
        :param j: строка клетки
        :return: какой класс запишется после upgrade
        класса по его правилам
        """
        return Rock

    @staticmethod
    def short_name():
        return "r"


class Maps(object):

    def __init__(self, start):
        """
        :param start: исходная карта, в нем записаны
        краткие названия классов(см. dict shortname),
        я записываю в start_map соответствующие классы
        по ключу из start
        """
        for i in range(len(start)):
            for j in range(len(start[i])):
                start[i][j] = long_name_dict[start[i][j]]
        self.start_map = start
        self.width = len(start[0])
        self.length = len(start)

    def upgrade(self, k):
        """
        :param k: count of periods to upgrade
        :return: the finale state of my map will be
        recorded in self.startmap
        """
        n = self.length
        m = self.width
        for s in range(k):
            edit_map = []
            for i in range(n):
                for j in range(m):
                    cell = self.start_map[i][j]
                    new_cell = cell.final_state(self.start_map, i, j)
                    if cell != new_cell:
                        edit_map.append([i, j, new_cell])
            for i in range(len(edit_map)):
                self.start_map[edit_map[i][0]][edit_map[i][1]] = edit_map[i][2]


def print_map(map):
    """
    :param map: list of lists, state of my map i should print
    :return: print map
    """
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