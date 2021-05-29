import random


class RandomIntGenerator():

    def __init__(self, n=4, include_negatives=False):
        """
        Initializes the RandomIntGenerator instance.

        Args:
            n (int): number of bytes the generated integer will occupy.
            include_negatives (bool): indicates whether the range to generate
                random numbers should include negative values or not.

        """

        self.n = n
        self.include_negatives = include_negatives
        self.range_left_limit = -1
        self.range_right_limit = -1

        self._calculate_range_limits()

    def _calculate_range_limits(self):
        """
        Calculates the range from which the random integer will be generated.

        """

        # TODO implement here include_negatives

        num_bits = self.n * 8
        self.range_left_limit = 2 ** (num_bits - 1) + 1
        self.range_right_limit = 2 ** num_bits

    def generate_random_int(self):
        """
        Generates an random n-byte integer.

        Returns:
            int: Generated random n-byte integer.

        """
        return random.randint(self.range_left_limit, self.range_right_limit)


if __name__ == "__main__":
    rnd_int_generator = RandomIntGenerator()
    rnd_int = rnd_int_generator.generate_random_int()

    print(rnd_int)
