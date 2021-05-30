import sys

sys.path.append("..")

from src.utils import randomint
import unittest


class TestRandomIntGeneration(unittest.TestCase):

    def test_rnd_int_generation(self):
        size = 1_000_000_000
        rnd_int_generator = randomint.RandomIntGenerator()
        rnd_ints = rnd_int_generator.get_random_int_list(size=size)

        self.assertEqual(len(rnd_ints), size)
        self.assertEqual(rnd_ints.dtype, "int32")


if __name__ == "__main__":
    unittest.main()
