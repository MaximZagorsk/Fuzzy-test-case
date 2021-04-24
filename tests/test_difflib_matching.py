from difflib import SequenceMatcher
import sys
import os
sys.path.append(os.path.abspath(os.curdir)[:-6])
import time
from fuzzyclass import FuzzyProgram

class DifflibRatioTest(FuzzyProgram):
    def matching(self, str1, str2):
        return round(SequenceMatcher(None, str1, str2).ratio() * 100)




if __name__ == "__main__":
    name_file1 = "example1.txt"
    name_file2 = "example2.txt"
    a = DifflibRatioTest(name_file1, name_file2, "=100")
    start_time = time.time()
    a.create_matching()
    print("--- %s seconds ---" % (time.time() - start_time))
    #Файл в 6 мб обрабатывает --- 92.68708753585815 seconds ---
