

class ExternalMergeSortProcessor():

    def __init__(self, source_file_path, dest_file_path, m=100_000):
        """
        Initializes the ExternalMergeSortProcessor instance.

        Args:
            m (int): in-memory capacity.
        """

        self.m = m
        self.source_file_path = source_file_path
        self.dest_file_path = dest_file_path
