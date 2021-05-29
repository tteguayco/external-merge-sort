import random
import numpy as np


class RandomIntGenerator():

    def __init__(self, n=4):
        """
        Initializes the RandomIntGenerator instance.

        Args:
            n (int): number of bytes the generated integer will occupy.

        """

        self.n = n
        self.range_left_limit = -1
        self.range_right_limit = -1

        self._calculate_range_limits()

    def _calculate_range_limits(self):
        """
        Calculates the range from which the random integer will be generated.

        """

        num_bits = self.n * 8
        self.range_left_limit = 2 ** (num_bits - 1) + 1
        self.range_right_limit = 2 ** num_bits

    def get_random_int_list(self, size=500_000_000):
        """
        Returns an ndarray containing size integer numbers.

        """

        return np.random.randint(
            low=self.range_left_limit,
            high=self.range_right_limit,
            size=size,
            dtype='int64'
        )
