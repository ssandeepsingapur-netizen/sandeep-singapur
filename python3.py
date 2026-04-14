import math

num = float(input("Enter a number "))

if num <= 0:
    print("please enter a positive number.")
else:
    result = math.log(num)
    print("The  natural logarithm of {num} is : {result}")