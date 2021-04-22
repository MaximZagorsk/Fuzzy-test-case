class FLException:
    def __init__(self, name_file):
        self.file1 = open(name_file, "r", encoding='utf-8')


    def check_FL(self):
        for line in self.file1:
            line = line.replace("\n", "")
            line = line.split(" ")
            if len(line) == 3:
                for i in line:
                    if i == "":
                        print(line)
                        raise TypeError("Файл не соответсвует формату ФИО")
            else:
                raise TypeError("Файл не соответсвует формату ФИО или содержит пустую строку")