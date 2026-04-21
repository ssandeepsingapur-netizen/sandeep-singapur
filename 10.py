def add(*a):
    print(type(a))

    return sum(a)

add(1,2,3,4,5)
print(add(1,2,3,4,5))


result = lambda a,b: a+b
print(result(10,20))
