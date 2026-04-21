def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))



def outer_function(name):
    print(f"Hello {name}")
    def inner_innerfunction():
        print(f"This is inner function")
        inner_innerfunction()
outer_function("sandy")

        