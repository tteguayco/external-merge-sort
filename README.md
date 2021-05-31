# External merge sort

## Install dependencies

Dependencies for the project are listed inside the ```requirements.txt``` file and can be installed via pip from the root directory:

```pip install -r ./requirements.txt```

## Project structure

The project is organized mainly in source code files located in ```src``` and some unit tests in ```tests```.

In the root of the ```src``` folder, one file per exercise can be found: ```a.py```, ```b.py``` and ```c.py```.

Input (unsorted) file and output (sorted) files are read and written from and to ```src/data```.

External memory is simulated on ```src/external```.

**Note:** Execution of ```b.py``` takes around 20 minutes for an input file containing ```10_000_000``` integers.

## Run the tests

Tests can be run via the following command from the ```tests``` folder:

```python -m unittest```

## Answers to proposed questions

1. **This program is likely to be I/O bound. Is there any way to take advantage of this?**

2. **Are there parts of the program that can be parallelized across multiple cores in the same machine?**

3. **Across multiple disks in the same machine?**

4. **Across multiple machines?**

5. **How would one choose M for different N, cores, spindles, and machines?**

