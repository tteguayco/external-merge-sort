import numpy as np

# -----------------------------------------------------------------------------

#INPUT_FILE_PATH = "./src/external/sorted/0sample.dat"
#INPUT_FILE_PATH = "./src/data/unsorted/sample.dat"
INPUT_FILE_PATH = "./src/data/sorted/sample.dat"

# -----------------------------------------------------------------------------


def get_int_array_from_file(file_path):
    with open(file_path, "rb") as f:
        return np.fromfile(f, dtype="int32")


def is_sorted(int_array):
    return np.all(int_array[:-1] <= int_array[1:])


if __name__ == "__main__":
    int_array = None
    sorted = False

    int_array = get_int_array_from_file(INPUT_FILE_PATH)

    if int_array is not None:
        sorted = is_sorted(int_array)

    if sorted:
        print("File is sorted.")
    else:
        print("File is not sorted.")

    print("File length: {0}".format(len(int_array)))

    print(int_array[:10])
    print(int_array[-10:])
