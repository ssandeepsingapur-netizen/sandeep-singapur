class student:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
s1 = student("sandy", 19)
s1.display()