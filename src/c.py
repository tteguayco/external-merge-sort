import numpy as np

# -----------------------------------------------------------------------------

INPUT_FILE_PATH = "./src/external/sorted/1sample1.dat"
#INPUT_FILE_PATH = "./src/data/sample1.dat"

# -----------------------------------------------------------------------------

if __name__ == "__main__":
    int_array = None
    sorted = False

    with open(INPUT_FILE_PATH, "rb") as f:
        int_array = np.fromfile(f, dtype="int32")

    if int_array is not None:
        sorted = np.all(int_array[:-1] <= int_array[1:])

    print(sorted)
