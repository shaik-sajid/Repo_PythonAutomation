class MyConstructor:
    num = 100 #Class Variables

    def __init__(self, a , b):
        self.firstNumber = a #instance variables
        self.secondNumber = b
        print("Default constructor")

    def add(self):
        var = 10 #local variables
        return self.firstNumber + self.secondNumber + self.num

    def sub(self):
        return MyConstructor.num - (self.firstNumber + self.secondNumber)

obj = MyConstructor(11, 22)
print(obj.add())
print(obj.sub())