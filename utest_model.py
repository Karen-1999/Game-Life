import unittest
from model import Animal
from model import Nothing
from model import Rock
from model import Maps
from model import Fishes
from model import Shrimps


class Test(unittest.TestCase):
    def test_init(self):
        nothing_test = Nothing
        self.assertEqual(nothing_test.short_name, "n")
        fishes_test = Fishes
        self.assertEqual(fishes_test.short_name, "f")
        shrimps_test = Shrimps
        self.assertEqual(shrimps_test.short_name, "s")
        rock_test = Rock
        self.assertEqual(rock_test.short_name, "r")

    def test_maps_init(self):
        my_map_short_named = []
        for raw in range(5):
            my_map_short_named.append([str("f") for collumn in range(5)])
        my_map = Maps(my_map_short_named)
        equal_map = [[Fishes, Fishes, Fishes, Fishes, Fishes],
                     [Fishes, Fishes, Fishes, Fishes, Fishes],
                     [Fishes, Fishes, Fishes, Fishes, Fishes],
                     [Fishes, Fishes, Fishes, Fishes, Fishes],
                     [Fishes, Fishes, Fishes, Fishes, Fishes]]
        self.assertEqual(my_map.start_map, equal_map)
        self.assertEqual(my_map.height, 5)
        self.assertEqual(my_map.width, 5)

    def test_maps_upgrade1(self):
        my_map_short_named = []
        my_map_short_named.append([str("n"), str("f"), str("f")])
        my_map_short_named.append([str("f"), str("f"), str("f")])
        my_map_short_named.append([str("f"), str("f"), str("f")])
        my_map = Maps(my_map_short_named)
        equal_map = [[Fishes, Nothing, Fishes],
                     [Nothing, Nothing, Nothing],
                     [Fishes, Nothing, Fishes]]
        my_map.upgrade(1)
        self.assertEqual(my_map.start_map, equal_map)
        self.assertEqual(my_map.height, 3)
        self.assertEqual(my_map.width, 3)

    def test_count_of_neighbors_nothing(self):
        my_map = [[Fishes, Nothing, Shrimps],
                  [Nothing, Nothing, Nothing],
                  [Fishes, Nothing, Rock]]
        my_map[1][1].count_of_neighbors(Animal, my_map, 1, 1)
        count_of_neighbors_dict = my_map[1][1].get_count_of_neighbors_dict(Animal)
        self.assertEqual(count_of_neighbors_dict[Fishes], 2)
        self.assertEqual(count_of_neighbors_dict[Nothing], 4)
        self.assertEqual(count_of_neighbors_dict[Shrimps], 1)
        self.assertEqual(count_of_neighbors_dict[Rock], 1)

    def test_count_of_neighbors_fish(self):
        my_map = [[Shrimps, Nothing, Nothing],
                  [Fishes, Rock, Fishes],
                  [Shrimps, Fishes, Rock]]
        my_map[1][2].count_of_neighbors(Animal, my_map, 1, 2)
        count_of_neighbors_dict = my_map[1][2].get_count_of_neighbors_dict(Animal)
        self.assertEqual(count_of_neighbors_dict[Fishes], 1)
        self.assertEqual(count_of_neighbors_dict[Nothing], 2)
        self.assertEqual(count_of_neighbors_dict[Rock], 2)

    def test_count_of_neighbors_rock(self):
        my_map = [[Rock, Nothing, Nothing],
                  [Fishes, Fishes, Fishes],
                  [Shrimps, Fishes, Fishes]]
        my_map[0][0].count_of_neighbors(Animal, my_map, 0, 0)
        count_of_neighbors_dict = my_map[0][0].get_count_of_neighbors_dict(Animal)
        self.assertEqual(count_of_neighbors_dict[Fishes], 2)
        self.assertEqual(count_of_neighbors_dict[Nothing], 1)

    def test_count_of_neighbors_shrimp(self):
        my_map = [[Fishes, Fishes, Shrimps, Nothing],
                  [Fishes, Shrimps, Fishes, Rock],
                  [Shrimps, Fishes, Fishes, Fishes],
                  [Shrimps, Rock, Shrimps, Nothing]]
        my_map[3][2].count_of_neighbors(Animal, my_map, 3, 2)
        count_of_neighbors_dict = my_map[3][2].get_count_of_neighbors_dict(Animal)
        self.assertEqual(count_of_neighbors_dict[Fishes], 3)
        self.assertEqual(count_of_neighbors_dict[Nothing], 1)
        self.assertEqual(count_of_neighbors_dict[Rock], 1)

    def test_rules_of_updating_fish(self):
        my_map = [[Fishes, Fishes, Shrimps, Nothing],
                  [Fishes, Shrimps, Fishes, Rock],
                  [Shrimps, Fishes, Fishes, Fishes],
                  [Shrimps, Rock, Shrimps, Nothing]]
        map = Maps
        map.start_map = my_map

        map.start_map[2][1].count_of_neighbors(Fishes, map.start_map, 2, 1)
        new_state = map.start_map[2][1].rules_of_updating(Fishes)
        self.assertEqual(new_state, Fishes)

    def test_rules_of_updating_shrimp(self):
        my_map = [[Fishes, Fishes, Shrimps, Nothing],
                  [Fishes, Shrimps, Fishes, Rock],
                  [Shrimps, Fishes, Fishes, Fishes],
                  [Shrimps, Rock, Shrimps, Nothing]]
        map = Maps
        map.start_map = my_map
        map.start_map[3][2].count_of_neighbors(Shrimps, map.start_map, 3, 2)
        new_state = map.start_map[3][2].rules_of_updating(Shrimps)
        self.assertEqual(new_state, Nothing)

    def test_rules_of_updating_nothing(self):
        my_map = [[Rock, Fishes, Shrimps, Nothing],
                  [Nothing, Shrimps, Fishes, Rock],
                  [Shrimps, Fishes, Nothing, Fishes],
                  [Shrimps, Rock, Shrimps, Nothing]]
        map = Maps
        map.start_map = my_map
        map.start_map[2][2].count_of_neighbors(Nothing, map.start_map, 2, 2)
        new_state = map.start_map[2][2].rules_of_updating(Nothing)
        self.assertEqual(new_state, Fishes)


"""
консольный интерфейс:
python3 -m unittest utest_model.py
"""
if __name__ == '__main__':
    unittest.main()
