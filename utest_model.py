import unittest
from model import Nothing
from model import Rock
from model import Maps
from model import Fishes
from model import Shrimps


class Test(unittest.TestCase):
    def test_init(self):
        nothing_test = Nothing
        self.assertEqual(nothing_test.short_name(), "n")
        fishes_test = Fishes
        self.assertEqual(fishes_test.short_name(), "f")
        shrimps_test = Shrimps
        self.assertEqual(shrimps_test.short_name(), "s")
        rock_test = Rock
        self.assertEqual(rock_test.short_name(), "r")

    def test_maps_init(self):
        my_map_short_named = []
        for i in range(5):
            my_map_short_named.append([str("f") for j in range(5)])
        my_map = Maps(my_map_short_named)
        equal_map = [[Fishes, Fishes, Fishes, Fishes, Fishes],
                     [Fishes, Fishes, Fishes, Fishes, Fishes],
                     [Fishes, Fishes, Fishes, Fishes, Fishes],
                     [Fishes, Fishes, Fishes, Fishes, Fishes],
                     [Fishes, Fishes, Fishes, Fishes, Fishes]]
        self.assertEqual(my_map.start_map, equal_map)
        self.assertEqual(my_map.height, 5)
        self.assertEqual(my_map.width, 5)

    def test_maps_upgrade(self):
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

    def test_maps_upgrade(self):
        my_map_short_named = []
        my_map_short_named.append([str("n"), str("f"), str("f"), str("s"), str("s")])
        my_map_short_named.append([str("f"), str("f"), str("r"), str("r"), str("s")])
        my_map_short_named.append([str("f"), str("f"), str("f"), str("s"), str("s")])
        my_map_short_named.append([str("s"), str("s"), str("n"), str("s"), str("s")])
        my_map_short_named.append([str("f"), str("r"), str("n"), str("n"), str("f")])
        my_map = Maps(my_map_short_named)
        equal_map = [[Nothing, Fishes, Nothing, Nothing, Nothing],
                     [Fishes, Nothing, Rock, Rock, Nothing],
                     [Nothing, Nothing, Nothing, Shrimps, Nothing],
                     [Nothing, Nothing, Nothing, Shrimps, Nothing],
                     [Nothing, Rock, Nothing, Shrimps, Nothing]]
        my_map.upgrade(2)
        self.assertEqual(my_map.start_map, equal_map)
        self.assertEqual(my_map.height, 5)
        self.assertEqual(my_map.width, 5)

    def test_count_of_neighbors_nothing(self):
        my_map = [[Fishes, Nothing, Shrimps],
                  [Nothing, Nothing, Nothing],
                  [Fishes, Nothing, Rock]]
        my_map[1][1].count_of_neighbors(Nothing, my_map, 1, 1)
        self.assertEqual(my_map[1][1].count_of_neighbors_fish, 2)
        self.assertEqual(my_map[1][1].count_of_neighbors_nothing, 4)
        self.assertEqual(my_map[1][1].count_of_neighbors_shrimp, 1)
        self.assertEqual(my_map[1][1].count_of_neighbors_rock, 1)

    def test_count_of_neighbors_fish(self):
        my_map = [[Shrimps, Nothing, Nothing],
                  [Fishes, Rock, Fishes],
                  [Shrimps, Fishes, Rock]]
        my_map[1][2].count_of_neighbors(Fishes, my_map, 1, 2)
        self.assertEqual(my_map[1][2].count_of_neighbors_fish, 1)
        self.assertEqual(my_map[1][2].count_of_neighbors_nothing, 2)
        self.assertEqual(my_map[1][2].count_of_neighbors_shrimp, 0)
        self.assertEqual(my_map[1][2].count_of_neighbors_rock, 2)

    def test_count_of_neighbors_rock(self):
        my_map = [[Rock, Nothing, Nothing],
                  [Fishes, Fishes, Fishes],
                  [Shrimps, Fishes, Fishes]]
        my_map[0][0].count_of_neighbors(Rock, my_map, 0, 0)
        self.assertEqual(my_map[0][0].count_of_neighbors_fish, 2)
        self.assertEqual(my_map[0][0].count_of_neighbors_nothing, 1)
        self.assertEqual(my_map[0][0].count_of_neighbors_shrimp, 0)
        self.assertEqual(my_map[0][0].count_of_neighbors_rock, 0)

    def test_count_of_neighbors_shrimp(self):
        my_map = [[Fishes, Fishes, Shrimps, Nothing],
                  [Fishes, Shrimps, Fishes, Rock],
                  [Shrimps, Fishes, Fishes, Fishes],
                  [Shrimps, Rock, Shrimps, Nothing]]
        my_map[3][2].count_of_neighbors(Shrimps, my_map, 3, 2)
        self.assertEqual(my_map[3][2].count_of_neighbors_fish, 3)
        self.assertEqual(my_map[3][2].count_of_neighbors_nothing, 1)
        self.assertEqual(my_map[3][2].count_of_neighbors_shrimp, 0)
        self.assertEqual(my_map[3][2].count_of_neighbors_rock, 1)

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

    def test_rules_of_updating_fish(self):
        my_map = [[Fishes, Fishes, Shrimps, Nothing],
                  [Fishes, Shrimps, Fishes, Rock],
                  [Shrimps, Fishes, Fishes, Fishes],
                  [Shrimps, Rock, Shrimps, Nothing]]
        map = Maps
        map.start_map = my_map
        map.start_map[2][1].count_of_neighbors(map, map.start_map, 2, 1)
        new_state = map.start_map[2][1].rules_of_updating(map)
        self.assertEqual(new_state, Fishes)

    def test_rules_of_updating_nothing(self):
        my_map = [[Rock, Fishes, Shrimps, Nothing],
                  [Nothing, Shrimps, Fishes, Rock],
                  [Shrimps, Fishes, Nothing, Fishes],
                  [Shrimps, Rock, Shrimps, Nothing]]
        map = Maps
        map.start_map = my_map
        map.start_map[2][2].count_of_neighbors(map, map.start_map, 2, 2)
        new_state = map.start_map[2][2].rules_of_updating(map)
        self.assertEqual(new_state, Fishes)

"""
консольный интерфейс:
python3 -m unittest utest_model.py
"""
if __name__ == '__main__':
    unittest.main()
