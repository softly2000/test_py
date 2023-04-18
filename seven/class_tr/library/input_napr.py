class InputNapr:
    def __init__(self):
        self.napr = []
        self.kNapr = 0
    
    def setNapr(self):
        while True:
            try:
                n = int(input("Введите количество направлений: "))
                for i in range(n):
                    napr_name = input(f"Введите название направления {i + 1}: ").upper()
                    self.napr.append(napr_name)
                self.kNapr = n
                return self.napr
            except ValueError:
                print("Ошибка: количество направлений должно быть целым числом")
