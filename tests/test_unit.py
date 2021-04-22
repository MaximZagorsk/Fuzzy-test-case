import unittest
import sys
import os

sys.path.append(os.path.abspath(os.curdir)[:-6])
from fuzzyclass import FuzzyProgram
from exceptions.fco_exception import FLException

# Класс unit тестирования
class TestMatchMethods(unittest.TestCase):

    # Тестирование функции split_function программы
    def test_func_split(self):
        test_class = FuzzyProgram("example1.txt", "example2.txt", "=100")
        FCS = "Иванов Иван Иванович"
        self.assertEqual(test_class.split_function(FCS), FCS)
        test_class.split_num = 1
        self.assertEqual(test_class.split_function(FCS), "Иванов")
        test_class.split_num = 2
        self.assertEqual(test_class.split_function(FCS), "Иванов Иван")
    # Тестирование функции matching программы
    def test_func_matching(self):
        test_class = FuzzyProgram("example1.txt", "example2.txt", "=100")
        self.assertEqual(test_class.matching("Иванов", "Иванов"), 100)
        self.assertEqual(test_class.matching("Иванов", "Сидоров"), 31)
        self.assertEqual(test_class.matching("Пеньков", "Петров"), 62)

    # Тестирование функции класса FCSException
    def test_fl_excepttion(self):
        test_class = FLException("example1.txt")
        self.assertRaises(TypeError, test_class.check_FL())


if __name__ == '__main__':
    unittest.main()
