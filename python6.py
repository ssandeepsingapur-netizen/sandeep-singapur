def is_pronic_number(num):
   for i in range(1,int(num**0.5)+1):
        if n * (n+1) == num:
            return True

print("pronic numbers between 1 and 100:")
for num in range(1,101):
    if is_pronic_number(num):
        print(num, end=' ')