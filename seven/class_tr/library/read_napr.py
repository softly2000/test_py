class ReadNapr:
    def __init__(self, filename):
        self.filename = filename
        self.napr = []
        self.kNapr = 0
        self.ko = 0
        
    def setNapr(self):
        try:
            with open(self.filename, 'r') as f:
                self.napr = f.readlines()
                self.napr = [x.strip() for x in self.napr]
                self.kNapr = len(self.napr)
                self.ko = 0
        except FileNotFoundError:
            self.ko = 2
    
        if self.kNapr == 0:
            self.ko = 1
        
        return self.napr, self.kNapr
    
    def setKo(self):
        return self.ko