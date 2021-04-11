from fuzzyset import FuzzySet
import time
class FuzzyProgram:
    def __init__(self):
        self.file1 = open('example1.txt', "r",encoding='utf-8')
        self.file2 = open('example2.txt', "r", encoding='utf-8')
        self.metrica = '=100'
        # Функция определения совпадения
        # Функция записи в файл

    def create_massive_from_file2(self):
        file = self.file2
        temp = []
        for line in file:
            temp.append(line.replace("\n", ""))
        file.close()
        return temp

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
                    if int(round(fuzzy.get(temp[i])[0][0], 2) * 100) <= int(self.metrica[1:4]):
                        fileoutput.write("{} => {}\n".format(line, temp[i]))
        file1.close()


if __name__ == "__main__":
    a = FuzzyProgram()
    start_time = time.time()
    a.create_coincide_file()
    print("--- %s seconds ---" % (time.time() - start_time))

