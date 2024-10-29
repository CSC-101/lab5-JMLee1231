import data
import lab5
import unittest

import math
from data import Time, Point

# Write your test cases for each part below.

class TestCases(unittest.TestCase):

    # Part 3: Test cases for time_add function
    def test_time_add_without_carry(self):
        t1 = Time(2, 30, 25)
        t2 = Time(1, 15, 20)
        expected = Time(3, 45, 45)
        result = lab5.time_add(t1, t2)
        self.assertAlmostEqual(result.hour, expected.hour)
        self.assertAlmostEqual(result.minute, expected.minute)
        self.assertAlmostEqual(result.second, expected.second)

    def test_time_add_with_carry(self):
        t1 = Time(1, 59, 40)
        t2 = Time(0, 1, 30)
        expected = Time(2, 1, 10)
        result = lab5.time_add(t1, t2)
        self.assertAlmostEqual(result.hour, expected.hour)
        self.assertAlmostEqual(result.minute, expected.minute)
        self.assertAlmostEqual(result.second, expected.second)

    # Part 4: Test cases for is_descending function
    def test_is_descending_true(self):
        result = lab5.is_descending([5.0, 4.0, 3.0, 2.0, 1.0])
        expected = True
        self.assertEqual(result, expected)

    def test_is_descending_false(self):
        result = lab5.is_descending([5.0, 4.0, 6.0, 2.0, 1.0])
        expected = False
        self.assertEqual(result, expected)

    # Part 5: Test cases for largest_between function
    def test_largest_between_within_bounds(self):
        result = lab5.largest_between([1, 3, 5, 7, 6], 1, 3)
        expected = 3
        self.assertEqual(result, expected)

    def test_largest_between_out_of_bounds(self):
        result = lab5.largest_between([1, 2, 3, 4, 5], -3, 10)
        expected = 4
        self.assertEqual(result, expected)

    # Part 6: Test cases for furthest_from_origin function
    def test_furthest_from_origin(self):
        points = [Point(0, 0), Point(3, 4), Point(5, 12), Point(8, 15)]
        result = lab5.furthest_from_origin(points)
        expected = 3
        self.assertEqual(result, expected)

    def test_furthest_from_origin_single_point(self):
        points = [Point(1, 1)]
        result = lab5.furthest_from_origin(points)
        expected = 0
        self.assertEqual(result, expected)
if __name__ == '__main__':
    unittest.main()
