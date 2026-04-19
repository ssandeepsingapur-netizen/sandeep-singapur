pin = 123
trials = 0
input_pin = int(input("Enter your pin: "))

while trials < 3:
    if input_pin == pin:
        print("Pin is correct!")
        break
    else:
        print("Incorrect pin. Try again.")
        trials += 1
        input_pin = int(input("Enter your pin: "))
else:
    print("Too many incorrect attempts. Access denied.")