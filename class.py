class FourCal:
    def setdata(self, first, second):
        self.aaa = first
        self.bbb = second
        self.ccc = 20
    def sum(self):
        result = self.aaa + self.bbb + self.ccc
        return result
    def mul(self):
        result = self.aaa * self.bbb
        return result
    def sub(self):
        result = self.aaa - self.bbb
        return result
    def div(self):
        result = self.aaa / self.bbb
        return result


a = FourCal()
b = FourCal()
a.setdata(4, 2)
b.setdata(3, 7)
a.sum()
b.sum()
print(a.sum(), "aaa")
print(b.sum(), "bbb")
