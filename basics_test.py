"""
Unit test file for get_column_stats.py

"""

import unittest
import get_column_stats as stats
import random
import statistics as st
import os

class TestCalc(unittest.TestCase):
    def test_mean_constant(self):
        self.assertEqual(stats.mean([3, 4, 5, 6]), st.mean([3, 4, 5, 6]))


    def test_stdev_constant(self):
        self.assertEqual(stats.stdev([3, 4, 5, 6]), st.pstdev([3, 4, 5, 6]))


    def setUp(self):
        #self.test_file_name = 'setup_test_file.txt'
        #f = open(self.test_file_name, 'w')

        self.random_list = []

        for i in range(100):
            rand_int = random.randint(1,100)
            self.random_list.append(rand_int)
            #f.write(str(rand_int) + '\n')
        #f.close()

        self.calc_mean_random_list = st.mean(self.random_list)
        self.calc_pstdev_random_list = st.pstdev(self.random_list)


    def tearDown(self):
        #os.remove(self.random_list)
        self.random_list = []


    def test_mean_random(self):
        file_mean = stats.mean(self.random_list)
        self.assertEqual(file_mean, self.calc_mean_random_list)


    def test_stdev_random(self):
        file_stdev = stats.stdev(self.random_list)
        self.assertEqual(file_stdev, self.calc_pstdev_random_list)


    # test an exception: empty list? non integer? not a list

if __name__ == '__main__':
    unittest.main()
