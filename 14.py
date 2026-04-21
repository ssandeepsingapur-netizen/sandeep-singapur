def total_sum(*numbers):
    result = 0
    for num in numbers:
        result += num
    return result
print(total_sum(1, 2, 3, 4, 5))





def student_info(** details):
    for key, value in details.items():
        print(f"{key}: {value}")

student_info(name="Alice", age=20, grade="A")