class Car:
   def __init__ (self, brand, model):
       self.brand = brand
       self.model = model
   def display_info(self):
       print(f"car brand: {self .brand}, model:{self.model}")
    
my_car =Car("Toyota","camry")
my_car.display_info()
