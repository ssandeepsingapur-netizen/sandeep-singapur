import random

numbers = random.randint(1,100)

while True:
    guess = int(input("enter your guess(1-100): "))
    if guess < numbers:
        print("too low")
    elif guess > numbers:
        print("too high")
    else:
        print("correct! you win")
        break