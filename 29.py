class cat:
    def sound(self):
        print("Meow")

class cow:
    def sound(self):
        print("amboo")

for animal in (cat(),cow()):
    animal.sound()