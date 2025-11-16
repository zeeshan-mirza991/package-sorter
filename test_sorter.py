import unittest
from sorter import sort

class TestPackageSorter(unittest.TestCase):

    def test_standard_small_light(self):
        self.assertEqual(sort(50, 40, 30, 5), "STANDARD")

    def test_standard_boundary_below_limits(self):
        self.assertEqual(sort(149, 149, 149, 19.9), "STANDARD")

    def test_special_bulky_volume(self):
        self.assertEqual(sort(200, 200, 30, 10), "SPECIAL")

    def test_special_bulky_dimension(self):
        self.assertEqual(sort(150, 20, 20, 5), "SPECIAL")

    def test_special_heavy(self):
        self.assertEqual(sort(40, 40, 40, 20), "SPECIAL")

    def test_special_heavy_decimal(self):
        self.assertEqual(sort(10, 10, 10, 20.0), "SPECIAL")

    def test_rejected_bulky_and_heavy(self):
        self.assertEqual(sort(200, 200, 200, 30), "REJECTED")

    def test_rejected_exact_thresholds(self):
        self.assertEqual(sort(150, 150, 150, 20), "REJECTED")

    def test_edge_zero_dimensions(self):
        self.assertEqual(sort(0, 0, 0, 0), "STANDARD")

    def test_edge_negative_values(self):
        self.assertEqual(sort(-10, 20, 30, 5), "STANDARD")

if __name__ == "__main__":
    unittest.main()
