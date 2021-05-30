import sys

sys.path.append("..")

import src.c as sortchecker
import numpy as np
import unittest


class TestArraySorted(unittest.TestCase):

    def test_is_sorted_array(self):
        int_array = np.array([10, 20, 30, 45, 56, 67, 72, 80, 91])
        sorted = sortchecker.is_sorted(int_array)

        self.assertTrue(sorted)

    def test_is_not_sorted_array(self):
        int_array = np.array([45, 20, 30, 10, 56, 67, 72, 80, 91])
        sorted = sortchecker.is_sorted(int_array)

        self.assertFalse(sorted)


if __name__ == "__main__":
    unittest.main()
