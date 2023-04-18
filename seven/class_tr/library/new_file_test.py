import datetime

class NewFileTest:
    def __init__(self, filename, first_line, napr):
        self.filename = filename
        self.first_line = first_line
        self.napr = napr
        self.ko = None
    
    def setKo(self):
        if self.ko == 0:
            print(f"Файл {self.filename} успешно создан")
        else:
            print(f"Ошибка при создании файла {self.filename}")
    
    def createFile(self):
        try:
            with open(self.filename, "a") as f:
                f.write(self.first_line)
                f.write("\n")
                f.write(str(datetime.datetime.now()))
                f.write("\n")
                f.write(str(self.napr))
                f.write("\n")
                f.write("END\n")
            self.ko = 0
        except Exception as e:
            print(f"Ошибка: {e}")
            self.ko = 1
            self.setKo()




