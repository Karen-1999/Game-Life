class Animal(object):

    def __init__(self, name="n"):
        self.name = name


class Fishes(Animal):

    def __init__(self, name):

        super(Fishes, self).__init__(name)

    def rules(self, near):
        """
        :param near: count of neighbours whose type is Fishes
        :return: what type of animal would be written in this place
        """
        if(near >= 4) or(near < 2):
            return "n"
        else:
            return "f"


class Shrimps(Animal):

    def __init__(self, name):
        super(Shrimps, self).__init__(name)

    def rules(self, near):
        """
        :param near: count of neighbours whose type is Shrimps
        :return: what type of animal would be written in this place
        """
        if(near >= 4) or(near < 2):
            return "n"
        else:
            return "s"


class Nothing(Animal):

    def __init__(self, name):
        super(Nothing, self).__init__(name)

    def rules(self, near_fishes, near_shrimps):
        """
        :param near_fishes: count of neighbours whose type is Fishes
        :param near_shrimps: count of neighbours whose type is Shrimps
        :return: what type of animal would be written in this place
        """
        if(near_fishes == 3):
            return "f"
        elif(near_shrimps == 3):
            return "s"
        else:
            return "n"


class Rock(object):

    def __init__(self, name):
        self.name = name

    def rules(self):
        """
        :return: type of animal would be written in this place
        """
        return "r"


class Maps(object):

    def __init__(self, start, n, m):
        self.start_map = start
        self.m = m
        self.n = n

    def upgrade(self, k):
        """
        :param k: count of periods to upgrade
        :return: the finale state of my map will be
        recorded in self.startmap
        """
        n = self.n
        m = self.m
        for s in range(k):
            edit_map = []
            for i in range(n):
                for j in range(m):
                    cell = self.start_map[i][j]
                    shr, fish = self.countnear(i, j)
                    if(cell == "f"):
                        c = Fishes(cell).rules(fish)
                        if(c != cell):
                            edit_map.append([i, j, c])
                    elif(cell == "s"):
                        c = Shrimps(cell).rules(shr)
                        if(c != cell):
                            edit_map.append([i, j, c])
                    elif(cell == "n"):
                        c = Nothing(cell).rules(fish, shr)
                        if(c != cell):
                            edit_map.append([i, j, c])
                    else:
                        continue
            for i in range(len(edit_map)):
                self.start_map[edit_map[i][0]][edit_map[i][1]] = edit_map[i][2]

    def countnear(self, i, j):
        """
        :param i: collumn of cell
        :param j: raw of cell
        :return: pair of integers, count of fish neighbours
        and shrimp neighbours
        """
        n = self.n
        m = self.m
        name = self.start_map[i][j]
        count_fishes = 0
        count_shrimps = 0
        for r in {i - 1, i, i + 1}:
            for w in {j - 1, j, j + 1}:
                if(0 <= r < n) and (0 <= w < m) and \
                   not (r == i and w == j):
                    if(self.start_map[r][w] == "f"):
                        count_fishes += 1
                    if(self.start_map[r][w] == "s"):
                        count_shrimps += 1
        return(count_shrimps, count_fishes)


def print_map(map):
    """
    :param map: list of lists, state of my map i should print
    :return: map
    """
    for i in map:
        for j in i:
            print(j, end='')
        print()
