class KontrN:
    def __init__(self, prompt, range):
        self.num = None
        self.ko = None
        self.prompt = prompt
        self.range = range
    
    def setNum(self):
        while True:
            try:
                self.num = int(input(self.prompt))
                if self.num not in self.range:
                    raise ValueError
                self.ko = 0
                return self.num
            except ValueError:
                print(f"Ошибка: число должно быть целым числом в диапазоне от {self.range[0]} до {self.range[-1]}")
    
    def setKo(self):
        if self.num is None:
            self.ko = 1
        else:
            self.ko = 0
