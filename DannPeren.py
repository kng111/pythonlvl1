def main(n):# Целочисленная переменная
    age = n

    # Переменная с плавающей запятой
    height = 1.75

    # Строковая переменная
    name = "John Doe"

    # Логическая переменная (True или False)
    is_student = True

    # Список
    grades = [90, 85, 78, 95, 88]

    # Кортеж
    coordinates = (10, 20)

    # Словарь
    person = {
        "name": "Alice",
        "age": 30,
        "is_student": False
    }

    # Вывод информации о переменных
    print(f"Имя: {name}")
    print(f"Возраст: {age} лет")
    print(f"Рост: {height} м")
    print(f"Студент: {is_student}")

    print(f"Оценки: {grades}")
    print(f"Координаты: {coordinates}")
    print(f"Информация о персоне: {person}")

    # Выполнение арифметических операций
    a = 10
    b = 5

    sum_result = a + b
    sub_result = a - b
    mul_result = a * b
    div_result = a / b
    mod_result = a % b
    exp_result = a ** b

    print(f"Сумма: {sum_result}")
    print(f"Разность: {sub_result}")
    print(f"Произведение: {mul_result}")
    print(f"Деление: {div_result}")
    print(f"Остаток от деления: {mod_result}")
    print(f"Возведение в степень: {exp_result}")

if __name__ == "__main__":
    main(25)
    print("Этот код выполняется только если программа запущена напрямую, а не импортирована в другой модуль.")