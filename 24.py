class person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello,my name is {self.name} and I am {self.age} years old.")
person1 = person("Alice", 30)
person2 = person("ashwini", 18)
person1.greet()
person2.greet()