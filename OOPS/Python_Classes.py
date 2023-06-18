class Calculator:
    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    var = 10


obj = Calculator()
print(Calculator.sum('Sum', 10, 20))
print(obj.sub(20, 10))
print(obj.var)
