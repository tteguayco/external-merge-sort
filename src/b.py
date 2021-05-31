import utils.sortprocessing as sortp

# -----------------------------------------------------------------------------

SOURCE_FILE_PATH = "./src/data/unsorted/sample.dat"
DEST_PATH = "./src/data/sorted/"
EXTERNAL_MEM_PATH = "./src/external/sorted/"
M = 10_000

# -----------------------------------------------------------------------------

if __name__ == "__main__":
    proc = sortp.ExternalMergeSortProcessor(
        SOURCE_FILE_PATH, DEST_PATH, EXTERNAL_MEM_PATH, m=M)
    proc.sort()
