from fuzzywuzzy import fuzz


class FuzzyProgram:
    def __init__(self, name_file1, name_file2, metrica, split_num=3):
        self.file1_name = name_file1
        self.file2_name = name_file2
        self.metrica = metrica
        self.split_num = split_num

    # Функция разделения строки по входному аргументу split_num
    def split_function(self, str):
        if self.split_num == 1:
            return str.split(" ")[0]
        if self.split_num == 2:
            return " ".join(str.split(" ")[:2])
        elif self.split_num == 3:
            return str

    # Функция проверки метрики и в случае совпадения значения метрики и функции соответсвия происходит запись в файл
    def check_metrica(self, file_output, str1, str2):
        match = self.matching(self.split_function(str1), self.split_function(str2))
        metrica_int = int(self.metrica[1:4])
        if self.metrica[0] == '>':
            if match >= metrica_int:
                file_output.write("{} => {}\n".format(str1, str2))
        elif self.metrica[0] == '=':
            if match == metrica_int:
                file_output.write("{} => {}\n".format(str1, str2))
        elif self.metrica[0] == '<':
            if match <= metrica_int:
                file_output.write("{} => {}\n".format(str1, str2))

    # Функция для поиска соответсвия
    def create_matching(self):
        file_output = open('result.txt', 'w')
        file1 = open(self.file1_name, "r", encoding='utf-8')
        for str1 in file1:
            file2 = open(self.file2_name, "r", encoding='utf-8')
            for str2 in file2:
                str1 = str1.replace("\n", "")
                str2 = str2.replace("\n", "")
                self.check_metrica(file_output, str1, str2)
            file2.close()
        file1.close()
        file_output.close()

    # Функция проверки нечеткого сравнения строк
    def matching(self, str1, str2):
        return fuzz.ratio(str1, str2)
