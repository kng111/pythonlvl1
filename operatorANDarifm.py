def main(n,z):
    # Арифметические операторы
    a = n #(10)
    b = z # (3)

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

    # Логические операторы
    x = True
    y = False

    and_result = x and y
    or_result = x or y
    not_result = not x

    print(f"Результат операции 'x and y': {and_result}")
    print(f"Результат операции 'x or y': {or_result}")
    print(f"Результат операции 'not x': {not_result}")

    # Операторы сравнения
    age = 25
    height = 1.75

    is_student = True

    print(f"Возраст больше 18? {age > 18}")
    print(f"Рост меньше 1.8 м? {height < 1.8}")
    print(f"Студент? {is_student}")

    # Операторы присваивания
    x = 10
    y = 5

    x += y  # x = x + y
    print(f"Результат операции 'x += y': {x}")

    x -= y  # x = x - y
    print(f"Результат операции 'x -= y': {x}")

    x *= y  # x = x * y
    print(f"Результат операции 'x *= y': {x}")

    x /= y  # x = x / y
    print(f"Результат операции 'x /= y': {x}")

    x %= y  # x = x % y
    print(f"Результат операции 'x %= y': {x}")

    x **= y  # x = x ** y
    print(f"Результат операции 'x **= y': {x}")

    # Операторы идентичности
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    list3 = list1

    print(f"list1 is list2? {list1 is list2}")
    print(f"list1 is list3? {list1 is list3}")

    # Операторы членства
    fruits = ["apple", "banana", "cherry"]

    print(f"Is 'apple' in fruits? {'apple' in fruits}")
    print(f"Is 'orange' not in fruits? {'orange' not in fruits}")
if __name__ == "__main__":
    main(10,3)
    print("Этот код выполняется только если программа запущена напрямую, а не импортирована в другой модуль.")