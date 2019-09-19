"""
Unit test file for mean and stdev methods in get_column_stats.py
"""

import unittest
import get_column_stats as column
import random
import statistics as st


class TestCalc(unittest.TestCase):
    def test_mean_constant(self):
        self.assertEqual(column.mean([3, 4, 5, 6]), st.mean([3, 4, 5, 6]))

    def test_stdev_constant(self):
        self.assertEqual(column.stdev([3, 4, 5, 6]), st.pstdev([3, 4, 5, 6]))

    def setUp(self):
        self.random_list = []

        for i in range(100):
            rand_int = random.randint(1, 100)
            self.random_list.append(rand_int)

        self.calc_mean_random_list = st.mean(self.random_list)
        self.calc_pstdev_random_list = st.pstdev(self.random_list)

    def tearDown(self):
        self.random_list = []

    def test_mean_random(self):
        file_mean = column.mean(self.random_list)
        self.assertEqual(file_mean, self.calc_mean_random_list)

    def test_stdev_random(self):
        file_stdev = column.stdev(self.random_list)
        self.assertEqual(round(file_stdev, 10),
                         round(self.calc_pstdev_random_list, 10))

    def test_mean_TypeError(self):
        self.assertRaises(TypeError, column.mean, random.randint(1, 100))

    def test_mean_empty_list(self):
        self.assertEqual(column.mean([]), None)

    def test_stdev_TypeError(self):
        self.assertRaises(TypeError, column.stdev, random.randint(1, 100))

    def test_stdev_empty_list(self):
        self.assertEqual(column.mean([]), None)


if __name__ == '__main__':
    unittest.main()
