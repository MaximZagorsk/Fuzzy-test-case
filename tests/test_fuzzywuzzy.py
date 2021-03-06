import time
import sys
import os
from fuzzywuzzy import fuzz

print(os.path.abspath(os.curdir)[:-6])
sys.path.append(os.path.abspath(os.curdir)[:-6])
from fuzzyclass import FuzzyProgram


class FuzzywuzzyTest(FuzzyProgram):

    def matching(self, str1, str2):
        return fuzz.ratio(str1, str2)


if __name__ == "__main__":
    name_file1 = "example1.txt"
    name_file2 = "example2.txt"
    a = FuzzywuzzyTest(name_file1, name_file2, "=100", 1)
    start_time = time.time()
    a.create_matching()
    print("--- %s seconds ---" % (time.time() - start_time))
    # Файл в 8 мб обрабатывает 42 сек
