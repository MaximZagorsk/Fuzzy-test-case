from fuzzyset import FuzzySet


class FuzzyProgram:
    # Инициализация программ
    def __init__(self):
        print("Введите имя первого файла с форматом(Пример: example1.txt)")
        self.file1 = open(input(), "r", encoding="utf-8")
        print("Введите имя второго файла c форматом(Пример: example1.txt)")
        self.file2 = open(input(), "r", encoding="utf-8")
        # Метрика задается процентным значением и знаком равенства, где "=" - это все равные значения,
        # " > " - это больше заданного значения, "<" - это меньше заданного значения
        print("Введите требуемый процент сходства со знаком равенства (Пример: =100) ")
        self.metrica = input()

    # Функция создания массива данных второго файла для сравнения с первым
    def create_massive_from_file2(self):
        file = self.file2
        temp = []
        for line in file:
            temp.append(line.replace("\n", ""))
        file.close()
        return temp

    # Функция создания файла результатов сравненмя
    def create_coincide_file(self):
        temp = self.create_massive_from_file2()
        file1 = self.file1
        fileoutput = open("result.txt", "w")
        for line in file1:
            line = line.replace("\n", "")
            fuzzy = FuzzySet()
            fuzzy.add(line)
            for i in range(len(temp)):
                if self.metrica[0] == '>':
                    if int(round(fuzzy.get(temp[i])[0][0], 2) * 100) >= int(self.metrica[1:4]):
                        fileoutput.write("{} => {}\n".format(line, temp[i]))
                elif self.metrica[0] == '=':
                    if int(round(fuzzy.get(temp[i])[0][0], 2) * 100) == int(self.metrica[1:4]):
                        fileoutput.write("{} => {}\n".format(line, temp[i]))
                elif self.metrica[0] == '<':
                    fileoutput.write("{} => {}\n".format(line, temp[i]))
        file1.close()
