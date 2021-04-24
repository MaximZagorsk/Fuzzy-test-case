import numpy as np
from threading import Thread
import sys
import os
sys.path.append(os.path.abspath(os.curdir)[:-6])
import time
from fuzzyclass import FuzzyProgram


class LevenshteinTest(FuzzyProgram):
    def matching(self, str1, str2):
        return int(round(self.levenshtein_ratio_and_distance(str1, str2) * 100))

    def levenshtein_ratio_and_distance(self, s, t):
        """ levenshtein_ratio_and_distance:
            Calculates levenshtein distance between two strings.
            If ratio_calc = True, the function computes the
            levenshtein distance ratio of similarity between two strings
            For all i and j, distance[i,j] will contain the Levenshtein
            distance between the first i characters of s and the
            first j characters of t
        """
        # Initialize matrix of zeros
        rows = len(s) + 1
        cols = len(t) + 1
        distance = np.zeros((rows, cols), dtype=int)

        # Populate matrix of zeros with the indeces of each character of both strings
        for i in range(1, rows):
            for k in range(1, cols):
                distance[i][0] = i
                distance[0][k] = k

        # Iterate over the matrix to compute the cost of deletions,insertions and/or substitutions
        for col in range(1, cols):
            for row in range(1, rows):
                if s[row - 1] == t[col - 1]:
                    cost = 0
                else:
                    cost = 2
                distance[row][col] = min(distance[row - 1][col] + 1,  # Cost of deletions
                                         distance[row][col - 1] + 1,  # Cost of insertions
                                         distance[row - 1][col - 1] + cost)  # Cost of substitutions

        Ratio = ((len(s) + len(t)) - distance[row][col]) / (len(s) + len(t))
        return Ratio


if __name__ == "__main__":
    name_file1 = "example1.txt"
    name_file2 = "example2.txt"
    a = LevenshteinTest(name_file1, name_file2, "=100")
    start_time = time.time()
    a.create_matching()
    print("--- %s seconds ---" % (time.time() - start_time))

