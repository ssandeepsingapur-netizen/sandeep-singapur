students = [
    {"name": "Alice", "marks": 20},
    {"name": "Bob", "marks": 30},
    {"name": "charlie", "marks": 40}
]

students.sort(key=lambda x: x["marks"], reverse=True)
print(students)