class Power:
    def __init__(self, base, exponent):
        self.base = base
        self.exponent = exponent
    def addexponent(self):
        self.exponent += 1
    def getTotal(self):
        return self.base**self.exponent
    def getBase(self):
        return self.base
    def getexponent(self):
        return self.exponent
    def printSelf(self):
        print self.base
        print self.exponent