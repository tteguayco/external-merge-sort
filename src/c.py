import numpy as np

# -----------------------------------------------------------------------------

#INPUT_FILE_PATH = "./src/external/sorted/0sample.dat"
#INPUT_FILE_PATH = "./src/data/unsorted/sample.dat"
INPUT_FILE_PATH = "./src/data/sorted/sample.dat"

# -----------------------------------------------------------------------------

if __name__ == "__main__":
    int_array = None
    sorted = False

    with open(INPUT_FILE_PATH, "rb") as f:
        int_array = np.fromfile(f, dtype="int32")

    if int_array is not None:
        sorted = np.all(int_array[:-1] <= int_array[1:])

    print(sorted)
    print(len(int_array))
    print(int_array[:100])
