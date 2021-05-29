import os
import numpy as np

# -----------------------------------------------------------------------------

INT_BYTE_SIZE = 4

# -----------------------------------------------------------------------------


class ExternalMergeSortProcessor():

    def __init__(self, source_file_path, dest_path, m=100_000):
        """
        Initializes the ExternalMergeSortProcessor instance.

        It assumes the binary files contain 4-byte integers (int32).

        Args:
            m (int): In-memory capacity as number of integers that fit.
            source_file_path (str): Binary file containing integers to be
                ordered.
            dest_path (str): Destination path where the sorted file will be
                placed in. The name for the sorted file will be taken from
                the provided source file.

        """

        self.m = m
        self.source_file_path = source_file_path
        self.dest_path = dest_path

        # Calculate info needed for further applying merge sort algorithm
        self.source_bytes_size = os.path.getsize(self.source_file_path)
        self.num_ints = int(self.source_bytes_size / INT_BYTE_SIZE)
        self.num_chunks = int(np.ceil(self.num_ints / self.m))
        self.chunks_byte_size = self.num_chunks * INT_BYTE_SIZE

    def _sort_ints(int_array):
        pass

    def _sort_chunks(self):
    
        with open(self.source_file_path, "rb") as f:
            for i in range(self.num_chunks):
                offset = int(i * self.chunks_byte_size)
                chunk_ints = np.fromfile(f, offset=offset)
                self._sort_ints(chunk_ints)

    def _merge_sorted_files(self):
        pass

    def sort(self):
        self._sort_chunks()
        self._merge_sorted_files()
