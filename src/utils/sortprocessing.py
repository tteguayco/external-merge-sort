import os
import shutil
import numpy as np
import heapq

# -----------------------------------------------------------------------------

INT_BYTE_SIZE = 4
EXTERNAL_MEM_PATH = "./src/external/sorted/"

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

        if not isinstance(source_file_path, str):
            raise TypeError("source_file_path must be str")

        if not isinstance(dest_path, str):
            raise TypeError("dest_path must be str")

        if not isinstance(m, int):
            raise TypeError("m must be int")

        if len(source_file_path) == 0:
            raise ValueError("source_file_path cannot be empty")

        if len(dest_path) == 0:
            raise ValueError("dest_path cannot be empty")

        if m <= 1:
            raise ValueError("m must be greater than 1")

        self.m = m
        self.source_file_path = source_file_path
        self.dest_path = dest_path
        self.source_file_name = os.path.split(self.source_file_path)[1]

        # Calculate info needed for applying merge sort algorithm
        self.source_bytes_size = os.path.getsize(self.source_file_path)
        self.num_ints = int(self.source_bytes_size / INT_BYTE_SIZE)
        self.num_chunks = int(np.ceil(self.num_ints / self.m))
        self.chunk_byte_size = self.m * INT_BYTE_SIZE

    def _clean_external_memory(self):
        shutil.rmtree(EXTERNAL_MEM_PATH)
        os.mkdir(EXTERNAL_MEM_PATH)

    def _sort_ints(self, int_array, chunk_idx):
        """
        Implements the in-memory sort for a given array of integers and stores
        the result in the file path that simulates the external memory
        (EXTERNAL_MEM_PATH).

        Args:
            int_array (np.array): Array of integers to be sorted.
            chunk_idx (int): Index that identifies the chunk from which
                int_array was taken.
        """

        ordered_array = np.sort(int_array, kind="quicksort")
        dest_file_name = str(chunk_idx) + self.source_file_name
        dest_file_path = os.path.join(EXTERNAL_MEM_PATH, dest_file_name)
        ordered_array.tofile(dest_file_path)

    def _sort_chunks(self):
        """
        Gets the integers from each chunk of the source binary file in order to
        apply an in-memory sort algorithm on them.

        Parallelization could be applied here: each chuck is sorted by a single
        thread.

        """

        with open(self.source_file_path, "rb") as f:
            for i in range(self.num_chunks):
                offset = int(i * self.chunk_byte_size)
                chunk_ints = np.fromfile(
                    f,
                    count=self.m,
                    dtype="int32")
                self._sort_ints(chunk_ints, i)

    def _insert_first_ints_in_heap(self, heap):
        file_idx = 0

        for filename in os.listdir(EXTERNAL_MEM_PATH):
            filepath = os.path.join(EXTERNAL_MEM_PATH, filename)

            with open(filepath, "rb") as f:
                first_int = np.fromfile(f, count=1, dtype="int32")

                if len(first_int) > 0:
                    first_int = first_int[0]
                    heapq.heappush(heap, (first_int, file_idx))

            file_idx += 1

        return heap

    def _read_int_from_external_file(self, file_name, file_pointer):
        """

        """

        file_path = os.path.join(EXTERNAL_MEM_PATH, file_name)

        with open(file_path, "rb") as f:
            offset = int(file_pointer * INT_BYTE_SIZE)
            int_num = np.fromfile(
                f,
                offset=offset,
                count=1,
                dtype="int32")

        if len(int_num) > 0:
            return int_num[0]

        return None

    def _init_files_pointers(self):
        num_files = len(os.listdir(EXTERNAL_MEM_PATH))

        return np.zeros(num_files, dtype="int8")

    def _merge_sorted_chunk_files(self):
        """
        Once all chunks have been sorted and these results are stored in the
        external memory as files, these are merged into one single sorted file.

        It uses a min-heap-based approach.
        """

        heap = []
        heapq.heapify(heap)

        heap = self._insert_first_ints_in_heap(heap)
        file_names = os.listdir(EXTERNAL_MEM_PATH)
        file_pointers = self._init_files_pointers()
        dest_file_path = os.path.join(self.dest_path, self.source_file_name)

        with open(dest_file_path, "wb+") as f:
            while len(heap) > 0:
                smallest_node = heapq.heappop(heap)
                smallest_int = smallest_node[0]
                file_idx = smallest_node[1]

                f.write(smallest_int)
                file_pointers[file_idx] += 1

                int2insert = self._read_int_from_external_file(
                    file_names[file_idx],
                    file_pointers[file_idx]
                )

                if int2insert:
                    heapq.heappush(heap, (int2insert, file_idx))

    def sort(self):
        """
        Applies external merge sort to the integers contained associated to
        an instance of ExternalMergeSortProcessor.

        """

        #self._clean_external_memory()
        #self._sort_chunks()
        self._merge_sorted_chunk_files()
        #self._clean_external_memory()
