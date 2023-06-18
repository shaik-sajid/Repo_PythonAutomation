class Bike:
    def myBike(self):
        print("Bike rides at 60 km/h")


class SportsBike(Bike):
    def mySportsBike(self):
        print("Sports Bike rides at 100 km/h")


class SuperBike(SportsBike):
    def mySuperBike(self):
        print("Super Bike runs at 200km/h")


grandChildren = SuperBike()
grandChildren.mySuperBike()
grandChildren.mySportsBike()
grandChildren.myBike()

parent = SportsBike()
parent.mySportsBike()
parent.myBike()
parent.mySuperBike()
