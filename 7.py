students = ["sandeep", "suresh", "vikas"]
marks = [90, 80, 70]
student_marks = {}

for index, student in enumerate(students):
    student_marks[students[index]] = marks[index]
    print(student_marks)