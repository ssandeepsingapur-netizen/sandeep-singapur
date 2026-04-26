class animal:
    def sound(self):
        print("animal makes sound")

class Dog(animal):
    def bark(self):
        print("dog barks")

d = Dog()
d.sound()
d.bark()