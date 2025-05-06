class Superhero:
    def __init__(self, name, power, level):
        self.name = name
        self.power = power
        self._level = level  

    def show_power(self):
        print(f"{self.name} uses {self.power}!")

    def get_level(self):
        return self._level

    def level_up(self):
        self._level += 1
        print(f"{self.name} leveled up! Now at level {self._level}.")

class FlyingHero(Superhero):
    def __init__(self, name, level):
        super().__init__(name, power="Flight", level=level)

    def show_power(self):
        print(f"{self.name} soars through the skies with level {self.get_level()} power! ✈️")

#activity 2
class Vehicle:
    def move(self):
        print("Vehicle is moving...")

class Car(Vehicle):
    def move(self):
        print("Driving on the road 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying in the sky ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing on the water 🚢")