import os
import shutil
import numpy as np
import heapq

# -----------------------------------------------------------------------------

INT_BYTE_SIZE = 4

# -----------------------------------------------------------------------------


class ExternalMergeSortProcessor():

    def __init__(self, source_file_path, dest_path, external_mem_path, m):
        """
        Initializes the ExternalMergeSortProcessor instance.

        It assumes the binary files contain 4-byte integers (int32).

        Args:
            source_file_path (str): Binary file containing integers to be
                ordered.
            dest_path (str): Destination path where the sorted file will be
                placed in. The name for the sorted file will be taken from
                the provided source file.
            external_mem_path (str): Path where all the files with the results
                of sorting the chuncks during first phase of merge sort
                algorithm will be placed.
            m (int): In-memory capacity as number of integers that fit.

        """

        if not isinstance(source_file_path, str):
            raise TypeError("source_file_path must be str")

        if not isinstance(dest_path, str):
            raise TypeError("dest_path must be str")

        if not isinstance(external_mem_path, str):
            raise TypeError("external_mem_path must be str")

        if not isinstance(m, int):
            raise TypeError("m must be int")

        if len(source_file_path) == 0:
            raise ValueError("source_file_path cannot be empty")

        if len(dest_path) == 0:
            raise ValueError("dest_path cannot be empty")

        if len(external_mem_path) == 0:
            raise ValueError("external_mem_path cannot be empty")

        if m <= 1:
            raise ValueError("m must be greater than 1")

        self.__m = m
        self.__source_file_path = source_file_path
        self.__dest_path = dest_path
        self.__external_mem_path = external_mem_path
        self.__source_file_name = os.path.split(self.__source_file_path)[1]

        # Calculate info needed for applying merge sort algorithm
        self.__source_bytes_size = os.path.getsize(self.__source_file_path)
        self.__num_ints = int(self.__source_bytes_size / INT_BYTE_SIZE)
        self.__num_chunks = int(np.ceil(self.__num_ints / self.__m))
        self.__chunk_byte_size = self.__m * INT_BYTE_SIZE

    def __clean_external_memory(self):
        """
        Cleans the external memory by removing its path and then creating it
        again.

        """

        shutil.rmtree(self.__external_mem_path)
        os.mkdir(self.__external_mem_path)

    def __sort_ints(self, int_array, chunk_idx):
        """
        Implements the in-memory sort for a given array of integers and stores
        the result in the file path that simulates the external memory
        (self.__external_mem_path).

        Args:
            int_array (np.array): Array of integers to be sorted.
            chunk_idx (int): Index that identifies the chunk from which
                int_array was taken.

        """

        ordered_array = np.sort(int_array, kind="quicksort")
        dest_file_name = str(chunk_idx) + self.__source_file_name
        dest_file_path = os.path.join(self.__external_mem_path, dest_file_name)
        ordered_array.tofile(dest_file_path)

    def __sort_chunks(self):
        """
        Gets the integers from each chunk of the source binary file in order to
        apply an in-memory sort algorithm on them.

        Parallelization could be applied here: each chuck is sorted by a single
        thread.

        """

        with open(self.__source_file_path, "rb") as f:
            for i in range(self.__num_chunks):
                offset = int(i * self.__chunk_byte_size)
                chunk_ints = np.fromfile(
                    f,
                    count=self.__m,
                    dtype="int32")
                self.__sort_ints(chunk_ints, i)

    def __insert_first_ints_in_heap(self, heap):
        """
        For every file in the external memory, reads the first integer and
        inserts it into the specified heap.

        Args:
            heap (list): list representing a heapq heap.

        """

        file_idx = 0

        for filename in os.listdir(self.__external_mem_path):
            filepath = os.path.join(self.__external_mem_path, filename)

            with open(filepath, "rb") as f:
                first_int = np.fromfile(f, count=1, dtype="int32")

                if len(first_int) > 0:
                    first_int = first_int[0]
                    heapq.heappush(heap, (first_int, file_idx))

            file_idx += 1

        return heap

    def __read_int_from_external_file(self, file_name, file_pointer):
        """
        Reads next integer to be read from file_name keeping file_pointer into
        account in order to calculate offset.

        Args:
            file_name (str): file to read.
            file_pointer (int): index of next integer to be read from file. It
                is used to calculate offset when reading.

        """

        file_path = os.path.join(self.__external_mem_path, file_name)

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

    def __init_files_pointers(self):
        """
        Returns and array filled with zeros for every file found in the
        external memory path.

        """

        num_files = len(os.listdir(self.__external_mem_path))

        return np.zeros(num_files, dtype="int32")

    def __merge_sorted_chunk_files(self):
        """
        Once all chunks have been sorted and these results are stored in the
        external memory as files, these are merged into one single sorted file.

        It uses a min-heap-based approach.

        """

        heap = []
        heapq.heapify(heap)

        heap = self.__insert_first_ints_in_heap(heap)
        file_names = os.listdir(self.__external_mem_path)
        file_pointers = self.__init_files_pointers()
        dest_file_path = os.path.join(self.__dest_path, self.__source_file_name)

        with open(dest_file_path, "wb+") as f:
            while len(heap) > 0:
                smallest_node = heapq.heappop(heap)
                smallest_int = smallest_node[0]
                file_idx = smallest_node[1]

                f.write(smallest_int)
                file_pointers[file_idx] += 1

                int2insert = self.__read_int_from_external_file(
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

        self.__clean_external_memory()
        self.__sort_chunks()
        self.__merge_sorted_chunk_files()
        self.__clean_external_memory()
