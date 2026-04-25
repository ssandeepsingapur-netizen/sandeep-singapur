class Dog :
    def __init__ (self, name, breed):
        self.name = name
        self.breed = breed
    def bark(self):
        print(f"{self.name} says barking!")

Dog1 = Dog("rex", "beedi nayi")
Dog2 = Dog("tommy", "german shepherd")
Dog1.bark()
Dog2.bark()