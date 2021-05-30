import sys

sys.path.append("..")

from src.utils import sortprocessing as sortp
import src.c as sortchecker
import numpy as np
import os
import unittest

# -----------------------------------------------------------------------------

INT_BYTE_SIZE = 4
EXTERNAL_MEM_PATH = "./external/sorted/"
SORTED_PATH = "./data/sorted/"
UNSORTED_FILE_PATH = "./data/unsorted/sample_test.dat"

# -----------------------------------------------------------------------------


class TestExternalMergeSort(unittest.TestCase):

    def setUp(self):
        int_array = np.array([45, 20, 30, 10, 101, 56, 67, 72, 80])
        int_array.tofile(UNSORTED_FILE_PATH)

    def test_external_merge_sort(self):
        m = 3
        proc = sortp.ExternalMergeSortProcessor(
            UNSORTED_FILE_PATH,
            SORTED_PATH,
            m)
        proc.sort()

        dest_file_path = os.path.join(SORTED_PATH, "sample_test.dat")

        unsorted_int_array = \
            sortchecker.get_int_array_from_file(UNSORTED_FILE_PATH)
        sorted_int_array = \
            sortchecker.get_int_array_from_file(dest_file_path)

        unsorted_is_sorted = sortchecker.is_sorted(unsorted_int_array)
        sorted_is_sorted = sortchecker.is_sorted(sorted_int_array)

        same_len = len(unsorted_int_array) == len(sorted_int_array)

        self.assertFalse(unsorted_is_sorted)
        self.assertTrue(sorted_is_sorted)
        self.assertTrue(same_len)


if __name__ == "__main__":
    unittest.main()
