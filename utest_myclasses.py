import unittest
from myclasses import Fishes
from myclasses import Animal
from myclasses import Shrimps
from myclasses import Nothing
from myclasses import Rock
from myclasses import Maps


class Test(unittest.TestCase):
    def test_init(self):
        nothing_test = Nothing("n")
        self.assertEqual(nothing_test.name, "n")
        animal_test = Animal("n")
        self.assertEqual(animal_test.name, "n")
        fishes_test = Fishes("f")
        self.assertEqual(fishes_test.name, "f")
        shrimps_test = Shrimps("s")
        self.assertEqual(shrimps_test.name, "s")
        rock_test = Rock("r")
        self.assertEqual(rock_test.name, "r")

    def test_rules(self):
        nothing_rules_test = Nothing.rules(Nothing, 3, 4)
        self.assertEqual(nothing_rules_test, "f")
        rock_rules_test = Rock.rules(Rock)
        self.assertEqual(rock_rules_test, "r")
        fishes_rules_test = Fishes.rules(Fishes, 3)
        self.assertEqual(fishes_rules_test, "f")
        shrimps_rules_test = Shrimps.rules(Shrimps, 3)
        self.assertEqual(shrimps_rules_test, "s")

    def test_maps_init(self):
        my_map = Maps([[] * 3] * 5, 5, 3)
        self.assertEqual(my_map.start_map, [[] * 3] * 5)
        self.assertEqual(my_map.n, 5)
        self.assertEqual(my_map.m, 3)

"""
консольный интерфейс:
python3 -m unittest utest_myclasses.py
"""
if __name__ == '__main__':
    unittest.main()
