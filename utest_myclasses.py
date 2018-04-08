import unittest
from myclasses import Nothing
from myclasses import Rock
from myclasses import Maps
from myclasses import Fishes
from myclasses import Shrimps


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
        self.assertEqual(my_map.length, 5)
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
        self.assertEqual(my_map.length, 3)
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
                     [Nothing, Rock, Nothing, Shrimps, Nothing]
                     ]
        my_map.upgrade(2)
        self.assertEqual(my_map.start_map, equal_map)
        self.assertEqual(my_map.length, 5)
        self.assertEqual(my_map.width, 5)


"""
консольный интерфейс:
python3 -m unittest utest_myclasses.py
"""
if __name__ == '__main__':
    unittest.main()
