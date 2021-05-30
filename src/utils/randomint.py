import numpy as np


class RandomIntGenerator():

    def __init__(self, n=4):
        """
        Initializes the RandomIntGenerator instance.

        Args:
            n (int): number of bytes the generated integer will occupy.

        """

        self.__n = n
        self.__range_left_limit = -1
        self.__range_right_limit = -1

        self.__calculate_range_limits()

    def __calculate_range_limits(self):
        """
        Calculates the range from which the random integer will be generated.

        """

        num_bits = self.__n * 8
        self.__range_right_limit = (2 ** num_bits) / 2
        self.__range_left_limit = (-1) * self.__range_right_limit

        self.__range_right_limit = int(self.__range_right_limit)
        self.__range_left_limit = int(self.__range_left_limit)

    def get_random_int_list(self, size=100_000_000):
        """
        Returns an ndarray containing size integer numbers.

        """

        return np.random.randint(
            low=self.__range_left_limit,
            high=self.__range_right_limit,
            size=size,
            dtype='int32'
        )
