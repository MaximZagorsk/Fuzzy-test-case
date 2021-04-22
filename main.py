from fuzzyclass import FuzzyProgram
import time
import argparse
from exceptions.fco_exception import FLException

# Создание CLI интерфейса
parser = argparse.ArgumentParser(description='Программа по нечеткому сравнению строк')
parser.add_argument('file1',
                    type=str,
                    help='Вводится имя первого файла для проверки с форматом (Пример: example1.txt)'
                    )

parser.add_argument('file2',
                    type=str,
                    help='Вводится имя второго файла для проверки с форматом (Пример: example2.txt)'
                    )

parser.add_argument('metrica',
                    type=str,
                    help='Вводится процент сравнения файла ,'
                         ' " = " - в результате будут все равные значения,'
                         ' " > " - результатом будут значения больше и равные заданного,'
                         ' " < " - результатом будут значения меньше и равные заданного.'
                    )

parser.add_argument('--FL_optional',
                    type=int,
                    default=3,
                    help='Необезателньый аргумент поиско по ФИО. '
                         'Если передается 1, то поиск производится только по фамилии, если 2, то по фамилии и'
                         'имени, если 3, то по всему ФИО. default: 3 '
                    )

args = parser.parse_args()

# Проверка файла на пустые строки и соответсвие формату ФИО
try:
    print("--- Проверка файлов на соотвествие формату ФИО ---")
    check_file1 = FLException(args.file1)
    check_file2 = FLException(args.file2)
    check_file1.check_FL()
    check_file2.check_FL()
    print("--- Проверка прошла успешно! ---")
except TypeError:
    print("--- WARNING --- \n Проверка файлов не прошла,"
          " один из файлов несоответсвует формату ФИО, вычисление продолжается\n"
          "--- WARNING --- ")

print("--- Начало работы программы ---")
a = FuzzyProgram(args.file1, args.file2, args.metrica, split_num=args.FL_optional)
start_time = time.time()
a.create_matching()
print("--- %s seconds ---" % (time.time() - start_time))
print("--- Поиск выполнен! Результаты будут находиться в файле result.txt ---")
