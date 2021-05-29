import utils.sortprocessing as sortp

# -----------------------------------------------------------------------------

SOURCE_FILE_PATH = "./src/data/sample1.dat"
DEST_PATH = "./src/data/sorted/"
M = 3

# -----------------------------------------------------------------------------

if __name__ == "__main__":
    proc = sortp.ExternalMergeSortProcessor(SOURCE_FILE_PATH, DEST_PATH, m=M)
    proc.sort()
