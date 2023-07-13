students = [
    ("Alice", 20, "Computer Science"),
    ("Bob", 22, "Mathematics"),
    ("Charlie", 19, "Physics"),
    ("Diana", 21, "Chemistry")
]

# Выводим информацию о каждом студенте
for student in students:
    name, age, major = student
    print(f'|Name: {name}, Age: {age}, Major: {major},|\n')