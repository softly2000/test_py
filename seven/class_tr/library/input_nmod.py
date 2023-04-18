class InputNmod:
    def __init__(self, n):
        self.nmod = None
        self.ko = None
        self.n = n
    
    def setNmod(self):
        while True:
            try:
                self.nmod = int(input("Введите номер модуля: "))
                if self.nmod not in range(1, self.n + 1):
                    raise ValueError
                self.ko = 0
                return self.nmod
            except ValueError:
                print(f"Ошибка: номер модуля должен быть целым числом от 1 до {self.n}")
    
    def setKo(self):
        if self.nmod is None:
            self.ko = 1
        else:
            self.ko = 0
