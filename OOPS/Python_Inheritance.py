class Bird:
    bird = 10
    def myBird(self):
        print("Parrot flies below clouds")

class Eagle(Bird):
    eagle = 20
    def myEagle(self):
        print("Eagle flies on clouds")

obj = Eagle()
print(obj.eagle)
obj.myEagle()
print(obj.bird)
obj.myBird()

obj1 = Bird()
obj1.myBird()
obj1.myEagle()