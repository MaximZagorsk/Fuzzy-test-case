from fuzzyset import FuzzySet
import sys
import os

sys.path.append(os.path.abspath(os.curdir)[:-6])
import time
from fuzzyclass import FuzzyProgram


class FuzzySetTest(FuzzyProgram):
    def matching(self, str1, str2):
        fuzzy = FuzzySet()
        fuzzy.add(str1)
        return round(fuzzy.get(str2)[0][0] * 100)


if __name__ == "__main__":
    name_file1 = "example1.txt"
    name_file2 = "example2.txt"
    a = FuzzySetTest(name_file1, name_file2, "=100")
    start_time = time.time()
    a.create_matching()
    print("--- %s seconds ---" % (time.time() - start_time))
    # Файл в 6 мб обрабатывает --- 116.77557706832886 seconds ---
