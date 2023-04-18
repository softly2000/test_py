from library.read_napr import ReadNapr

class KontrNapr:
    def __init__(self, filename):
        self.filename = filename
        self.nameNapr = ""

    def setNameNapr(self):
        try:
            rn = ReadNapr(self.filename)
            napr, kNapr = rn.setNapr()
        except FileNotFoundError:
            print("Ошибка: файл не найден")
            return self.nameNapr

        if kNapr > 0:
            print("Выберите направление:")
            for i in range(kNapr):
                print(f"{i + 1}. {napr[i]}")

            while True:
                choice = input("Введите номер направления: ")
                if choice.isdigit() and int(choice) in range(1, kNapr+1):
                    self.nameNapr = napr[int(choice)-1]
                    print(f"Выбрано направление: {self.nameNapr}")
                    break
                else:
                    print("Некорректный ввод.")
        else:
            print("Нет доступных направлений.")

        return self.nameNapr



















        
"""
   class KontrNapr:
    def __init__(self, filename):
        self.filename = filename
        self.nameNapr = ""
        self.naprList = []

    def setNapr(self):
        napr = []
        with open(self.filename, "r") as f:
            # читаем первую строку и игнорируем ее
            f.readline()

            # читаем дату и игнорируем ее
            f.readline()

            # читаем список направлений
            line = f.readline().strip()
            while line != "END":
                napr.append(line)
                line = f.readline().strip()

        self.naprList = napr
        return napr

    def setNameNapr(self):
        try:
            rn = ReadNapr(self.filename)
            napr, kNapr = rn.setNapr()
        except FileNotFoundError:
            print("Ошибка: файл не найден")
            return self.nameNapr

        if kNapr > 0:
            print("Выберите направление:")
            for i in range(kNapr):
                print(f"{i + 1}. {napr[i]}")

            while True:
                choice = input("Введите номер направления: ")
                if choice.isdigit() and int(choice) in range(1, kNapr+1):
                    self.nameNapr = napr[int(choice)-1]
                    print(f"Выбрано направление: {self.nameNapr}")
                    break
                else:
                    print("Некорректный ввод.")
        else:
            print("Нет доступных направлений.")

        return self.nameNapr

    def getChosenNapr(self):
        return self.nameNapr
"""