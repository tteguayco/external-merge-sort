import os
import time
import utils.randomint as rndint

# -----------------------------------------------------------------------------

N = 1_000_000_000
DATA_PATH = "./src/data/"
DATA_FILE_EXT = ".dat"
DATA_LINE_SEP = "\n"

# -----------------------------------------------------------------------------


def generate_file_path():
    """
    Generates a full path for a data file.

    """
    filename = "sample" + DATA_FILE_EXT

    return os.path.join(DATA_PATH, filename)


if __name__ == "__main__":
    rnd_int_generator = rndint.RandomIntGenerator()
    filepath = generate_file_path()

    start = time.time()
    rnd_ints = rnd_int_generator.get_random_int_list(size=N)
    rnd_ints.tofile(filepath)
    end = time.time()
    elapsed_time = end - start

    print("Process finished. Elapsed time: {} seconds".format(elapsed_time))
